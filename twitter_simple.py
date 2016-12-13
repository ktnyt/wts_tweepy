#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy

if __name__ == '__main__':
    consumer_key        = 'jXCJDViYGtDQ5bEUvPZmHQ'
    consumer_secret     = 'xexlwpVcNLSWvNwSGg0trbLfQj0NzHebh0X4q0CTs'
    access_token        = '167358179-aGv42HeElgPcwhJruFVLGGm2sXNaZwucR27bw6cT'
    access_token_secret = 'r412L37AIw7WIo3wHRsgzN6tKlKR6C02ruJD5E0Q7aERa'

    # Twitter OAuth
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.secure = True
    auth.set_access_token(access_token, access_token_secret)

    # Twitter API
    api = tweepy.API(auth)

    # Mentionの取得
    # 自分宛てのツイートを取得して表示
    mentions = api.mentions_timeline(count=10)
    for tweet in mentions:
        byte_text = tweet.text.encode('utf-8')
        user = tweet.user
        screen_name = user.screen_name.encode('utf-8')
        print '%s: %s' % (byte_text, screen_name)

    # ツイートを送信
    try:
        api.update_status(status='Hello, world!')
    except tweepy.TweepError as e:
        print 'Error code %d: %s' % (e[0][0]['code'], e[0][0]['message'])
