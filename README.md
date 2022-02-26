# WHAT HAS BEEN DONE SO FAR

The main idea is the study and comparison of the popularity boost gained by Eurovision 2021 winners, with a focus on Maneskin because they arrived 
first place and they're a good case study in general.

1. The tweets
We have retrieved tweets regarding the first 6 artists classified in the timespan May 10 - June 6. This has been done gathering all tweets containing
mentions of the official accounts of the artists or hashtags related to them. Each artist has its own set of tweets in .pkl format. Then, every set of
tweets has been split into 4 weeks and also converted to .csv. Finally, the english tweets from each artist have been extracted, their text has been
cleaned, and only some relevant columns have been kept, in order to produce an input file for the sentiment analysis software (the LIWC). The same has
been done with the italian Maneskin tweets because I found an italian sentiment dictionary that could be used (the Sentix).
All tweets are available in the "tweets" folder.

2. Sentiment analysis
Sentiment analysis of ONLY the english tweets has been automatically performed by LIWC. The results can be found in the results_liwc.zip file.
For italian tweets, the tone of each tweet has been calculated with a script that averaged on the sentiment of each (relevant) word, that being
obtained by matching tokenized words with the ones contained in the Sentix dictionary. The .csv with all the italian Maneskin tweets and their respective
emotional tone can be found in the maneskin_italian_clean_scored_tweets.zip file.

3. The modularity analysis
Semantic networks have been created for each week of Maneskin tweets, both italian and english. The nodes are the words, they include the number of times
the word has been used during the week in the count field. The edges link together words that appear in the same tweet, and their weight is how many times
that happens. For each network, many metrics have been extracted and a filtered version of it has been visualized with words of different colour based on
the modularity class (community) they belong to and word size depending on their eigenvector centrality. Filtering was needed in order to obtain a clean
representation, and the choice was to hide words used only once in the case of italian tweets, and hide words used less than 8 times for english tweets
because they were many more. All the extracted metrics + details on the procedure can be found in the Maneskin Semantic Network - Modularity Analysis.zip
file. The main outcome of this analysis was the following: it appears that starting from the 2nd week and especially during the 3rd one, people's opinion
aligned and grouped because more different words were used but less communities are found. Modularity metric confirms it. This effect was found both in
the english tweets and the italian tweets, disappearing pretty quickly in the 4th week. Further confirmation is needed by using the results of sentiment
analysis, we need to understand if this shift in people's thought was positive or negative.

4. The hashtags network
Since it's impossible to build a network of users because we would have no means to link them (we don't have full conversations between users since we
only gathered tweets containing certain keywords), we thought of extracting hashtags and see whether they were more used in "positive" tweets or "negative" 
tweets week by week. The procedure has been the following: hashtags have been extracted from each week and per each artist. Then, a score has been computed
for each hashtag by averaging on the emotional tones of the tweets it appears in during that week. Basically the output of this process is, for each
artist, a list of hashtags for each week. Every hashtag is written with a score that represents the average tone they have been associated to and the number
of times it appears.
IF this tone is more polarized towards negativity or positivity during the 2nd/3rd week (especially 3rd), we have proven our point for that artist, so an
alignment in opinion towards him has happened and these opinions are polarized. This needs to be investigated.
IF the tone is neutral, then one of two scenarios are happening: either the tweets are neutral, or the community is splitted on the topic.
The english scored hashtags for every artist can be found in the tags.zip file: (hashtag, tone, num of appearance).
The italian hashtags for Maneskin will be treated in the same way and uploaded in the italian_tags.zip file.

# WHAT NEEDS TO BE DONE
Everyone should perform some kind of analyis on the results or comparison between the effects on the considered artists. This is because we have to
send a quite lengthy report (just go look at the example of past reports on Moodle) and we need to talk 5 minutes each during the presentation.
Each one of us needs something to talk about, so I thought of some analysis ideas:
- Someone should replicate the modularity analysis I did on Maneskin tweets for the other 5 artists and see if the effect is common. (Alex?)
- Someone could make graphs out of Edo's hashtag analysis and study how these hashtags were used across the weeks (if more in a positive or 
negative way) to try and see if that matches the outcome of the modularity analysis like explained above. This should also be verified for italian
hashtags.

I also think that the above ideas can be carried out in groups of two people.

# NOTES
It's important to remember that LIWC result files don't contain all the tweets, but just the ones in english language. Whenever a metric has to be calculated
on the entire set of tweets related to an artist, the raw tweets contained in the "artistname.pkl" file in the "tweets" folder are the ones that should be 
used.

Also, I think that writing the report will be very time consuming. We need to start writing along with the final analyses otherwise we won't make it in time.
From what I've seen, a report of about 20 pages should do it. The longer the better though. But writing it and explaining the results will require the
construction of many diagrams/graphs/etc. so it will take time. We need to start working on it ASAP, if everyone contributes with a section about what they
did we can make it in time.
