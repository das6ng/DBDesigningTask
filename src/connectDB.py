#!/bin/baaash/env python
# -*- coding:utf-8 -*-

# Usage:
#     connect the Database
#   DB name: StuMgr
#

import pymysql

host = "127.0.0.1"
port = 3306
user = "stumgr"
passwd = "1234"
db = "StuMgr_test"

def connectDB():
    try:
        conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset='utf8')
        print "->DB connect sucess!"
    except Exception,e:
        print "->DB connect Failed!"

    return conn


if __name__ == "__main__":
    connectDB()
