import pandas as pd
s=pd.read_csv("sample.csv")
print(s.columns)
s.sort_values(by="alphaname",inplace=True)
for i in range(len(s)):
  

  mlst=s["maiuscule"].unique().tolist()
wlst=[]
for i in range(len(mlst)):
  wlst.append({})
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
bands.to_json("bandsObjTest.json",orient="records")