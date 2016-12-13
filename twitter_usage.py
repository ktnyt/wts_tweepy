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
    count = 3
    print '[ Mentions Timeline (あなた宛のツイート) : 最新 %d 件 ]' % (count)
    timeline = api.mentions_timeline(count=count)
    for tweet in timeline:
        print '--'
        print '発 言 者:\t%s' % (tweet.user.screen_name.encode('utf-8'))
        print '本 　 文:\t%s' % (tweet.text.encode('utf-8'))
        print 'MssageId:\t%s' % (tweet.id)
        print '発言時間:\t%s' % (tweet.created_at)

    # Timelineの取得 (1)
    # 自分がフォロー関係のツイートを取得する
    print '[ Home Timeline : 最新 {0} 件 ]'.format(count)
    timeline = api.home_timeline(count=count)
    for tweet in timeline:
        print '--'
        print '発 言 者:\t%s' % (tweet.user.screen_name.encode('utf-8'))
        print '本 　 文:\t%s' % (tweet.text.encode('utf-8'))
        print 'MssageId:\t%s' % (tweet.id)
        print '発言時間:\t%s' % (tweet.created_at)

    # Timelineの取得 (2)
    # 特定の「ある人」のツイートだけを取得する
    screen_name = 'kotone_nyt'
    print '[ {0} さん のツイート : 最新 {1} 件 ]'.format(screen_name, count)
    timeline = api.user_timeline(screen_name=screen_name, count=count)
    for tweet in timeline:
        print '--'
        print '発 言 者:\t%s' % (tweet.user.screen_name.encode('utf-8'))
        print '本 　 文:\t%s' % (tweet.text.encode('utf-8'))
        print 'MssageId:\t%s' % (tweet.id)
        print '発言時間:\t%s' % (tweet.created_at)

    # ツイートを送信
    text = 'Hello, world!'
    try:
        api.update_status(status=text)
        print '[以下の内容でツイートしました]'
        print text
    except tweepy.TweepError as e:
        print '[Updateに失敗しました]'
        print 'Error code %d: %s' % (e[0][0]['code'], e[0][0]['message'])

    # リプライを送信
    user = 'wts12_official'
    text = '@{0} リプライのテスト'.format(user)
    try:
        api.update_status(status=text)
        print '[以下の内容でリプライしました]'
        print text
    except tweepy.TweepError as e:
        print '[Updateに失敗しました]'
        print 'Error code %d: %s' % (e[0][0]['code'], e[0][0]['message'])
