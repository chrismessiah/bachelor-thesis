# Predict golfer performance using sentiment analysis on Twitter

Authors: *Christian Abdelmassih* & *Axel Hultman*

This repo contains the software used in bachelor thesis submitted at KTH, Royal Institute of Technology (yet to be published). The repo contains the following programs

*  `make_golferstats2015.py` used to parse stats in HTML-files into objects
*  `make_golferstats2016.py` as above 
*  `twitter_mining.py` used to mine the 1000 latest tweets from the verified golfers' accounts.
*  `construct_datapairs.py` used to construct datapairs of mean AFINN score and relative player-performance to be later used in the regression model.

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
