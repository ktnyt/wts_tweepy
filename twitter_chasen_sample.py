#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import system
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

    # 自分のタイムラインを取得
    timeline = api.home_timeline(count=10)
    fout = open('output.txt', 'w')
    for tweet in timeline:
        byte_text = tweet.text.encode('utf-8')
        print byte_text
        fout.write('{}\n'.format(byte_text))
    fout.close()

    # 外部コマンドの実行には `os.system()` を使う
    # ここでは `from os import system` を宣言済み
    system('chasen < output.txt > output.txt.chasen')

    data = {}

    fin = open('output.txt.chasen', 'r')
    for line in fin.readlines():
        if line.find('EOS') == 0:
            pass
        else:
            tmp = line.strip().split("\t")
            if tmp[3].find('名詞') == 0:
                if not word in data:
                    data[word] = 0
                data[word] += 1
    fin.close()

    for item in sorted(data.items(), key=lambda x:x[1], reverse=True):
        print '{}\t{}'.format(item[0], item[1])
