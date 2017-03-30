#coding:utf-8
from selenium import webdriver
import re,os,pymysql
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

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

try:
    url = 'http://weixin.sogou.com/weixin?type=1&ie=utf8&_sug_=n&_sug_type_=&query=whcbnews'
    # url = 'http://www.baidu.com'
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53  (KHTML, like Gecko) Chrome/15.0.87")
    # service_args = [
    #     # '--proxy=51.254.106.68:80',
    #     '--proxy=HE1022KPM6W5935P:BEA893E7441DA3A4@proxy.abuyun.com:9010',
    #     '--proxy-type=http',
    # ]
    service_args = [
        '--proxy=proxy.abuyun.com:9010',
        '--proxy-type=http',
        '--proxy-auth=HE1022KPM6W5935P:BEA893E7441DA3A4',
    ]

    driver = webdriver.PhantomJS(service_args=service_args)
    # driver = webdriver.PhantomJS()
    driver.get(url)
    print(driver.page_source)

except Exception as e:
    print(e)


# try:
#     url = 'http://weixin.sogou.com/weixin?type=1&ie=utf8&_sug_=n&_sug_type_=&query=whcbnews'
#
#     PROXY='115.204.200.124:8998'
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument('--proxy-server=http://%s' % PROXY)
#     driver = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
#     driver.get(url)
#     print(driver)
# except Exception as e:
#     print(e)