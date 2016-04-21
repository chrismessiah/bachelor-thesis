# -*- coding: utf-8 -*-
from afinn.afinn import Afinn
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import Cursor
from tweepy import API
from tweepy import RateLimitError
from tweepy import TweepError
from datetime import datetime
from tqdm import tqdm
import time
import json
import pprint
import logging
logging.captureWarnings(True)
#load Afinn
afinn = Afinn()
# Amount of tweets to fetch
amont_of_tweets = 1000

# User to fetch tweets from
#nickname = "Michael__Putnam"

#Variables that contains the user credentials to access Twitter API
access_token = "4891415603-ZM8LKg9VjAqGxSIL4xo7jwbEbqkpyURDGl4UrOw"
access_token_secret = "0hCSgD6YrC3wajSVcJ4G0OGFbkEIb1TTUvCFKUNscKcQG"
consumer_key = "fUwv85bmP4B85Kry1ivTJwk1U"
consumer_secret = "SO0CUea567Jm9PSXeIp7c7lgGxBwFKUBPWrLCjpyaeEXRX2Hqu"

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)

def get_tweets(tweeter_id, from_id = None):
    #Setup
    #l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = API(auth)

    #Get tweets (status) from Twitter A
    if from_id == None:
        status = api.user_timeline(user_id = tweeter_id, count=amont_of_tweets)
    else:
        status = api.user_timeline(user_id = tweeter_id, count=amont_of_tweets, max_id = from_id)
        status.pop(0) #Remove duplicate first tweet, max_id not included.

    tweetlist = []
    last_id = 0

    #print("Cleaning tweets from :", status.user.screen_name, "id: ", tweeter_id)
    for items in status:
        tweet = {}
        tweet["id"] = items.id
        tweet["user_id"] = tweeter_id
        tweet["nickname"] = items.user.screen_name
        tweet["realname"] = items.user.name
        tweet["date"] = datetime.strptime(str(items.created_at), "%Y-%m-%d %H:%M:%S")
        tweet["text"] = items.text

        tweetlist.append(tweet)
        last_id = items.id

    print("Last ID: ", last_id, "\n")
    return tweetlist, last_id

def score_tweets(tweets):
    ratings = []
    for row in tweets:
        tweetscore = afinn.score(row["text"])
        row["score"] = tweetscore
        ratings.append(tweetscore)

        #print(row["nickname"], row["date"], "\n", row["text"], tweetscore)
        #print("\n")

    #print(sum(ratings) / len(ratings))

    return tweets

def wait_fifteen():
    print("RateLimitError, waiting for 16 minutes and trying again")
    for i in range(1,17):
        time.sleep(60) #Wait 15 minutes and try again (should this be shorter?)
        print(i, " minutes waited")
    print("Retrying!")

def run(tweeter_id, output_filename):
    """Gets two rounds of twitter user_ids, should be changed so it runs until
    selected date is hit (if available) """
    print("Getting tweets for ID: ", tweeter_id)
    last_id = None
    alltweets = []
    for i in xrange(5):
        try:
            if last_id == None:
                tweets, last_id = get_tweets(tweeter_id) # Get tweets via twitter API
            elif last_id == 0 or i == 4:
                output_tweets(alltweets, output_filename)
                break
            else:
                tweets, last_id = get_tweets(tweeter_id, last_id)
            result = score_tweets(tweets)
            print("Request" + str(i) + " ", len(tweets))
            alltweets = alltweets + result

        except RateLimitError:
            wait_fifteen()
            if last_id == None:
                tweets, last_id = get_tweets(tweeter_id) # Get tweets via twitter API
            elif last_id == 0 or i == 4:
                output_tweets(alltweets, output_filename)
                break
            else:
                tweets, last_id = get_tweets(tweeter_id, last_id)
            result = score_tweets(tweets)
            print("Request" + str(i) + " ", len(tweets))
            alltweets = alltweets + result
            #run(tweeter_id)

        except IndexError:
            print("IndexError")
            return None

def output_tweets(alltweets, output_filename):
    with open(output_filename, "a") as f:
        for items in alltweets:
            f.write(str(items))
            f.write("\n")

def get_golfers():
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = API(auth)

    #golfers = api.friends_ids(screen_name = "golfjobb")
    golfers = [43334612,
    224395974,
    365659638,
    608085042,
    832245307,
    1406435672,
    2575022059,
    2586530467,
    2795249566,
    15668931,
    31630805,
    32453930,
    55247998,
    62130152,
    103691667,
    119754291,
    155858930,
    171065186,
    174596509,
    179205995,
    184995243,
    212795923,
    235180756,
    284814482,
    300011126,
    317245257,
    373511205,
    382202772,
    386007220,
    404865489,
    431158121,
    431333874,
    538169429,
    558220594,
    603055123,
    819954614,
    842960749,
    995830002,
    1138456724,
    1152096636,
    1152776161,
    1308077142,
    1493901511,
    1553899147,
    1596541134,
    1924882021,
    2253890264,
    2271120397,
    2575555092,
    2790755710,
    2852157224,
    2856052017,
    3028563436
    ]


    #with open("golferID.txt", "w") as f:
    #    for items in golfers:
    #        f.write(str(items))
    #        f.write("\n")

    print("GOlfers: ", golfers)
    return golfers

if __name__ == '__main__':
    output_filename = "output2.txt"
    error_filename = "errors2.txt"
    golfers = get_golfers()
    for golfer_id in tqdm(golfers):
        try:
            run(golfer_id, output_filename)
        except TweepError:
            with open(error_filename, "a") as f:
                f.write("TweepError detected when processing: " +  str(golfer_id))
                f.write("\n")
