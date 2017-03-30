#coding:utf-8
import db
import UrlDownload
import basefunc
import threading
import itertools
import time

def pyphantomjs(a):
    # UrlDownload.download('http://weixin.sogou.com/weixin?type=1&query=rmrbwx&ie=utf8&_sug_=n&_sug_type_=')
    for i in itertools.count(1):
        try:
            baseUrl = 'http://weixin.sogou.com/weixin?type=1&ie=utf8&_sug_=n&_sug_type_='
            codes = db.getAllCode();
            baseUrl += '&query=' + codes[0]

            #返回资源
            driver = UrlDownload.download(baseUrl)
            nextUrl = ''

            #判断是否为None
            if driver != None:
                a = basefunc.resultfind(driver)
                if a != '':
                    nextUrl = a
            #
            # print(driver)
            # exit()
            tmpList = UrlDownload.getcodeinseturl(nextUrl)

            # print(tmpList)
            # exit()

            if len(tmpList) > 0:
                db.insertData(tmpList, codes[0])
                db.upData(codes[0])
            print(u'完成公众号文章列表采集')
        except Exception as e:
            print(e)

# pyphantomjs(1)
#ip分线程并发处理采集回来的ip
#这里只是进行线程处理，没有任何逻辑
# def ipthreading(nums=2):
#     threads = []
#
#     for i in range(1, nums):
#         s = 't%s' % i
#         s = threading.Thread(target=pyphantomjs, args=())
#         threads.append(s)
#
#     return  threads
#
# threadss = ipthreading()
# if __name__ == '__main__':
#     for t in threadss:
#         t.setDaemon(True)
#         t.start()
#
#     t.join()
#     print(u'=====================处理完所有公众号=======================')
# def func1(num):
#     for i in range(num):
#         #threading.currentThread()获取当前线程，getName()获取线程名字
#         print('I am %s.num:%s' % (threading.currentThread().getName(), i))
#
#
def main(thread_num):
    thread_list = []  # 定义一个线程列表
    for i in range(thread_num):
        thread_list.append(threading.Thread(target=pyphantomjs, args=(3,)))
        #thread_list.append(threading.Thread(target=pyphantomjs, args=(3,)))
    for a in thread_list:
        # a.setDaemon(True)这个setDaemon默认为False 非守护线程
        # 表示主线程等所有子线程结束后，在结束
        # 设置为True的话 表示是个守护线程 子线程就会随着主线程的结束而结束
        # 听说服务监控工具生成的心跳线程 就是用的守护线程
        a.start()

    for a in thread_list:
        a.join()  # 表示等待直到线程运行完毕

main(6)