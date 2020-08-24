#!/usr/bin/python

# Daily BC Politics Tweet Scraper
# Cron Job scheduled nightly at 00:00
# e.g. 0 0 * * * $(which python3) /path/to/script.py

import os
import datetime
import twitter
import tweepy
import csv
from tweepy.auth import OAuthHandler

# Twitter API Keys & Authentication Method
# Your API keys should be environment variables
# e.g. export TWITTER_CONSUMER_KEY='YOUR_KEY'

consumer_key = os.environ.get("TWITTER_CONSUMER_KEY")
consumer_secret = os.environ.get("TWITTER_CONSUMER_SECRET")
access_token = os.environ.get("TWITTER_ACCESS_TOKEN")
access_token_secret = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
auth.set_access_token(access_token, access_token_secret)

# Other Variables

csvFile = open('bcpoli.csv', 'a') 
csvWriter = csv.writer(csvFile)
date = (datetime.date.today() - datetime.timedelta(days=1)) 

for tweet in tweepy.Cursor(api.search,q="#bcpoli",count=100,
                           lang="en",
                           since=date).items(): # Pulls all bcpoli tweets from previous day
    print (tweet.id, tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.id, tweet.created_at, tweet.text.encode('utf-8')])