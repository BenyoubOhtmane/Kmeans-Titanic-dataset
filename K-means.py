import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
import numpy as np
from sklearn.cluster import KMeans
import pandas as pd
from sklearn import preprocessing

df=pd.read_excel("/Users/User/Desktop/ML0000/python/titanic.xls")
df.drop(["body","name"],1,inplace=True)
for k in df:
    k=pd.to_numeric(k,errors="ignore")
df.fillna(0,inplace=True)

def handle_non_numerical_data(df):
    columns=df.columns.values #regroups all columns names in a list
    for column in columns:
        text_digit_vals={}
        def convert_to_int(val):
            return text_digit_vals[val]
        if df[column].dtype!=np.int64 and df[column].dtype!=np.float64:
            column_contents=df[column].values.tolist() #Values into a list
            unique_elements=set(column_contents) #set() gives unique elements in a list
            x=0
            for unique in unique_elements:
                if unique not in  text_digit_vals:
                    text_digit_vals[unique]=x
                    x+=1

            df[column]=list(map(convert_to_int,df[column]))
    return df

df=handle_non_numerical_data(df)
df.drop(["sex"],1,inplace=True) #added at the end to see impact
print(df.head())

X=np.array(df.drop(["survived"],1).astype(float))
#X=preprocessing.scale(X)  #added at the end to see if there's any accuracy increase
y=np.array(df["survived"])

cf=KMeans(n_clusters=2)
cf.fit(X)

correct=0
for i in range(len(X)):
    predict_me=np.array(X[i].astype(float))
    predict_me=predict_me.reshape(-1,len(predict_me))
    prediction=cf.predict(predict_me)
    if prediction[0] ==y[i]:
        correct +=1

print(correct/len(X))