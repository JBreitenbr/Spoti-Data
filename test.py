import pandas as pd
s=pd.read_csv("spotiData2_4.csv")
print(s.isnull().sum())
alph=s[s["alphaname"].isna()]
arts=alph["artist"].unique().tolist()
alph.to_csv("alph.csv",index=False)
comp=s[s["alphaname"].notna()]
print(len(comp))
comp.to_csv("comp.csv",index=False)