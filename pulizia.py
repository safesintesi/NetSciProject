import os
from pathlib import Path
import pandas as pd

sl = int(input("inster your first line: "))
el = int(input("insert your last line: "))

for n in range(sl, el+1):
    df = pd.read_csv("./data/" + str(n) + ".csv")
    df["text"] = df["text"].str.replace("\n", " ")
    df.to_csv("./data/"+str(n)+".csv", index=False)
    df.to_pickle("./data/"+str(n)+".pkl")