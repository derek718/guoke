#coding:utf-8
import urllib2
import bs4
import itertools
from time import sleep
import pymysql
import basefunc

User_Agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
header = {}
header['User-Agent'] = User_Agent

for page in itertools.count(1):
    #异常处理
    try:
        url = "http://www.xicidaili.com/nt/%d" % page
        req = urllib2.Request(url, headers=header)
        res = urllib2.urlopen(req).read()
        # res = fun.download(url)

        bsObj = bs4.BeautifulSoup(res, 'html.parser')
        #当前页面的所有tr标签
        allTr = bsObj.findAll("tr")
        # print(allTr)
        # exit()

        #记录到一个数组里
        tmpip = []
        #循环出来每个tr
        for x in range(1, len(allTr)):
            nowTr = allTr[x]
            ipArr = nowTr.findAll('td')

            ip = ipArr[1].text + ":" + ipArr[2].text
            print(ip)
            tmpip.append(ip)


        #插入动作
        basefunc.insertIPData(tmpip)
    except Exception as e:
        continue

    sleep(80)
