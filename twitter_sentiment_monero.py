# -*- coding: utf-8 -*-
"""
Created on Wed Jun 07 00:52:37 2017

@author: abc
"""

import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key= 'iq6BHYjneyvtFT7qtg50YQA4I'
consumer_secret= 'PwedTBrtKr05iX0JKmc57Tulf4MLVZP4zuRK0fz4t4jtGpEqU5'

access_token='2656380056-fkTeAlckTwGO9vtrfsYVigZeWkcrJrQOp4Zo3e7'
access_token_secret= 'bGy1daJfDplHT7Qdiw8AH4l3mOpRtJ62iAfOg3kgMPcIU'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('Monero')




for tweet in public_tweets:
    print(tweet.text)
    
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")