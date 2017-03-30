#coding:utf-8
import bs4
import itertools
from time import sleep
import pymysql
import urllib2
import basefunc
from bs4 import BeautifulSoup
import threading

#判断一个元素是否存在
def isElementExist(self, element):
    flag = True
    browser = self
    try:
        # browser.find_element_by_class_name(element)
        browser.find_all("div", {"class": element})
        return flag

    except:
        flag = False
        return flag

def ipthreadingFunc():
    for ii in itertools.count(1):
        ip = basefunc.randIp()

        #如果IP池没有数据那么退出这个线程
        if ip == False:
            return
        try:
            cookies = urllib2.HTTPCookieProcessor()
            proxyHandler = urllib2.ProxyHandler({"http": r'http://%s' % ip})
            opener = urllib2.build_opener(cookies, proxyHandler)
            opener.addheaders = [('User-agent',
                                  'Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9B176 MicroMessenger/4.3.2')]
            req = opener.open('http://weixin.sogou.com/weixin?type=2&query=whcbnews&ie=utf8&_sug_=n&_sug_type_=1', timeout=20)
            result = req.read()
            res = BeautifulSoup(result, 'html.parser')
            # print(result)
            bools = isElementExist(res, 'wx-rb')
            yzbools = isElementExist(res, 'anti-box')

            if bools == False:
                raise Exception(r"页面打开了，但是找不到节点")
            # if yzbools != False:
            #     raise Exception(r"页面打开了，但是是验证页面")
            print(ip)

        except Exception as e:
            print(e)
            basefunc.delIP(ip)


#ip分线程并发处理采集回来的ip
#这里只是进行线程处理，没有任何逻辑
def ipthreading(nums=30):
    threads = []

    for i in range(1, nums):
        s = 't%s' % i
        s = threading.Thread(target=ipthreadingFunc, args=())
        threads.append(s)

    return  threads


threadss = ipthreading()
if __name__ == '__main__':
    for t in threadss:
        t.setDaemon(True)
        t.start()

    t.join()
    sleep(10)
    print(u'处理完所有ip')