#!/usr/bin/env python
# -*- coding: utf-8 -*-
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

    # Mentionの取得
    # 自分宛てのツイートを取得して表示
    mentions = api.mentions_timeline(count=10)
    for tweet in mentions:
        byte_text = tweet.text.encode('utf-8')
        user = tweet.user
        screen_name = user.screen_name
        print '{}: {}'.format(byte_text, screen_name)

    # ツイートを送信
    try:
        api.update_status(status='Hello, world!')
    except tweepy.TweepError as e:
        print 'Error code {}: {}'.format(e[0][0]['code'], e[0][0]['message'])
