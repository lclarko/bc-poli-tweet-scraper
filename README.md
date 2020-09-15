# BC Politics Tweet Scraper 

## Summary

* A python script that utilizes [Tweepy](http://docs.tweepy.org/en/latest/) to scrap #bcpoli tweets from the previous day.
* The script can be easily modified to pull tweets relating to any string, just change -> ```q="#bcpoli"```
* By default, the csv file this script generates will be in the same directory as the script. You can modify the ```csvFile``` variable to change this.

## Requirements
* You must have Twitter API keys.
    * A [Twitter Developer account](https://developer.twitter.com/en/apply-for-access) and an approved application is the easiest way to obtain these.
* It's a good idea to review the [restricted uses of the Twitter APIs](https://developer.twitter.com/en/developer-terms/more-on-restricted-use-cases), as there are many terms that you have to accept, especially if you plan on redistributing any twitter data.