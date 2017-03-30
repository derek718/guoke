#coding:utf-8
import threading,random,time
import db
import UrlDownload
import basefunc
import json
import itertools

def pyphantomjs():
    for i in itertools.count(1):
	if i >=5:
		break
        try:
            baseUrl = 'http://weixin.sogou.com/weixin?type=1&ie=utf8&_sug_=n&_sug_type_='
            print_r('dfasd')
            codes = db.getAllCode();
            if len(codes[0]) < 1:
                continue
            baseUrl += '&query=' + codes[0]
            #返回资源
            driver = UrlDownload.download(baseUrl)
            nextUrl = ''

            #判断是否为None
            if driver != None:
                a = basefunc.resultfind(driver)
                if a != '':
                    nextUrl = a

            UrlDownload.getArticleList(nextUrl, codes[0])

            #print(u'完成公众号文章列表采集')
	    print(u"Complete the article List color set")
        except Exception as e:
            print(e)

class MyThread(threading.Thread):
    def run(self):
        wait_time = random.randrange(1, 5)
        time.sleep(wait_time)
        pyphantomjs()


if __name__ == "__main__":
    threads = []

    for i in range(10):
        t = MyThread()
        t.setDaemon(True)
        t.start()
    #time.sleep(59)
