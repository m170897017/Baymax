# /usr/bin/env python
# coding:utf-8
__author__ = 'stephen'
import pymysql.cursors

def test_for_db():
    connection = pymysql.connect(host='172.16.10.92',
                                 user='eleme',
                                 password='eleMe',
                                 db='eleme',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor
                                 )

    try:
        # with connection.cursor() as cursor:
        #     # Create a new record
        #     sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        #     cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
        #
        # # connection is not autocommit by default. So you must commit to save
        # # your changes.
        # connection.commit()

        with connection.cursor() as cursor:
            # Read a single record
            # sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
            sql = 'select description from restaurant where id=17850'
            # cursor.execute(sql, ('webmaster@python.org',))
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result)
    finally:
        connection.close()

###############

def test_for_requests():

    import requests


    url = 'http://walis127.eleme.test/api/bd/restaurant/17850/detail'
    token = '6e334e6a-be03-4c9b-9215-228cae604fa4'
    my_session = requests.session()
    my_session.headers.update({'Authorization':token,
                                     'HTTP_ACCESS_TOKEN':token,
            # 'Origin': 'http://{host}'.format(host=host),
            # 'Authorization': token,
            # 'Accept-Encoding': 'gzip, deflate',
            # 'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',
            # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) '
            #               'AppleWebKit/537.36 (KHTML, like Gecko) '
            #               'Chrome/44.0.2403.61 Safari/537.36',
            # 'Content-Type': 'application/json;charset=UTF-8',
            # 'Accept': 'application/json, text/plain, */*',
            # 'Referer': 'http://{host}'.format(host=host),
            # 'HTTP_ACCESS_TOKEN': token,
            # 'Connection': 'keep-alive',
            # 'DNT': '1',  # 禁止追踪
                                     })
    print my_session.headers
    r = my_session.get(url)
    print r
    print r.text
    print dir(r)

def test_for_print():

    a = {"online_payment": 0, "description": "\u7f8e\u5473\u53ef\u53e3", "mobile": "", "admin_mobile": "", "address_text": "\u6d66\u4e1c\u5357\u8def999\u53f7\u65b0\u6885\u8054\u5408\u5e7f\u573a4\u697c", "cert_status": 0, "admin_status": 0, "come_from": 0, "bankcard_status": -2, "serving_time": [["10:00:00", "21:00:00"]], "id": 17850, "busy_level": 2, "name": "\u54c1\u724c\uff1a\u539a\u5473\u9999\u8fa3\u9986\uff08\u6d66\u4e1c\u5357\u8def\u5e97\uff09"}
    print a['description'].encode('utf-8')
    print str('美味可口'.encode('utf-8'))

if __name__ == '__main__':
    test_for_db()
    test_for_print()










