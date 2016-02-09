# -*- coding: utf-8 -*-
#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import Cursor
from tweepy import API
import json
import pprint

#Variables that contains the user credentials to access Twitter API 
access_token = "4891415603-ZM8LKg9VjAqGxSIL4xo7jwbEbqkpyURDGl4UrOw"
access_token_secret = "0hCSgD6YrC3wajSVcJ4G0OGFbkEIb1TTUvCFKUNscKcQG"
consumer_key = "fUwv85bmP4B85Kry1ivTJwk1U"
consumer_secret = "SO0CUea567Jm9PSXeIp7c7lgGxBwFKUBPWrLCjpyaeEXRX2Hqu"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)


    api = API(auth)
    # for status in Cursor(api.home_timeline).items(30):
    #     print(status.text)
        #print(status.created_at)
        #print(status.screen_name)
    nickname = "Michael__Putnam"
    status = api.user_timeline(screen_name=nickname, count=10)
    tweetlist = []
    for items in status:
        tweet = {}
        tweet["date"] = str(items.created_at)
        tweet["text"] = items.text
        tweet["nickname"] = nickname
        tweetlist.append(tweet)

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(tweetlist)

    # print status.text
    # print status.text

    #stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    #stream.filter(track=['python', 'javascript', 'ruby'],follow=['575930104'] async=True)
    

    #stream.filter(follow=['575930104'], async=True)
    #stream.filter(follow=['BHaasGolf'])



