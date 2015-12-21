#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
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

    user = sys.argv[1]
    max_count = int(sys.argv[2])

    total = 0
    prev = -1
    max_id = 0
    count = 200
    N = 1

    while total < max_count:
        tweets = []

        if max_id == 0:
            tweets = api.user_timeline(count=count, screen_name=user)
        else:
            tweets = api.user_timeline(count=count, screen_name=user, max_id=max_id-1)

        prev = total

        for tweet in tweets:
            byte_text =  tweet.text.encode('utf_8')
            print '{0}\t{1}\t{2}\t{3}'.format(N, tweet.id, tweet.created_at, byte_text)
            N += 1
            total += 1
            if total >= max_count:
                break

        if prev == total:
            break
