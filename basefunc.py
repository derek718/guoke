#coding:utf-8
import urllib2
import re,os,pymysql,time
import itertools
import urlparse
import threading
from bs4 import BeautifulSoup
import cgi
import sys
import HTMLParser


#传入一个页面资源进行find找寻
def resultfind(html=''):
    bsObj = BeautifulSoup(html, 'html.parser')
    # allCode = bsObj.find_all("div", class_="wx-rb")
    # allCode = bsObj.find_all("div", {"class": "wx-rb"})
    allCode = bsObj.find_all("a", {"uigs": "main_toweixin_account_name_0"})

    url = ''
    for i in allCode:
        if 'href' in i.attrs:
            url = i.attrs['href']
        break
    # print(u'=====================================反回公众号列表页面URL'+url)
    #print(u'=====================================反回公众号列表页面URL=====================================')
    return url


#抓取微信文章一些基本信息
def wenzhangDataFind(html):
    reload(sys)
    sys.setdefaultencoding('utf8')
    html_parser = HTMLParser.HTMLParser()

    try:
        data=[]
        title = html.find("h2", {"id": "activity-name"}).contents
        times = html.find("em", {"id": "post-date"}).contents
        user = html.find("a", {"id": "post-user"}).contents
        contents = html.find("div", {"id":"js_content"})
        # a = a.decode('utf-8')
        # print(a)
        # exit()
        # a = html_parser.unescape(contents)
        #
        contents = cgi.escape(str(contents))
        b = contents.replace("'", '"')
	b = ""
        # b = contents.replace('body{font-family:"Helvetica Neue",Helvetica,"Hiragino Sans GB","Microsoft YaHei",Arial,sans-serif}', '')
        # print(b)
        # exit()
        title = title[0].strip()
        times = times[0].strip()
        user = user[0].strip()
        contents = contents
        data.append(title)
        data.append(times)
        data.append(user)
        data.append(b)

    except Exception as e:
        data = None
        print(e)

    return data
