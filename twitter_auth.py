#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy
import sys

if __name__ == '__main__':
    consumer_key    = ''
    consumer_secret = ''

    # Twitter OAuth
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.secure = True
    redirect_url = auth.get_authorization_url()
    print '%s' % (redirect_url)
    verifier = raw_input('Token: ')
    access_token, access_token_secret = auth.get_access_token(verifier)
    print 'Access Token:        %s' % (access_token)
    print 'Access Token Secret: %s' % (access_token_secret)
    fh = open('tokens', 'w')
    fh.write('%s\t%s' % (access_token, access_token_secret))
    fh.close()
