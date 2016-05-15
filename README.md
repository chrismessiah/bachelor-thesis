# Predict golfer statistics using sentiment analysis on Twitter

Authors: *Christian Abdelmassih* & *Axel Hultman*

This repo contains the written software used in our bachelor thesis (to be published). It contains the four programs which we wrote to our study. These are

*  make_golferstats2015.py and make_golferstats2016.py
*  twitter_mining.py
*  construct_datapairs.py

## Features:
- Get tweets using Tweepy API with error handling

- Calculate relative or absolute sentiment-score of tweets for a golfer and competition

- Calculate performance-score of a golfer and competition

## Requirements

- Pip
- Tweepy

## Installation
```
$ sudo easy_install pip
$ pip install -r requirements.txt
$ git clone git://github.com/tweepy/tweepy.git
$ git clone https://github.com/fnielsen/afinn.git
$ touch afinn/__init__.py
$ cd tweepy
$ sudo python setup.py install
```
