import tweepy

def login(secrets):

    client = tweepy.Client(
        consumer_key=secrets['API_KEY'],
        consumer_secret=secrets['API_SECRET'],
        access_token=secrets['ACCESS_TOKEN'],
        access_token_secret=secrets['ACCESS_SECRET']
    )
    auth = tweepy.OAuth1UserHandler(
        consumer_key=secrets['API_KEY'],
        consumer_secret=secrets['API_SECRET'],
        access_token=secrets['ACCESS_TOKEN'],
        access_token_secret=secrets['ACCESS_SECRET']
    )
    api = tweepy.API(auth)
    return client, api
