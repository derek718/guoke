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
import re

baseUrl = 'http://mp.weixin.qq.com'
wzdata = db.getTmpArt()
url = baseUrl + wzdata[2]
html = UrlDownload.getwenzhanginfo(url)

txt = UrlDownload.getwenzhangurl(url, html)

# var appuin = ""||"MjM5NzM0MzQ4MQ==";
# params = re.findall('''var msg_link = "(.*?)";''', content)
# uin = re.findall('var appuin = "(.*?)";', s)
# uin = str(uin[0])
# txt = uin.replace('"||"', "")
# txt = str(text).replace("&amp;", "&")
print(txt)

# relink = '<a href="(.*)">(.*)</a>'
# info = '<a href="http://www.baidu.com">baidu</a>'
# cinfo = re.findall(relink,s)
# print(cinfo)

# url = 'http://mp.weixin.qq.com/s?src=3&timestamp=1478842927&ver=1&signature=E8leMnMl0w3rGiyxTL8GneWammnw8lmdfa7iiabUqo9UWhoqqj3gfRJgnIwx-NozlCK*i3FlHJGRwOIq13LfyvnuLK97CPh3Rc*NzDO3uoE19WmB142CFgN2UnTNnoMvzfjdBjbwyesqr0UC7TQt33t7ddfK3BsxWai4E*3LZV0='
#
# urls = url +"&uin=MjM5ODAxMjU2MA%3D%3D"
#
# text = requests.get(urls,allow_redirects=False)
# print(text.headers['Location'])

