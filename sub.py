import pandas as pd 
df0=pd.read_csv("spotiData1_6.csv")
cnt=pd.read_csv("counts.csv")
df=pd.merge(df0,cnt,on="artist")
print(len(df))
s=df[df["count"]>10]
print(len(s))
s.to_csv("sub.csv",index=False)