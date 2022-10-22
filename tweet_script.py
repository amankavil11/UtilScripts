import tweepy
from decouple import config

# Authenticate to Twitter
CONSUMER_KEY = config('CONSUMER_KEY')
CONSUMER_SECRET = config('CONSUMER_SECRET')
ACCESS_TOKEN = config('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = config('ACCESS_TOKEN_SECRET')
BEARER_TOKEN = config('BEARER_TOKEN')

client = tweepy.Client(bearer_token= BEARER_TOKEN, consumer_key=CONSUMER_KEY,
                       consumer_secret=CONSUMER_SECRET,
                       access_token=ACCESS_TOKEN,
                       access_token_secret=ACCESS_TOKEN_SECRET)
# Create a tweet

def get_userid(screename):
    user_dict = client.get_user(username=screename)
    return user_dict.data.id

#Need user_auth=True to authenticate user ID for OAuth 2.0
#includes retweets
def get_recent_tweets(screename):
    response = client.get_users_tweets(get_userid(screename), user_auth=True)
    tweets_list = []
    for tweet in response.data:
        tweets_list.append(tweet.text)
    return tweets_list

def tweet(message):
    client.create_tweet(text=message)