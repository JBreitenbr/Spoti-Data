import pandas as pd 
df=pd.read_csv("spotiData6jun.csv")
cnt=df["artist"].value_counts()
cnt.to_csv("counts.csv")