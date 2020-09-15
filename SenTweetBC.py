#!/usr/bin/python

# Daily BC Politics Tweet Scraper
# See crontab -l for job time

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

csvFile = open('bcpoli.csv', 'a') # Create/Open a file to append data to
csvWriter = csv.writer(csvFile)
ystd = (datetime.date.today() - datetime.timedelta(days=1))
today = (datetime.date.today())

# Search for any hashtag by modifying q="#TERM"

for tweet in tweepy.Cursor(api.search,q="#bcpoli",count=100,
                           lang="en",
                           since=ystd,
                           until=today).items(): # Pulls all tweets from previous day
    print (tweet.id, tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.id, tweet.created_at, tweet.text.encode('utf-8')])