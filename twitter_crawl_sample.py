#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
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

    parser = argparse.ArgumentParser(description='あるscreenameのユーザのツイートをmax_count件取得する')
    parser.add_argument('user', type=str, help='Twitterのscreenname')
    parser.add_argument('max_count', type=int, help='取得する件数')

    args = parser.parse_args()
    user = args.user
    max_count = args.max_count

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
            print '{}\t{}\t{}\t{}'.format(N, tweet.id, tweet.created_at, byte_text)
            N += 1
            total += 1
            if total >= max_count:
                break

        if prev == total:
            break
