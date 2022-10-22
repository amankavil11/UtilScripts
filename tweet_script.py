import tweepy

# Authenticate to Twitter
CONSUMER_KEY = "adG5l4IPcUWD4BY80s1sJDmvt"
CONSUMER_SECRET = "FNEYeWi8pELaYFIQYliBGYDDguulsnmMeXUfhire6K4HpEMZ8S"
ACCESS_TOKEN = "986064704824070145-albpFWqIv4Y8mzFIJ9jymTJnNQhvXVL"
ACCESS_TOKEN_SECRET = "liWVJE5Esm6d64hb0BBxfRVVKXDifzqYmiYQsFdengQqG"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAALibegEAAAAA1CmbWfiEBzKMEnN5YFqC%2F066veI%3D5dy40wNAvMuWN1Pk6YVbfH8uGKekrJdFmoW3AAIMPVc6w6w7ra"


import tweepy
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