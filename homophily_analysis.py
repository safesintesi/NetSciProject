from os import rename
import pandas as pd
import numpy
from matplotlib import pyplot as plt
import math

name = "maneskin"

def check_entities(ent) -> bool:
    #if Nan is float
    return (type(ent) is not float)

def link_by_tags(df: pd.DataFrame) -> pd.DataFrame:

    dfs = []
    half = len(df) // 2
    dfs.append(df.iloc[:half])
    dfs.append(df.iloc[half:])

    joined = []
    for x in dfs:
        for y in dfs:
            t = x.merge(y, on='tag', how='inner')
            t.drop(columns='tag', inplace=True)
            t.drop_duplicates(ignore_index=True, inplace=True)
            t = t.loc[t['id_x'] != t['id_y']]
            joined.append(t)
    t = pd.concat(joined, ignore_index=True)
    return t

def get_tone(df: pd.DataFrame, id: str) -> int:
    idx = df['id'] == id
    return df.loc[idx, 'Tone'].iat[0]

def retrieve_links(df: pd.DataFrame):
    print("creating table id-tag")
    table = pd.DataFrame({
        'id': [],
        'tag': []})
    for row in df.itertuples():
        ent = row.entities
        if check_entities(ent) and ("hashtags" in ent.keys()):
            new_lines = [table]
            for ha in ent["hashtags"]:
                ha = ha["tag"].lower()
                if ha == "maneskin":
                    continue
                new_line = pd.DataFrame({
                    'id': row.id,
                    'tag': ha}, index=[0])
                new_lines.append(new_line)
            table = pd.concat(new_lines, ignore_index=True)
                
    table = link_by_tags(table)
    
    return table

print("reading df")
tweet_df = pd.read_pickle("./tweets/"+ name +".pkl")
result_df = pd.read_pickle("./temp/maneskin_italian_clean_scored_tweets_noduplicates.pkl") #, dtype={'id': 'str'}

print("merging df")
tweet_df = tweet_df[["id","created_at","entities"]]
result_df = result_df[["id","sentiment_score"]]
df = pd.merge(tweet_df, result_df, on='id', how="inner")


print("dividing dataframe")
dfs = []
dfs.append(df.loc[df['created_at'] > '2021-05-31T00:00:00.000Z'])
dfs.append(df.loc[(df['created_at'] > '2021-05-24T00:00:00.000Z') & (df['created_at'] < '2021-05-31T00:00:00.000Z')])
dfs.append(df.loc[(df['created_at'] > '2021-05-17T00:00:00.000Z') & (df['created_at'] < '2021-05-24T00:00:00.000Z')])
dfs.append(df.loc[df['created_at'] < '2021-05-17T00:00:00.000Z'])

print("slimming data")
temp = []
for df in dfs:
    df = df[['id', 'sentiment_score', 'entities']]
    temp.append(df)
dfs = temp

print("calculating homophily matrixes")
i = 0
result_df.rename(columns={"id":"id_y","sentiment_score":"tone_y"}, inplace=True)
for df in dfs:
    print("==============")
    links = retrieve_links(df[['id','entities']])
    #m = numpy.zeros(shape=(100,100),dtype=int)
    links = links.merge(result_df, on="id_y", how="inner")
    links.drop(columns='id_y', inplace=True)
    links = links.groupby('id_x').mean()

    result_df.rename(columns={"id_y":"id_x","tone_y":"tone_x"}, inplace=True)
    links = links.merge(result_df, on="id_x", how="inner")
    links.drop(columns='id_x', inplace=True)


    print("Scatter Plot")
    links.rename(columns={"tone_x":"tone_tweet","tone_y":"avg_tone_neighbours"}, inplace=True)
    links.to_csv("./temp/"+ name + "_xd_" + str(i) + ".csv", index=False)
    
    result_df.rename(columns={"id_x":"id_y","tone_x":"tone_y"}, inplace=True)
    i += 1
