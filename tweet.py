
import os
import tweepy
import pandas
from tweepy.auth import OAuthHandler


consumer_key = API_KEY
consumer_secret = API_SECRET_KEY
access_token = ACCESS_TOKEN
access_token_secret = ACCESS_TOKEN_SECRET
# search for tweets function


def search_tweet():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    username = 'jack'
    count = 150
    try:
        # Creation of query method using parameters
        import pdb
        pdb.set_trace()
        tweets = tweepy.Cursor(api.user_timeline, id=username).items(count)

        # Pulling information from tweets iterable object
        tweets_list = [[tweet.created_at, tweet.id, tweet.text]
                       for tweet in tweets]

        # Creation of dataframe from tweets list
        # Add or remove columns as you remove tweet information
        tweets_df = pandas.DataFrame(tweets_list)
    except BaseException as e:
        print('failed on_status,', str(e))
        time.sleep(3)
