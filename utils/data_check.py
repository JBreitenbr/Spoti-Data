import pandas as pd
"""
df=pd.read_csv("brock6.csv")

df=df.reset_index(drop=True)
gr=pd.DataFrame(df["track_id"].value_counts())
dupli=gr[gr["count"]>1]
lst=dupli.index.tolist()
print(len(lst))
tev=df[df["track_id"].isin(lst)][["artist","album","track"]]
tev.to_csv("tev6.csv")

"""
df0=pd.read_csv("brock6.csv")
df0=df0.reset_index(drop=True)
df=df0
alb=pd.read_csv("album_info_6.csv")
ids=pd.read_csv("test_ids_6.csv")[["track_id","album_id","artist_id"]]
ids=ids.reset_index(drop=True)
mrg1=pd.merge(ids,alb,on="album_id")
mrg=pd.merge(df,mrg1,on="track_id")
for i in range(len(mrg)):
  exp1=mrg.loc[i,"album_tracks"]
  exp2=mrg.loc[i,"track"]
  try:
     clause=exp1.index(exp2)
  except:
     clause=-1
  mrg.loc[i,"indexOf"]=clause
lst=mrg["indexOf"].tolist()
art=pd.read_csv("artist_genres_6.csv")
mrg2=pd.merge(mrg,art,on="artist_id")
print("len")
print(len(mrg2))
#print(lst)
neg=[]
for i in range(len(lst)):
   if lst[i]==-1:
     neg.append(i)
print(neg)
tc=mrg[mrg["indexOf"]<0]
tc.to_csv("tc6_.csv")
mrg2.to_csv("brock6_cleaned.csv",index=False)
"""
lst=df["track_id"].tolist()
for i in range(len(lst)):
   if lst[i][0:2]=="38":
      print(i)
"""
      