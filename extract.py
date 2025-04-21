import pandas as pd
s=pd.read_csv("sub.csv")
s["alphaname"]=s["alphaname"].astype(str)

for i in range(len(s)):
  s.loc[i,"maiuscule"]=s.loc[i,"alphaname"].upper()[0]

mlst=s["maiuscule"].unique().tolist()

wDict={}
for i in range(len(mlst)):
  wDict[mlst[i]]=[]
blst=[]
for i in range(len(mlst)):
  hlp=s[s["maiuscule"]==mlst[i]]["artist"].unique().tolist()
  blst.append(hlp)
for i in range(len(blst)):
  for j in range(len(blst[i])):
    wDict[mlst[i]].append(blst[i][j])
print(wDict)
arr=[]
arr.append(wDict)
"""
for i in range(len(mlst)):
  wlst[i]["name"]=mlst[i]
  wlst[i]["bands"]=[]
blst=[]
for i in range(len(mlst)):
  hlp=s[s["maiuscule"]==mlst[i]]["artist"].unique().tolist()
  blst.append(hlp)
slst=[[] for i in range(len(mlst))]
for i in range(len(blst)):
  for j in range(len(blst[i])):
    slst[i].append({"name":blst[i][j]})
for i in range(len(wlst)):
  wlst[i]["bands"]=slst[i]
bands=pd.DataFrame(wlst)
"""
bands=pd.DataFrame(arr)
bands.to_json("newApproach.json",orient="records")

