#!/usr/bin/python

# Daily BC Politics Tweet Scraper
# See crontab -l for job time

import os
import datetime
import twitter
import tweepy
import csv
from tweepy.auth import OAuthHandler

# Twitter API Keys / Authentication Method

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
                           since=date).items():
    print (tweet.id, tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.id, tweet.created_at, tweet.text.encode('utf-8')])

# To run on headless pi, via SSH that won't terminate the script on hangup
# screen -S bcpoli -dm bash -c 'python ./bcpoli.py'
