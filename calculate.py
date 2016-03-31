# -*- coding: utf-8 -*-
import datetime 

def get_tweets_from_file(filename):
	with open(filename, "r") as f:
		tweet = f.readlines()

	tweet_objects = []
	for items in tweet:
		tweet_objects.append(eval(items))

	return tweet_objects

def tweet_interval_avg(dateObj, num_days, tweet_objects):
    """Takes a datetime object, an int and a list of tweetobjecs and returns the average score
    for tweets within that span. 

    Example dateOjb: dateObj = datetime.datetime.strptime("2015-06-01 00:00:00", "%Y-%m-%d %H:%M:%S") """

    span = datetime.timedelta(days= num_days).total_seconds()
    print("SPAN: ", datetime.timedelta(days= num_days), 
        "Seconds:", datetime.timedelta(days= num_days).total_seconds())

    total_score = 0
    hits = 0
    for items in tweet_objects:
        #print((items["date"] - dateObj))
        if (abs(items["date"] - dateObj).total_seconds()) < span:
            print("Hit within span, score: ", items["score"])
            total_score += items["score"]
            hits += 1

    return total_score / hits

def tweets_per_golfer(tweets):
    golf_list = []
    for tweet in tweets:
        golfers = {}
        if tweet["realname"] not in golfers:
            golfers[ tweet["realname"] ] = 1
        else:
            golfers[ tweet["realname"] ] += 1

        golfers["oldest"] = tweet["date"]
        golf_list.append(golfers)
    return golf_list

if __name__ == '__main__':
    tweets = get_tweets_from_file("golfersRun27mars.txt")
    avg = tweet_interval_avg(datetime.datetime.strptime("2015-06-01" ,"%Y-%m-%d"), 5, tweets)
    #print("Average within 5 days from 2016-06-01: ", avg)
    print(tweets_per_golfer(tweets))