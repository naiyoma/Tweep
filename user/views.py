
import os
import tweepy
import pandas as pd

# from datetime import datetime, timedelta
import datetime

from tweepy.auth import OAuthHandler

from django.views.generic import ListView, DetailView
from .models import User

# Create your views here.

consumer_key = "yNtiYh9eA99AzeDAvj3eg8QcQ"
consumer_secret = "ZxXKs8gmfg6w61GIWkUhAfVV1HrI8S76oWbf6JMtk3jzJh9vRD"
access_token = "1072560730451439616-owT3mm92S0Fc5sznvQ61i8WkmttWbB"
access_token_secret = "2plWVwJjnTq2FaxZzfSCCatBPmLeAVfxsRgthbAFVcA3w"


class UserListView(ListView):
    model = User

    def get_context_data(self, **kwargs):

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth, wait_on_rate_limit=True)
        context = super(UserListView, self).get_context_data(**kwargs)
        # 1.get end time as the current time
        end_time = datetime.datetime.now().replace(microsecond=0)
        start_time = (datetime.datetime.now().replace(
            microsecond=0) - datetime.timedelta(minutes=1))
        current_time = datetime.datetime.now().minute

        # search for #Cardano per minute
        tweets = tweepy.Cursor(
            api.search,
            q="#Cardano",
            lang="en",
            start_time=start_time,
            end_time=end_time,
            tweet_mode="extended").items(10)

        et_tweets_dict = {}
        for tweet in tweets:
            et_tweets_dict[str(tweet.id)] = tweet.created_at.minute

        for key, value in dict(et_tweets_dict).items():
            if value < current_time - 2:
                del et_tweets_dict[key]
        ca_number = list(et_tweets_dict.values())

        ca_favorite_count = []
        ca_retweets_count = []
        interactions_ca = sum(ca_favorite_count + ca_retweets_count)

        for key, value in dict(et_tweets_dict).items():
            try:
                tweet = api.get_status(key)
                ca_favorite_count.append(tweet.favorite_count)
                ca_retweets_count.append(tweet.retweet_count)
            except:
                pass

        context['ca_num'] = len(ca_number)
        context["ca_interactions"] = interactions_ca

        # search for #XRP per minute
        tweets = tweepy.Cursor(
            api.search,
            q="#XRP",
            lang="en",
            start_time=start_time,
            end_time=end_time,
            tweet_mode="extended").items(10)

        xrp_all_tweets_dict = {}
        for tweet in tweets:
            xrp_all_tweets_dict[str(tweet.id)] = tweet.created_at.minute

        for key, value in dict(xrp_all_tweets_dict).items():
            if value < current_time - 2:
                del xrp_all_tweets_dict[key]
        xrp_number = list(xrp_all_tweets_dict.values())

        xrp_favorite_count = []
        xrp_retweets_count = []
        interactions_xrp = sum(xrp_favorite_count + xrp_retweets_count)

        for key, value in dict(xrp_all_tweets_dict).items():
            try:
                tweet = api.get_status(key)
                xrp_favorite_count.append(tweet.favorite_count)
                xrp_retweets_count.append(tweet.retweet_count)
            except:
                pass

        context['xrp_num'] = len(xrp_number)
        context["xrp_interactions"] = interactions_xrp

        # search for #Litecoin per minute
        tweets = tweepy.Cursor(
            api.search,
            q="#Litecoin",
            lang="en",
            start_time=start_time,
            end_time=end_time,
            tweet_mode="extended").items(10)

        lt_all_tweets_dict = {}
        for tweet in tweets:
            lt_all_tweets_dict[str(tweet.id)] = tweet.created_at.minute

        for key, value in dict(lt_all_tweets_dict).items():
            if value < current_time - 2:
                del lt_all_tweets_dict[key]
        lt_number = list(lt_all_tweets_dict.values())

        lt_favorite_count = []
        lt_retweets_count = []
        interactions_lt = sum(lt_favorite_count + lt_retweets_count)

        for key, value in dict(lt_all_tweets_dict).items():
            try:
                tweet = api.get_status(key)
                lt_favorite_count.append(tweet.favorite_count)
                lt_retweets_count.append(tweet.retweet_count)
            except:
                pass

        context['lt_num'] = len(lt_number)
        context["lt_interactions"] = interactions_lt

        # search for #DogeCoin per minute
        tweets = tweepy.Cursor(
            api.search,
            q="#DogeCoin",
            lang="en",
            start_time=start_time,
            end_time=end_time,
            tweet_mode="extended").items(10)

        dg_all_tweets_dict = {}
        for tweet in tweets:
            dg_all_tweets_dict[str(tweet.id)] = tweet.created_at.minute

        for key, value in dict(dg_all_tweets_dict).items():
            if value < current_time - 2:
                del dg_all_tweets_dict[key]
        dg_number = list(dg_all_tweets_dict.values())

        dg_favorite_count = []
        dg_retweets_count = []
        interactions_dg = sum(dg_favorite_count + dg_retweets_count)

        for key, value in dict(dg_all_tweets_dict).items():
            try:
                tweet = api.get_status(key)
                dg_favorite_count.append(tweet.favorite_count)
                dg_retweets_count.append(tweet.retweet_count)
            except:
                pass

        context['dg_num'] = len(dg_number)
        context["dg_interactions"] = interactions_dg

        # search for ##Ethereum per minute.
        tweets = tweepy.Cursor(
            api.search,
            q="#Ethereum",
            lang="en",
            start_time=start_time,
            end_time=end_time,
            tweet_mode="extended").items(50)

        current_time = datetime.datetime.now().minute

        et_all_tweets_dict = {}
        for tweet in tweets:
            et_all_tweets_dict[str(tweet.id)] = tweet.created_at.minute

        for key, value in dict(et_all_tweets_dict).items():
            if value < current_time - 2:
                del et_all_tweets_dict[key]
        et_number = list(et_all_tweets_dict.values())

        et_favorite_count = []
        et_retweets_count = []
        interactions_et = sum(et_favorite_count + et_retweets_count)

        for key, value in dict(et_all_tweets_dict).items():
            try:
                tweet = api.get_status(key)
                et_favorite_count.append(tweet.favorite_count)
                et_retweets_count.append(tweet.retweet_count)
            except:
                pass

        context['et_num'] = len(et_number)
        context["et_interactions"] = interactions_et

        return context

    template_name = 'home.html'


class UserDetailView(DetailView):
    model = User
    template_name = 'detail.html'
