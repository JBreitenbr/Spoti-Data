import pandas as pd
s1=pd.read_csv("comp.csv")
s2=pd.read_csv("aleph.csv")
df=pd.concat([s1,s2])
df.reset_index(inplace=True)
for i in range(len(df)):
     df.loc[i,"year"]=df.loc[i,"album_date"][0:4]
for i in range(len(df)):
     su=df.loc[i,"track"]+" ("
     tr=df.loc[i,"album_tracks"]
     pos=tr.index(su)
     df.loc[i,"pos"]=pos
     df.sort_values(by=["alphaname","year","album_name","pos"],inplace=True)
del df["index"]
del df["year"]
del df["pos"]
df.to_csv("spotiData2_4_cl.csv",index=False)