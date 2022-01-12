import os
from pathlib import Path
import twitter as tw
import pandas as pd
import linecache as lc
import funcs as lib
import re

token = lib.getToken()
headers = lib.create_headers(token)

#select artists for tweet downloading
print("Read your lines from 'Pull splits'")
sl = int(input("inster your first line: "))
el = int(input("insert your last line: "))

#downloadin Tweets
for n in range(sl, el+1):
    #getting keywords from artists.txt
    line = lc.getline("./artists.txt", n)
    line = re.sub(r"(\(.*?\))", "", line) # remove (*something*)
    query = lib.crateQuery(line)

    #api request
    tweets = lib.get_single_response(
        headers,
        query, 
        "202104010000", #start time
        "202108010000", #end time
        "NetworkScience1", #poject label
        "fullarchive") #history mode (aka not recent)
    tweets_df = pd.DataFrame(tweets)

    #remove return char from text for formatting
    tweets_df["text"] = tweets_df["text"].str.replace("\n", " ")

    #save tweets
    tweets_df.to_csv("./data/"+str(n)+".csv", index=False)
    tweets_df.to_pickle("./data/"+str(n)+".pkl")

