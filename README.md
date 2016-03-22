# golfjobb

### Requirements

* Pip
* Tweepy
# Golfjobb

## Features:
- Get list of 'golfkex' followers
- Get tweets from API with (not fully tested) error handling
- Score tweets
- Save tweets to file, dict on every line.
- Calculate avrage within timespan (calculate.py)

## ToDo:
- Get golfer statistics from PGA
- Statistics modules to calculate.py


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

## Running

```
To get tweets from twitter, takes a long time due to API constaints.
$ python twitter_mining.py

To save output

```
