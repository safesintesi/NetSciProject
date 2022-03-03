import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

name = 'maneskin' #artist name as in save files

for i in range(0,4):
    filepath = "./temp/"+name+"_xd_"+str(i)+".csv"
    df = pd.read_csv(filepath)
    plt.axhline(y=0,linestyle=':')
    plt.axvline(linestyle=':')
    plt.scatter(df['tone_tweet'],df['avg_tone_neighbours'],alpha=0.5)
    plt.xlim(-1,1)
    plt.ylim(-0.2,0.2)
    plt.savefig("./temp/"+name+"_xd_"+str(i)+".png")
    plt.clf()
    
    


