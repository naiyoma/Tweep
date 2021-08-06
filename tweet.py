
import os
import tweepy
import pandas
from tweepy.auth import OAuthHandler

f

API_SECRET_KEY = "ZxXKs8gmfg6w61GIWkUhAfVV1HrI8S76oWbf6JMtk3jzJh9vRD"
API_KEY = "yNtiYh9eA99AzeDAvj3eg8QcQ"
# BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAABuURQEAAAAAXL4HCaEJyePzYh3o2M % 2BGESxXU
# sU % 3DCGFQJFo2YC91q356gh3AvmYAJhx61kwaqQO3mQJkTajwuYaOBi"
ACCESS_TOKEN = "1072560730451439616-owT3mm92S0Fc5sznvQ61i8WkmttWbB"
ACCESS_TOKEN_SECRET = "2plWVwJjnTq2FaxZzfSCCatBPmLeAVfxsRgthbAFVcA3w"

consumer_key = API_KEY
consumer_secret = API_SECRET_KEY
access_token = ACCESS_TOKEN
access_token_secret = ACCESS_TOKEN_SECRET
# search for tweets function


class UserListView(ListView):
    model = User

    def get_context_data(self, **kwargs):

        context = super(UserListView, self).get_context_data(**kwargs)
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth, wait_on_rate_limit=True)
        last_tweet_id = False
        page_num = 1
        query = "BTC"
        data = get_df()
        cypto_query = f"#{query}"
        print(" ===== ", query, cypto_query)
        for page in tweepy.Cursor(
            self.api.search,
            q=cypto_query,
            lang="en",
            tweet_mode="extended",
            count=200,
        ).pages():
            print(" ...... new page", page_num)
            page_num += 1

            for item in page:
                mined = {
                    "tweet_id": item.id,
                    "name": item.user.name,
                    "screen_name": item.user.screen_name,
                    "retweet_count": item.retweet_count,
                    "text": item.full_text,
                    "mined_at": datetime.datetime.now(),
                    "created_at": item.created_at,
                    "favourite_count": item.favorite_count,
                    "hashtags": item.entities["hashtags"],
                    "status_count": item.user.statuses_count,
                    "followers_count": item.user.followers_count,
                    "location": item.place,
                    "source_device": item.source,
                }

                try:
                    mined["retweet_text"] = item.retweeted_status.full_text
                except:
                    mined["retweet_text"] = "None"

                last_tweet_id = item.id
                data = data.append(mined, ignore_index=True)

            if page_num % 180 == 0:
                date_label = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                print("....... outputting to csv", page_num, len(data))
                data.to_csv(
                    f"{query}_{page_num}_{date_label}.csv", index=False)
                print("  ..... resetting df")
                data = get_df()

        date_label = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        data.to_csv(f"{query}_{page_num}_{date_label}.csv", index=False)
        context['tweet_tweet_location'] = df.to_dict()['col1'][0]

        context = "test user_data"

        return context

    template_name = 'home.html'

    # search for Ethereum per minute

    tweets = tweepy.Cursor(
        api.search,
        q="#Ethereum",
        lang="en",
        start_time=start_time,
        end_time=end_time,
        tweet_mode="extended").items(100)
    all_tweets_et = [tweet.created_at.minute for tweet in tweets]
    current_time = datetime.datetime.now().minute
    filtered_tweets_et = [x for x in all_tweets_et if x == current_time
                          or x == current_time - 1]

    # search for #Litecoin per  minute
    tweets = tweepy.Cursor(
        api.search,
        q="#Litecoin",
        lang="en",
        start_time=start_time,
        end_time=end_time,
        tweet_mode="extended").items(100)
    all_tweets_lt = [tweet.created_at.minute for tweet in tweets]
    current_time = datetime.datetime.now().minute
    filtered_tweets_lt = [x for x in all_tweets_lt if x == current_time
                          or x == current_time - 1]

    # Search #XRP per minute and create a tweepy filter
    tweets = tweepy.Cursor(
        api.search,
        q="#XRP",
        lang="en",
        start_time=start_time,
        end_time=end_time,
        tweet_mode="extended").items(100)
    all_tweets_bt = [tweet.created_at.minute for tweet in tweets]
    current_time = datetime.datetime.now().minute
    filtered_tweets_bt = [x for x in all_tweets_bt if x == current_time
                          or x == current_time - 1]

    # Search for #DogeCoin per minute
    tweets = tweepy.Cursor(
        api.search,
        q="#DogeCoin",
        lang="en",
        start_time=start_time,
        end_time=end_time,
        tweet_mode="extended").items(100)
    all_tweets_dg = [tweet.created_at.minute for tweet in tweets]
    current_time = datetime.datetime.now().minute
    filtered_tweets_dg = [x for x in all_tweets_dg if x == current_time
                          or x == current_time - 1]
