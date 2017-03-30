#coding:utf-8
import urllib2
import UrlDownload
import db
import basefunc
import threading
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import UserAgents
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from time import sleep
import urlparse
import itertools
import cgi
import time,random

def caijiJson():

        try:
            myTime = time.strftime('%Y%m%d', time.localtime(time.time() - 24 * 60 * 60))
            myTime = int(myTime)


            baseUrl = 'http://mp.weixin.qq.com'
            wzdata = db.getTmpArt()
            url = baseUrl + wzdata[2]   #搜狗微信文章link
  	    if len(wzdata) < 1:
		return False
	   
            urlParam = urlparse.urlparse(url)
            param = urlParam.query
            comment_url = 'http://mp.weixin.qq.com/mp/getcomment?{}'.format(param)
            html = UrlDownload.getwenzhanginfo(url)
            #文章时间
            times = html.find("em", {"id": "post-date"})
            times = str(times.contents[0])
            times = times.replace('-','')
            times = int(times)

            if times != myTime:
                db.delTmpWen(wzdata[0])



            if html == None:
                #raise Exception("打开文章失败")
                raise Exception("open aticle error")

            # 获取微信文章真实地址
            trueUrl = UrlDownload.getwenzhangurl(url, html)

            #抓取微信一些基本信息
            data = basefunc.wenzhangDataFind(html)

            if data == None:
                #raise Exception("获取文章基本失败")
                raise Exception("get article baseinfo error")

            if len(data) < 4:
                raise Exception("ewew")

            data.append(wzdata[1])

            #获取文章阅读数和点贊数
            dataJson = UrlDownload.getwenzhangjson(comment_url)

            if dataJson == None:
                #raise Exception("获取文章阅读数和点贊数失败")
                raise Exception("get article dianzan and yuedu error")
	    

            like_num = dataJson.get("like_num")
            read_num = dataJson.get("read_num")
            data.append(like_num)
            data.append(read_num)
            data.append(trueUrl)
            #print(data)
            #exit()
            bools = db.uptmpdata(data, wzdata[0])
            if bools == False:
                print(2)
                #continue

        except Exception as e:
            print(e)

class MyThread(threading.Thread):
    def run(self):
        wait_time = random.randrange(1, 3)
        time.sleep(wait_time)
        caijiJson()


if __name__ == "__main__":
    threads = []

    for i in range(30):
        t = MyThread()
        t.setDaemon(True)
        t.start()


    time.sleep(59)

