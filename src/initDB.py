#!/bin/baaash/env python
# -*- coding:utf-8 -*-

# Usage:
#     initialize the Database
#

import pymysql

from connectDB import connectDB

class initObj(object):
    
    def __init__(self):
        self.DBfd = connectDB()
        self.cursor = self.DBfd.cursor()
        print "msg> <initObj>connecter called"
        
    def __del__(self):
        self.DBfd.commit()
        self.DBfd.close()
        print "->Db connection close."

    def dropTable(self, table):    
        sql = "drop table %s;"%table
        msg = self.cursor.execute(sql)
        
        print "msg D> ",msg
        return msg
        
    def getAllData(self, table):
        sql = "select * from %s;"%table
        msg = self.cursor.execute(sql)
        
        data = self.cursor.fetchall()
        return data
        
    
    def createTestTable(self):
        msg = self.cursor.execute("create table test(id char(9) not null primary key, name char(16) not null);")
        
        print "msg C> ",msg
        return msg
    
    def insertTestData(self, id_, name_):
        sql = "insert into test(id, name) values (%s, %s);"
        msg = self.cursor.execute(sql, (id_, name_))
        
        print "msg I> ",msg
        return msg

if __name__ == "__main__":
    c = initObj()
    try:
        c.dropTable('test')
    except Exception,e:
        print "->drop exception",e
        pass
    try:
        c.createTestTable()
    except Exception,e:
        print "->create exception",e
        pass
    for i in range(0,15):
        c.insertTestData(str(i), 'n'+str(i))
    try:
        r = c.getAllData("test")
        print "id name"
        for i in r:
            print i[0],' ',i[1]
    except Exception,e:
        print "->select exception. msg:",e
        pass
        
        
