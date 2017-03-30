#coding:utf-8
author = 'haoning'
import time
import datetime
import requests
import urllib2
from bs4 import BeautifulSoup
import urlparse
#from urlparse import urlparse
# from urllib2.parse import urlparse
import re
import json

url = 'http://weixin.sogou.com/weixin?type=2&query='
a = urllib2.quote("楼市又出重磅消息！开发商还能扛住吗？rmrbwx")
url += a

# 代理服务器
proxyHost = "proxy.abuyun.com"
proxyPort = "9010"

# 代理隧道验证信息
proxyUser = "HE1022KPM6W5935P"
proxyPass = "BEA893E7441DA3A4"

proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
  "host" : proxyHost,
  "port" : proxyPort,
  "user" : proxyUser,
  "pass" : proxyPass,
}

proxies = {
    "http"  : proxyMeta,
    "https" : proxyMeta,
}

s = requests.Session()
dr = re.compile(r'<[^>]+>',re.S)

# s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
# r = s.get("http://httpbin.org/cookies")
r = s.get(url, verify=True, proxies=proxies)
bsObj = BeautifulSoup(r.content, 'html.parser')

soup_text = bsObj.select("h4 a")
pattern = '<a.*?href="(.+)" id="(.+)">(.*?)</a>'
content_list = []

for text in soup_text:
    txt = str(text).replace("&amp;", "&")
    ret = re.search(pattern, txt)
    href = ret.groups()[0]
    title = dr.sub('', ret.groups()[2])
    content_list.append({'href': href, 'title': title})

content_links = content_list
comment_list = []
for link in content_links:
    parse = urlparse.urlparse(link['href'])
    param = parse.query
    comment_url = 'http://mp.weixin.qq.com/mp/getcomment?{}'.format(param)
    comment = s.get(comment_url).json()

    print(comment)
    exit()