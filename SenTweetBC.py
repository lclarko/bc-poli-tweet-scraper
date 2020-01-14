

import twitter

# initialize api instance
twitter_api = twitter.Api(consumer_key='',
                        consumer_secret='',
                        access_token_key='',
                        access_token_secret='')

# test authentication
print(twitter_api.VerifyCredentials())