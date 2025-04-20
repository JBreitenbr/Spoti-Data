import pandas as pd 
df0=pd.read_csv("spotiData20_4.csv")
cnt=pd.read_csv("count.csv")
df=pd.merge(df0,cnt,on="artist")
print(len(df))
s=df[df["count"]>10]
print(len(s))
s.to_csv("sub.csv",index=False)