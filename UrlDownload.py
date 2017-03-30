#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import urllib2
import selenium.webdriver.support.ui as ui
from bs4 import BeautifulSoup
import UserAgents
from selenium.webdriver.common.keys import Keys
from time import sleep
from urllib2 import quote
import urlparse
import requests
import re
import json
import time
import cgi
import db
import sys
import HTMLParser,pymysql
import json

#代理
service_args = [
    '--proxy=proxy.abuyun.com:9010',
    '--proxy-type=http',
    '--proxy-auth=HE1022KPM6W5935P:BEA893E7441DA3A4',
]
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


def download(url, num_retries=2, user_agent=''):
    try:
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        # dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53  (KHTML, like Gecko) Chrome/15.0.87")
        dcap["phantomjs.page.settings.userAgent"] = UserAgents.getRandAgent()
        dcap["phantomjs.page.settings.resourceTimeout"] = "5000"
        dcap["phantomjs.page.settings.loadImages"]  =  False

        driver = webdriver.PhantomJS(desired_capabilities=dcap, service_args=service_args)
	driver.implicitly_wait(5)
        driver.set_page_load_timeout(10)
        driver.set_script_timeout(10)
        driver.get(url)
        # print(driver.page_source)
        #print(u'=====================================打开搜狗搜索页面=====================================')

        bsObj = BeautifulSoup(driver.page_source, 'html.parser')
	
        #判断是否有此公众号和是否ip限制，如果找不到元素那么抛出异常
        wx_rb = isElementExist(bsObj, 'wx-rb')

        if wx_rb == False:
	    driver.quit()
            download(url)
            return

        #返回页面HTML
        html = driver.page_source.encode('utf-8')
        #print(u"=====================================返回公众号搜索页面=====================================")
        return html
    except Exception as e:
        print(e)
        # 抛出的异常接住，再次调用
        # n = num_retries-1
        #print(u'-------------------------------------公众号异常处理')
        html = None
        if num_retries > 0:
            return download(url, num_retries - 1)

#接收一个公众号的URL,进行所有文章的link收集
def getcodeinseturl(url, num_retries=2):
    myTime = time.strftime('%Y%m%d', time.localtime(time.time() - 24 * 60 * 60))
    try:
        # print(myTime)
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] = UserAgents.getRandAgent()
        dcap["phantomjs.page.settings.resourceTimeout"] = "5000"
        dcap["phantomjs.page.settings.loadImages"]  =  False

        # print(url)
        # exit()
        driver = webdriver.PhantomJS(desired_capabilities=dcap, service_args=service_args)
	driver.implicitly_wait(5)
        driver.set_page_load_timeout(10)
        driver.set_script_timeout(10)
        driver.get(url)

        #print('dfasdfasdfadfasdfasdfasd')
	#exit()
        # print(driver.page_source)instwenzhang
        #print(u'============================打开搜狗微信公众号文章列表页面=============================')
	print(u"open public code page")

        bsObj = BeautifulSoup(driver.page_source, 'html.parser')
        _bool = isElementExist(bsObj, 'weui_media_title')


        if _bool == False:
	    driver.quit()
            (url)
            return

        urlList = driver.find_elements_by_class_name('weui_media_title')
        tmpurllist = []
        for i in urlList:
            tmpurllist.append(i.get_attribute('hrefs'))

        #print(u'=============================返回微信公众号文章列表Link========================')
	print(u"return public code article list")
        return tmpurllist

    except Exception as e:
        print(e)
        #print(u'-----------------------------------文章异常处理')
	print(u"artilce note")
        tmpurllist = []
        if num_retries > 0:
            return getcodeinseturl(url, num_retries - 1)

def getwenzhanginfo(url, num_retries=2):
    try:
        # 代理服务器
        proxyHost = "proxy.abuyun.com"
        proxyPort = "9010"

        # 代理隧道验证信息
        proxyUser = "HE1022KPM6W5935P"
        proxyPass = "BEA893E7441DA3A4"

        proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
            "host": proxyHost,
            "port": proxyPort,
            "user": proxyUser,
            "pass": proxyPass,
        }

        proxies = {
            "http": proxyMeta,
            "https": proxyMeta,
        }

        s = requests.Session()
        r = s.get(url, verify=True, proxies=proxies, timeout=5000)
        bsObj = BeautifulSoup(r.content, 'html.parser')
        # print(bsObj)
        html = bsObj

    except Exception as e:
        html = None
        print(e)
        if num_retries > 0:
            return getwenzhanginfo(url, num_retries - 1)
    return html

def getwenzhangjson(url, num_retries=2):
    data = None
    try:
        # 代理服务器
        proxyHost = "proxy.abuyun.com"
        proxyPort = "9010"

        # 代理隧道验证信息
        proxyUser = "HE1022KPM6W5935P"
        proxyPass = "BEA893E7441DA3A4"

        proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
            "host": proxyHost,
            "port": proxyPort,
            "user": proxyUser,
            "pass": proxyPass,
        }

        proxies = {
            "http": proxyMeta,
            "https": proxyMeta,
        }

        s = requests.Session()
        r = s.get(url, verify=True, proxies=proxies).json()
        data = r
    except Exception as e:
        print(e)
        if num_retries > 0:
            return getwenzhangjson(url, num_retries - 1)
    return data

#获取微信文章真实地址
def getwenzhangurl(url='', html=''):
    try:
        html = str(html)
        uin = re.findall('var appuin = "(.*?)";', html)
        uin = str(uin[0])
        txt = uin.replace('"||"', "")

        urls = url + "&uin=%s" %txt

        # 代理服务器
        proxyHost = "proxy.abuyun.com"
        proxyPort = "9010"

        # 代理隧道验证信息
        proxyUser = "HE1022KPM6W5935P"
        proxyPass = "BEA893E7441DA3A4"

        proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
            "host": proxyHost,
            "port": proxyPort,
            "user": proxyUser,
            "pass": proxyPass,
        }

        proxies = {
            "http": proxyMeta,
            "https": proxyMeta,
        }

        s = requests.Session()
        r = s.get(urls, verify=True, proxies=proxies, allow_redirects=False, timeout=5000)
        return  r.headers['Location']

    except Exception as e:
        print(e)
        return None

#公众号的文章列表页面，统一拿数据到mysql中，再用PHP来处理
def getArticleList(url, codes):
    try:
        reload(sys)
        sys.setdefaultencoding('utf8')
        html_parser = HTMLParser.HTMLParser()

        # 代理服务器
        proxyHost = "proxy.abuyun.com"
        proxyPort = "9010"

        # 代理隧道验证信息
        proxyUser = "HE1022KPM6W5935P"
        proxyPass = "BEA893E7441DA3A4"

        proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
            "host": proxyHost,
            "port": proxyPort,
            "user": proxyUser,
            "pass": proxyPass,
        }

        proxies = {
            "http": proxyMeta,
            "https": proxyMeta,
        }

        s = requests.Session()
        r = s.get(url, verify=True, proxies=proxies, allow_redirects=False, timeout=5000)
        #time.sleep(3)
        html = BeautifulSoup(r.content, 'html.parser',from_encoding="utf-8")
        jsonstr = re.findall('var msgList = (.*?)}}]};', str(html))
	
	#公众号基本信息
	#codebase = html.find_all("div", "profile_desc_value")
	#print(codebase)
	#exit()

        if len(jsonstr) < 1:
            # print(html)
            #raise Exception("没有正则到列表")
            raise Exception("no rege")


        contents = cgi.escape(str(jsonstr[0]))
        b = contents.replace("'", '"')
        b += "}}]}"

        # b = json.loads(b)
        # b = json.dumps(b)
        # print(json.load(b))
        #
        # exit()

        conn = pymysql.connect(host='118.178.91.98', unix_socket='/tmp/mysql.sock', user='root', passwd='ai~!@dsi$@ds',
                               db='guoke',
                               charset='utf8')
        cur = conn.cursor()
        sql = "insert into gk_jsonstr (strs,code) values ('%(a)s','%(b)s')" % {
            "a": b,
            "b": codes,
        }
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()

        db.upData(codes)

    except Exception as e:
        print(e)

