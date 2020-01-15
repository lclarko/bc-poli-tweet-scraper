#!/usr/bin/env python

import twitter
import pandas as pd

# initialize api instance
twitter_api = twitter.Api(consumer_key='',
                        consumer_secret='',
                        access_token_key='',
                        access_token_secret='')

# test authentication
#print(twitter_api.VerifyCredentials())

def buildTestSet(search_keyword):
    try:
        tweets_fetched = twitter_api.GetSearch(search_keyword, count = 100)

        print('Fetched ' + str(len(tweets_fetched)) + ' tweets for the term ' + search_keyword)

        return [{'text': status.text, 'label':None} for status in tweets_fetched]
    except:
        print('Something went wrong...')
        return None
search_term = input("Enter a search keyword:")
testDataSet = buildTestSet(search_term)

# Print 5 tweets (JSON)
print(testDataSet[0:4])