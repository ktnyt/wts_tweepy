#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
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

    current = datetime.now()
    deadline = datetime(2017, 1, 1, 0, 0, 0, 0)
    diff = deadline - current
    days = diff.days
    hours = diff.seconds / 3600 + days * 24

    text = '新年まであと%d日(%d時間)です。' % (days, hours)

    # ツイートを送信
    try:
        api.update_status(status=text)
    except tweepy.TweepError as e:
        print 'Error code %d: %s' %(e[0][0]['code'], e[0][0]['message'])
