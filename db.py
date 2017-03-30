#coding:utf-8
import pymysql
import time

#得到库里的所有公众号编码
def getAllCode():
    retAll = []
    conn = pymysql.connect(host='118.178.91.98', unix_socket='/tmp/mysql.sock', user='root', passwd='ai~!@dsi$@ds',
                           db='guoke',
                           charset='utf8')
    cur = conn.cursor()
    #sql = "select wx_code from gk_public_number where is_py<>1 order by addtime DESC  limit 1"
    sql = "select wx_code from gk_public_number where is_py<>1 ORDER by rand() LIMIT 1"
    cur.execute(sql)
    AllCode = cur.fetchall()
    AllCode = list(AllCode)
    conn.commit()
    cur.close()
    conn.close()

    for code in AllCode:
        code = list(code)
        retAll.append(code[0])

    return  retAll



#插入到临时库里
def insertData(data,code=''):
    conn = pymysql.connect(host='118.178.91.98', unix_socket='/tmp/mysql.sock', user='root', passwd='ai~!@dsi$@ds', db='guoke',
                           charset='utf8')
    cur = conn.cursor()

    for link in data:
        sql = "insert into gk_tmpcodelist (code,link) values ('"+code+"','" + link + "')"
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()


#跑完一个公众号，进行公众号标明已完成采集任务
def upData( code = ''):
    conn = pymysql.connect(host='118.178.91.98', unix_socket='/tmp/mysql.sock', user='root', passwd='ai~!@dsi$@ds',
                           db='guoke',
                           charset='utf8')
    cur = conn.cursor()
    sql = "update gk_public_number set is_py=1 where wx_code='"+code+"'"
    cur.execute(sql)

    conn.commit()
    cur.close()
    conn.close()
    print(u'update')

#取一篇临时文章出来
def getTmpArt():
    retAll = []
    conn = pymysql.connect(host='118.178.91.98', unix_socket='/tmp/mysql.sock', user='root', passwd='ai~!@dsi$@ds',
                           db='guoke',
                           charset='utf8')
    cur = conn.cursor()
    # sql = "select * from gk_tmpcodelist where is_caiji <> 1 ORDER by rand() and id DESC LIMIT 1"
    sql = "select * from gk_tmpcodelist where is_caiji <> 1 ORDER by rand()  LIMIT 1"
    cur.execute(sql)
    AllCode = cur.fetchall()
    AllCode = list(AllCode)
    conn.commit()
    cur.close()
    conn.close()

    for code in AllCode:
        code = list(code)
        for v in code:
            retAll.append(v)
    return  retAll

#正式插入一篇文章
def instwenzhang(data):
    conn = pymysql.connect(host='118.178.91.98', unix_socket='/tmp/mysql.sock', user='root', passwd='ai~!@dsi$@ds',
                           db='pythons',
                           charset='utf8')
    cur = conn.cursor()
    # sql = "insert into gk_tmpcodelist (title,add_time,public_name,content,public_code,zan,hit) values ('"+data[0]+"','"+data[1]+"','"+data[2]+"','"+data[3]+"','"+data[4]+"','"+data[5]+"','"+data[6]+"')"
    sql = "insert into gk_article (title,add_time,public_name,content,public_code,zan,hit) values ('%(a)s','%(b)s','%(c)s','%(d)s','%(e)s','%(f)s','%(j)s')" % {
        "a": data[0],
        "b": data[1],
        "c": data[2],
        "d": data[3],
        "e": data[4],
        "f": data[5],
        "j": data[6],
    }

    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()

def delTmpWen(_id):
    _id = int(id)
    conn = pymysql.connect(host='118.178.91.98', unix_socket='/tmp/mysql.sock', user='root', passwd='ai~!@dsi$@ds',
                           db='guoke',
                           charset='utf8')
    cur = conn.cursor()
    sql = "delete from gk_tmpcodelist where id=%s" %_id
    cur.execute(sql)

    conn.commit()
    cur.close()
    conn.close()
    print(u'delete')

#更新文章临时表中数据
def uptmpdata(data,_id):
    time.sleep(2)
    try:
        if len(data) < 6:
            return False

        conn = pymysql.connect(host='118.178.91.98', unix_socket='/tmp/mysql.sock', user='root', passwd='ai~!@dsi$@ds',
                               db='guoke',
                               charset='utf8')
        cur = conn.cursor()
        sql = "update gk_tmpcodelist set is_caiji=1,title='%(a)s',add_time='%(b)s',public_name='%(c)s',content='%(d)s',public_code='%(e)s',zan='%(f)s',hit='%(g)s',wx_url='%(h)s' where id='%(i)s'" % {
            "a": data[0],
            "b": data[1],
            "c": data[2],
            "d": "",
            "e": data[4],
            "f": data[5],
            "g": data[6],
            "h": data[7],
            "i": _id,
        }
        # print(sql)
        # exit()
        cur.execute(sql)

        conn.commit()
        cur.close()
        conn.close()
        print(u'update')
        return True
    except Exception as e:
        print(e)
        return False

