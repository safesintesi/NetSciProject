# NetSciProject

1) select the artists we want to talk about

2) select the hashtags & keywords & @s related to those artists (group by id)

3) select positive & negative words (assign positive or negative weight to the tweet)

4) create a network of users and artists

5) create links counting tweet weight

6) connecting artists by "proximity": network 2

7) check differences between befor and after eurovision (maybe check older eurovision verions)
 
NOTES

April 1 - August 1

# HOW TO RUN THE CODE
0) make sure to set up your dev environments

You can find them in the side nav bar on Twitter's dev portal. Set up "Search Tweets: Full Archive / Sandbox" and call it NetworkScience1

1) `pip install -r requirements.txt`

this should install the necessary packages for running the script

2) `py main.py` or `python3 main.py`

this will run the script

3) follow the instructions

## Troubleshooting

if your scripts gives a file missing error try creating two empty folders, one called "data" and the other called "lib" and run again the script.