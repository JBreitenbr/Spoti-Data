import pandas as pd 
df=pd.read_csv("spotiData20_4.csv")
cnt=df["artist"].value_counts()
cnt.to_csv("count.csv")