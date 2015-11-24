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
    count = 3
    print '[ Mentions Timeline (あなた宛のツイート) : 最新 {} 件 ]'.format(count)
    timeline = api.mentions_timeline(count=count)
    for tweet in timeline:
        print '--'
        print '発 言 者:\t{}'.format(tweet.user.screen_name)
        print '本 　 文:\t{}'.format(tweet.text.encode('utf-8'))
        print 'MssageId:\t{}'.format(tweet.id)
        print '発言時間:\t{}'.format(tweet.created_at)

    # Timelineの取得 (1)
    # 自分がフォロー関係のツイートを取得する
    print '[ Home Timeline : 最新 {} 件 ]'.format(count)
    timeline = api.home_timeline(count=count)
    for tweet in timeline:
        print '--'
        print '発 言 者:\t{}'.format(tweet.user.screen_name)
        print '本 　 文:\t{}'.format(tweet.text.encode('utf-8'))
        print 'MssageId:\t{}'.format(tweet.id)
        print '発言時間:\t{}'.format(tweet.created_at)

    # Timelineの取得 (2)
    # 特定の「ある人」のツイートだけを取得する
    screen_name = 'kotone_nyt'
    print '[ {} さん のツイート : 最新 {} 件 ]'.format(screen_name, count)
    timeline = api.user_timeline(screen_name=screen_name, count=count)
    for tweet in timeline:
        print '--'
        print '発 言 者:\t{}'.format(tweet.user.screen_name)
        print '本 　 文:\t{}'.format(tweet.text.encode('utf-8'))
        print 'MssageId:\t{}'.format(tweet.id)
        print '発言時間:\t{}'.format(tweet.created_at)

    # ツイートを送信
    text = 'Hello, world!'
    try:
        api.update_status(status=text)
        print '[以下の内容でツイートしました]'
        print text
    except tweepy.TweepError as e:
        print '[Updateに失敗しました]'
        print 'Error code {}: {}'.format(e[0][0]['code'], e[0][0]['message'])

    # リプライを送信
    user = 'wts12_official'
    text = '@{} リプライのテスト'.format(user)
    try:
        api.update_status(status=text)
        print '[以下の内容でリプライしました]'
        print text
    except tweepy.TweepError as e:
        print '[Updateに失敗しました]'
        print 'Error code {}: {}'.format(e[0][0]['code'], e[0][0]['message'])
