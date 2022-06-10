import os

import requests
import tweepy
from dotenv import load_dotenv
from loguru import logger

load_dotenv()

consumer_key = os.environ.get("API_KEY")
consumer_secret = os.environ.get("API_KEY_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
)

wiki_random_url = "https://en.wikipedia.org/wiki/Special:Random"


def tweet_random_article(client: tweepy.Client):

    response = requests.get(wiki_random_url)
    article_url = response.url
    response = client.create_tweet(text=article_url, user_auth=True)
    logger.info(response)


tweet_random_article(client)
