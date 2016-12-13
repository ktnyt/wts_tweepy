#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os.path import isfile
import fcntl
from fcntl import flock
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

    data = []

    if isfile('log.txt'):
        f = open('log.txt', 'r')
        flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
        for line in f.readlines():
            data.append(line.strip())
        flock(f, fcntl.LOCK_UN)
        f.close()
    else:
        print 'Warning: log.txt not found'

    mentions = api.mentions_timeline(count=10)
    for tweet in mentions:
        if not tweet.id in data:
            try:
                api.update_status(
                    status='@%s Hello!' % (tweet.user.screen_name),
                    in_reply_to_status_id=tweet.id
                )
                data.append(tweet.id)
            except tweepy.TweepError as e:
                print 'Error code %d: %s' % (e[0][0]['code'], e[0][0]['message'])
        break

    f = open('log.txt', 'w')
    flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
    for item in data:
        f.write('%s\n' % (item))
    flock(f, fcntl.LOCK_UN)
    f.close()
