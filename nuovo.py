import os
import pandas as pd

name = 'barbara_pravi' #artist name as in save files

df = pd.read_pickle("./tweets/"+ name +".pkl")
df = df.loc[df['lang'] == 'en']
#df1 = df1.loc[pd.isna(df1["withheld"]), df1.columns.drop('withheld')]
#df1 = df1[sorted(df1.columns)]
#df2 = pd.read_pickle('./tweets/maneskin_before.pkl')
#df2 = df2[sorted(df2.columns)]
#df = pd.concat([df1,df2], ignore_index=True)
#df["text"] = df["text"].str.replace("\n", " ")
#df.to_pickle("./tweets/"+ name +".pkl")


#print(df['created_at'])
dfa = df.loc[df['created_at'] > '2021-05-31T00:00:00.000Z']
dfb = df.loc[(df['created_at'] > '2021-05-24T00:00:00.000Z') & (df['created_at'] < '2021-05-31T00:00:00.000Z')]
dfc = df.loc[(df['created_at'] > '2021-05-17T00:00:00.000Z') & (df['created_at'] < '2021-05-24T00:00:00.000Z')]
dfd = df.loc[df['created_at'] < '2021-05-17T00:00:00.000Z']
#print(dfa['created_at'])
#print(dfb['created_at'])
#print(dfc['created_at'])
#print(dfd['created_at'])

dfa["text"].to_csv("./tweets/"+name+"_0531_0606.csv", index=False)
dfa.to_pickle("./tweets/"+name+"_0531_0606.pkl")
dfb["text"].to_csv("./tweets/"+name+"_0524_0531.csv", index=False)
dfb.to_pickle("./tweets/"+name+"_0524_0531.pkl")
dfc["text"].to_csv("./tweets/"+name+"_0517_0524.csv", index=False)
dfc.to_pickle("./tweets/"+name+"_0517_0524.pkl")
dfd["text"].to_csv("./tweets/"+name+"_0510_0517.csv", index=False)
dfd.to_pickle("./tweets/"+name+"_0510_0517.pkl")
#df.to_csv("./tweets/"+name+"_indexed.csv")
