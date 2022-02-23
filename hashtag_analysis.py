import pandas as pd
name = "maneskin"

def retrieve_hashtags(df: pd.DataFrame):
    print("selecting hashtags")
    hashtags = dict()
    for row in df.itertuples():
        ent = row.entities
        tone = row.Tone
        if "hashtags" in ent.keys():
            for ha in ent["hashtags"]:
                ha = ha["tag"].lower()
                if ha not in hashtags.keys():
                    hashtags[ha] = (tone, 1)
                else:
                    hashtags[ha] = (hashtags[ha][0] + tone, hashtags[ha][1] + 1)
    
    #averaging tones
    for ha in hashtags.keys():
        tone, num = hashtags[ha]
        hashtags[ha] = (tone/num, num)

    return hashtags

print("reading df")
tweet_df = pd.read_pickle("./tweets/"+ name +".pkl")
result_df = pd.read_csv("./results/"+ name +"_liwc.csv")
#result_df = pd.read_excel("./results/"+ name +"_liwc.xlsx")

print("merging df")
tweet_df = tweet_df[["id","created_at","entities"]]
result_df = result_df[["id","Tone"]]
df = pd.merge(tweet_df, result_df, on='id', how="inner")

#splitting df dates
dfs = []
dfs.append(df.loc[df['created_at'] > '2021-05-31T00:00:00.000Z'])
dfs.append(df.loc[(df['created_at'] > '2021-05-24T00:00:00.000Z') & (df['created_at'] < '2021-05-31T00:00:00.000Z')])
dfs.append(df.loc[(df['created_at'] > '2021-05-17T00:00:00.000Z') & (df['created_at'] < '2021-05-24T00:00:00.000Z')])
dfs.append(df.loc[df['created_at'] < '2021-05-17T00:00:00.000Z'])

i = 0
for x in dfs:
    print("retrieving hashtags" + str(i))
    hashtags = retrieve_hashtags(x)
    print(x.head())

    print("writing data" + str(i))
    filename = './tags/' + name + "_" + str(i) + '_tags.csv'
    with open(filename, 'w', encoding="utf-8") as f:
        for key in hashtags.keys():
            tone, num = hashtags[key]
            f.write("%s, %s, %s\n" % (key, tone, num))
    i = i + 1

