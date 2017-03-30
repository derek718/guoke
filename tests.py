#coding:utf-8
import urllib2
from  bs4 import BeautifulSoup
import threading,time

#判断一个元素是否存在
def isElementExist(self, element):
    flag = True
    browser = self
    try:
        # browser.find_element_by_class_name(element)
        # browser.find_element_by_class_name(element)
        browser.find_all("div",{"class":"wx-rb"})
        return flag

    except:
        flag = False
        return flag

# HOST = 'http://weixin.sogou.com/'
# url = HOST + "weixin?type=1&query=rmrbwx"
#
# req = urllib2.Request(url)
# res = urllib2.urlopen(req).read()
# bsObj = bs4.BeautifulSoup(res, 'html.parser')
# a = isElementExist(bsObj, 'wx-rb')
#
#
# print(a)

def demo1():
    # 要访问的目标页面
    targetUrl = "http://weixin.sogou.com/weixin?type=1&query=rmrbwx&ie=utf8&_sug_=n&_sug_type_=1&w=01015002&oq=&ri=12&sourceid=sugg&sut=0&sst0=1477963971468&lkt=0%2C0%2C0&p=40040108"
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

    proxy_handler = urllib2.ProxyHandler({
        "http": proxyMeta,
        "https": proxyMeta,
    })

    opener = urllib2.build_opener(proxy_handler)

    opener.addheaders = [("Proxy-Switch-Ip", "yes")]
    urllib2.install_opener(opener)
    resp = urllib2.urlopen(targetUrl).read()
    bsObj = BeautifulSoup(resp, 'html.parser')
    print(bsObj.title)

def demo2():
    # 要访问的目标页面
    targetUrl = "http://weixin.sogou.com/weixin?type=1&query=rmrbwx&ie=utf8&_sug_=n&_sug_type_=1&w=01015002&oq=&ri=12&sourceid=sugg&sut=0&sst0=1477963971468&lkt=0%2C0%2C0&p=40040108"
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

    proxy_handler = urllib2.ProxyHandler({
        "http": proxyMeta,
        "https": proxyMeta,
    })

    opener = urllib2.build_opener(proxy_handler)

    opener.addheaders = [("Proxy-Switch-Ip", "yes")]
    urllib2.install_opener(opener)
    resp = urllib2.urlopen(targetUrl).read()
    bsObj = BeautifulSoup(resp, 'html.parser')
    print(bsObj.title)

def demo3():
    # 要访问的目标页面
    targetUrl = "http://weixin.sogou.com/weixin?type=1&query=rmrbwx&ie=utf8&_sug_=n&_sug_type_=1&w=01015002&oq=&ri=12&sourceid=sugg&sut=0&sst0=1477963971468&lkt=0%2C0%2C0&p=40040108"
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

    proxy_handler = urllib2.ProxyHandler({
        "http": proxyMeta,
        "https": proxyMeta,
    })

    opener = urllib2.build_opener(proxy_handler)

    opener.addheaders = [("Proxy-Switch-Ip", "yes")]
    urllib2.install_opener(opener)
    resp = urllib2.urlopen(targetUrl).read()
    bsObj = BeautifulSoup(resp, 'html.parser')
    print(bsObj.title)

def demo4():
    # 要访问的目标页面
    targetUrl = "http://weixin.sogou.com/weixin?type=1&query=rmrbwx&ie=utf8&_sug_=n&_sug_type_=1&w=01015002&oq=&ri=12&sourceid=sugg&sut=0&sst0=1477963971468&lkt=0%2C0%2C0&p=40040108"
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

    proxy_handler = urllib2.ProxyHandler({
        "http": proxyMeta,
        "https": proxyMeta,
    })

    opener = urllib2.build_opener(proxy_handler)

    opener.addheaders = [("Proxy-Switch-Ip", "yes")]
    urllib2.install_opener(opener)
    resp = urllib2.urlopen(targetUrl).read()
    bsObj = BeautifulSoup(resp, 'html.parser')
    print(bsObj.title)

def demo5():
    # 要访问的目标页面
    targetUrl = "http://weixin.sogou.com/weixin?type=1&query=rmrbwx&ie=utf8&_sug_=n&_sug_type_=1&w=01015002&oq=&ri=12&sourceid=sugg&sut=0&sst0=1477963971468&lkt=0%2C0%2C0&p=40040108"
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

    proxy_handler = urllib2.ProxyHandler({
        "http": proxyMeta,
        "https": proxyMeta,
    })

    opener = urllib2.build_opener(proxy_handler)

    opener.addheaders = [("Proxy-Switch-Ip", "yes")]
    urllib2.install_opener(opener)
    resp = urllib2.urlopen(targetUrl).read()
    bsObj = BeautifulSoup(resp, 'html.parser')
    print(bsObj.title)

def demo6():
    # 要访问的目标页面
    targetUrl = "http://weixin.sogou.com/weixin?type=1&query=rmrbwx&ie=utf8&_sug_=n&_sug_type_=1&w=01015002&oq=&ri=12&sourceid=sugg&sut=0&sst0=1477963971468&lkt=0%2C0%2C0&p=40040108"
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

    proxy_handler = urllib2.ProxyHandler({
        "http": proxyMeta,
        "https": proxyMeta,
    })

    opener = urllib2.build_opener(proxy_handler)

    opener.addheaders = [("Proxy-Switch-Ip", "yes")]
    urllib2.install_opener(opener)
    resp = urllib2.urlopen(targetUrl).read()
    bsObj = BeautifulSoup(resp, 'html.parser')
    print(bsObj.title)

def demo7():
    # 要访问的目标页面
    targetUrl = "http://weixin.sogou.com/weixin?type=1&query=rmrbwx&ie=utf8&_sug_=n&_sug_type_=1&w=01015002&oq=&ri=12&sourceid=sugg&sut=0&sst0=1477963971468&lkt=0%2C0%2C0&p=40040108"
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

    proxy_handler = urllib2.ProxyHandler({
        "http": proxyMeta,
        "https": proxyMeta,
    })

    opener = urllib2.build_opener(proxy_handler)

    opener.addheaders = [("Proxy-Switch-Ip", "yes")]
    urllib2.install_opener(opener)
    resp = urllib2.urlopen(targetUrl).read()
    bsObj = BeautifulSoup(resp, 'html.parser')
    print(bsObj.title)

def demo8():
    # 要访问的目标页面
    targetUrl = "http://weixin.sogou.com/weixin?type=1&query=rmrbwx&ie=utf8&_sug_=n&_sug_type_=1&w=01015002&oq=&ri=12&sourceid=sugg&sut=0&sst0=1477963971468&lkt=0%2C0%2C0&p=40040108"
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

    proxy_handler = urllib2.ProxyHandler({
        "http": proxyMeta,
        "https": proxyMeta,
    })

    opener = urllib2.build_opener(proxy_handler)

    opener.addheaders = [("Proxy-Switch-Ip", "yes")]
    urllib2.install_opener(opener)
    resp = urllib2.urlopen(targetUrl).read()
    bsObj = BeautifulSoup(resp, 'html.parser')
    print(bsObj.title)

def demo9():
    # 要访问的目标页面
    targetUrl = "http://weixin.sogou.com/weixin?type=1&query=rmrbwx&ie=utf8&_sug_=n&_sug_type_=1&w=01015002&oq=&ri=12&sourceid=sugg&sut=0&sst0=1477963971468&lkt=0%2C0%2C0&p=40040108"
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

    proxy_handler = urllib2.ProxyHandler({
        "http": proxyMeta,
        "https": proxyMeta,
    })

    opener = urllib2.build_opener(proxy_handler)

    opener.addheaders = [("Proxy-Switch-Ip", "yes")]
    urllib2.install_opener(opener)
    resp = urllib2.urlopen(targetUrl).read()
    bsObj = BeautifulSoup(resp, 'html.parser')
    print(bsObj.title)

def demo10():
    # 要访问的目标页面
    targetUrl = "http://weixin.sogou.com/weixin?type=1&query=rmrbwx&ie=utf8&_sug_=n&_sug_type_=1&w=01015002&oq=&ri=12&sourceid=sugg&sut=0&sst0=1477963971468&lkt=0%2C0%2C0&p=40040108"
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

    proxy_handler = urllib2.ProxyHandler({
        "http": proxyMeta,
        "https": proxyMeta,
    })

    opener = urllib2.build_opener(proxy_handler)

    opener.addheaders = [("Proxy-Switch-Ip", "yes")]
    urllib2.install_opener(opener)
    resp = urllib2.urlopen(targetUrl).read()
    bsObj = BeautifulSoup(resp, 'html.parser')
    print(bsObj.title)


def demo11():
    # 要访问的目标页面
    targetUrl = "http://weixin.sogou.com/weixin?type=1&query=rmrbwx&ie=utf8&_sug_=n&_sug_type_=1&w=01015002&oq=&ri=12&sourceid=sugg&sut=0&sst0=1477963971468&lkt=0%2C0%2C0&p=40040108"
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

    proxy_handler = urllib2.ProxyHandler({
        "http": proxyMeta,
        "https": proxyMeta,
    })

    opener = urllib2.build_opener(proxy_handler)

    opener.addheaders = [("Proxy-Switch-Ip", "yes")]
    urllib2.install_opener(opener)
    resp = urllib2.urlopen(targetUrl).read()
    bsObj = BeautifulSoup(resp, 'html.parser')
    print(bsObj.title)

def demo12():
    # 要访问的目标页面
    targetUrl = "http://weixin.sogou.com/weixin?type=1&query=rmrbwx&ie=utf8&_sug_=n&_sug_type_=1&w=01015002&oq=&ri=12&sourceid=sugg&sut=0&sst0=1477963971468&lkt=0%2C0%2C0&p=40040108"
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

    proxy_handler = urllib2.ProxyHandler({
        "http": proxyMeta,
        "https": proxyMeta,
    })

    opener = urllib2.build_opener(proxy_handler)

    opener.addheaders = [("Proxy-Switch-Ip", "yes")]
    urllib2.install_opener(opener)
    resp = urllib2.urlopen(targetUrl).read()
    bsObj = BeautifulSoup(resp, 'html.parser')
    print(bsObj.title)

def demo13():
    # 要访问的目标页面
    targetUrl = "http://weixin.sogou.com/weixin?type=1&query=rmrbwx&ie=utf8&_sug_=n&_sug_type_=1&w=01015002&oq=&ri=12&sourceid=sugg&sut=0&sst0=1477963971468&lkt=0%2C0%2C0&p=40040108"
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

    proxy_handler = urllib2.ProxyHandler({
        "http": proxyMeta,
        "https": proxyMeta,
    })

    opener = urllib2.build_opener(proxy_handler)

    opener.addheaders = [("Proxy-Switch-Ip", "yes")]
    urllib2.install_opener(opener)
    resp = urllib2.urlopen(targetUrl).read()
    bsObj = BeautifulSoup(resp, 'html.parser')
    print(bsObj.title)

def demo14():
    # 要访问的目标页面
    targetUrl = "http://weixin.sogou.com/weixin?type=1&query=rmrbwx&ie=utf8&_sug_=n&_sug_type_=1&w=01015002&oq=&ri=12&sourceid=sugg&sut=0&sst0=1477963971468&lkt=0%2C0%2C0&p=40040108"
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

    proxy_handler = urllib2.ProxyHandler({
        "http": proxyMeta,
        "https": proxyMeta,
    })

    opener = urllib2.build_opener(proxy_handler)

    opener.addheaders = [("Proxy-Switch-Ip", "yes")]
    urllib2.install_opener(opener)
    resp = urllib2.urlopen(targetUrl).read()
    bsObj = BeautifulSoup(resp, 'html.parser')
    print(bsObj.title)

def demo15():
    # 要访问的目标页面
    targetUrl = "http://weixin.sogou.com/weixin?type=1&query=rmrbwx&ie=utf8&_sug_=n&_sug_type_=1&w=01015002&oq=&ri=12&sourceid=sugg&sut=0&sst0=1477963971468&lkt=0%2C0%2C0&p=40040108"
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

    proxy_handler = urllib2.ProxyHandler({
        "http": proxyMeta,
        "https": proxyMeta,
    })

    opener = urllib2.build_opener(proxy_handler)

    opener.addheaders = [("Proxy-Switch-Ip", "yes")]
    urllib2.install_opener(opener)
    resp = urllib2.urlopen(targetUrl).read()
    bsObj = BeautifulSoup(resp, 'html.parser')
    print(bsObj.title)

def demo16():
    # 要访问的目标页面
    targetUrl = "http://weixin.sogou.com/weixin?type=1&query=rmrbwx&ie=utf8&_sug_=n&_sug_type_=1&w=01015002&oq=&ri=12&sourceid=sugg&sut=0&sst0=1477963971468&lkt=0%2C0%2C0&p=40040108"
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

    proxy_handler = urllib2.ProxyHandler({
        "http": proxyMeta,
        "https": proxyMeta,
    })

    opener = urllib2.build_opener(proxy_handler)

    opener.addheaders = [("Proxy-Switch-Ip", "yes")]
    urllib2.install_opener(opener)
    resp = urllib2.urlopen(targetUrl).read()
    bsObj = BeautifulSoup(resp, 'html.parser')
    print(bsObj.title)

def demo17():
    # 要访问的目标页面
    targetUrl = "http://weixin.sogou.com/weixin?type=1&query=rmrbwx&ie=utf8&_sug_=n&_sug_type_=1&w=01015002&oq=&ri=12&sourceid=sugg&sut=0&sst0=1477963971468&lkt=0%2C0%2C0&p=40040108"
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

    proxy_handler = urllib2.ProxyHandler({
        "http": proxyMeta,
        "https": proxyMeta,
    })

    opener = urllib2.build_opener(proxy_handler)

    opener.addheaders = [("Proxy-Switch-Ip", "yes")]
    urllib2.install_opener(opener)
    resp = urllib2.urlopen(targetUrl).read()
    bsObj = BeautifulSoup(resp, 'html.parser')
    print(bsObj.title)

def demo18():
    # 要访问的目标页面
    targetUrl = "http://weixin.sogou.com/weixin?type=1&query=rmrbwx&ie=utf8&_sug_=n&_sug_type_=1&w=01015002&oq=&ri=12&sourceid=sugg&sut=0&sst0=1477963971468&lkt=0%2C0%2C0&p=40040108"
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

    proxy_handler = urllib2.ProxyHandler({
        "http": proxyMeta,
        "https": proxyMeta,
    })

    opener = urllib2.build_opener(proxy_handler)

    opener.addheaders = [("Proxy-Switch-Ip", "yes")]
    urllib2.install_opener(opener)
    resp = urllib2.urlopen(targetUrl).read()
    bsObj = BeautifulSoup(resp, 'html.parser')
    print(bsObj.title)

def demo19():
    # 要访问的目标页面
    targetUrl = "http://weixin.sogou.com/weixin?type=1&query=rmrbwx&ie=utf8&_sug_=n&_sug_type_=1&w=01015002&oq=&ri=12&sourceid=sugg&sut=0&sst0=1477963971468&lkt=0%2C0%2C0&p=40040108"
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

    proxy_handler = urllib2.ProxyHandler({
        "http": proxyMeta,
        "https": proxyMeta,
    })

    opener = urllib2.build_opener(proxy_handler)

    opener.addheaders = [("Proxy-Switch-Ip", "yes")]
    urllib2.install_opener(opener)
    resp = urllib2.urlopen(targetUrl).read()
    bsObj = BeautifulSoup(resp, 'html.parser')
    print(bsObj.title)

def demo20():
    # 要访问的目标页面
    targetUrl = "http://weixin.sogou.com/weixin?type=1&query=rmrbwx&ie=utf8&_sug_=n&_sug_type_=1&w=01015002&oq=&ri=12&sourceid=sugg&sut=0&sst0=1477963971468&lkt=0%2C0%2C0&p=40040108"
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

    proxy_handler = urllib2.ProxyHandler({
        "http": proxyMeta,
        "https": proxyMeta,
    })

    opener = urllib2.build_opener(proxy_handler)

    opener.addheaders = [("Proxy-Switch-Ip", "yes")]
    urllib2.install_opener(opener)
    resp = urllib2.urlopen(targetUrl).read()
    bsObj = BeautifulSoup(resp, 'html.parser')
    print(bsObj.title)

threads = []

t1 = threading.Thread(target=demo1)
threads.append(t1)
t2 = threading.Thread(target=demo2)
threads.append(t2)
t3 = threading.Thread(target=demo3)
threads.append(t3)
t4 = threading.Thread(target=demo4)
threads.append(t4)
t5 = threading.Thread(target=demo5)
threads.append(t5)
t6 = threading.Thread(target=demo6)
threads.append(t6)
t7 = threading.Thread(target=demo7)
threads.append(t7)
t8 = threading.Thread(target=demo8)
threads.append(t8)
t9 = threading.Thread(target=demo9)
threads.append(t9)
t10 = threading.Thread(target=demo10)
threads.append(t10)
# t11 = threading.Thread(target=demo11)
# threads.append(t11)
# t12 = threading.Thread(target=demo12)
# threads.append(t12)
# t13 = threading.Thread(target=demo13)
# threads.append(t13)
# t14 = threading.Thread(target=demo14)
# threads.append(t14)
# t15 = threading.Thread(target=demo15)
# threads.append(t15)
# t16 = threading.Thread(target=demo16)
# threads.append(t16)
# t17 = threading.Thread(target=demo17)
# threads.append(t17)
# t18 = threading.Thread(target=demo18)
# threads.append(t18)
# t19 = threading.Thread(target=demo19)
# threads.append(t19)
# t20 = threading.Thread(target=demo20)
# threads.append(t20)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()

    t.join()
    # time.sleep(10)
