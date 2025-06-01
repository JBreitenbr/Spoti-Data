import pandas as pd 
df=pd.read_csv("spotiData1_6.csv")
cnt=df["artist"].value_counts()
cnt.to_csv("counts.csv")