#!/usr/bin/env python
# -*- encoding:utf-8 -*-

__author__ = 'ZACH'

from splinter import Browser
import datetime
import ConfigParser

MaxPrice = 0
MyPrice = 0

b = Browser('chrome')


def endStep():
    global MaxPrice
    global MyPrice
    while True:
        try:
            b.reload()
            sPrice = u'%s' % (b.find_by_id('cur_price').value,)
            print u'%s-->current price：%s' % (datetime.datetime.now().strftime("%H:%M:%S.%f"), sPrice)

            nPrice = int(sPrice[1:-3])

            if nPrice > MyPrice:
                MyPrice = nPrice + 1

                if MyPrice <= MaxPrice:
                    sPrice = str(MyPrice)

                    print u'i will give the price is: %s' % (sPrice,)

                    inputs = b.find_by_tag("input")
                    inputs[-2].fill(sPrice)
                    print u'submit my price'

                    b.find_by_id('buy-btn').click()
                else:
                    print u'current price is higher my max price, cancel ...'
                    break
        except:
            print u'except, but but continue go go go ...'


if __name__ == '__main__':
    print u'start ...'
    config = ConfigParser.ConfigParser()
    config.readfp(open('db.ini', 'rb'))
    code = config.get('global', 'code')
    b.visit('https://passport.jd.com/new/login.aspx?ReturnUrl=http://auction.jd.com/%s' % (code,))  # 请修改相应物品ID
    MaxPrice = int(raw_input(u'input your max price, then anykey continue:'))
    endStep()
    print u"over ..."