#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import choice
import tweepy

if __name__ == '__main__':
    consumer_key        = ''
    consumer_secret     = ''
    access_token        = ''
    access_token_secret = ''

    # Twitter OAuth
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.secure = True
    auth.set_access_token(access_token, access_token_secret)

    # Twitter API
    api = tweepy.API(auth)

    f = open('meigen.txt', 'r')
    meigen = list(f.readlines())
    f.close()

    text = choice(meigen)

    # ツイートを送信
    try:
        api.update_status(status=text)
    except tweepy.TweepError as e:
        print 'Error code %d: %s' % (e[0][0]['code'], e[0][0]['message'])
