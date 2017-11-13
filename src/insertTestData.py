#!/bin/baaash/env python
# -*- coding:utf-8 -*-

# Usage:
#     insert test data into Database
#

import pymysql

from connectDB import connectDB

class InsertTestData(object):
    # get a DB connection
    def __init__(self):
        self.DBfd = connectDB()
        self.cursor = self.DBfd.cursor()
        print "msg> initObj:consructor called."
    
    # commit changes and close connection    
    def __del__(self):
        self.DBfd.commit()
        self.DBfd.close()
        print "--> DB connection close."
    
    def insertTestData(self, id_, name_):
        sql = "insert into test(id, name) values (%s, %s);"
        msg = self.cursor.execute(sql, (id_, name_))
        print "msg> ",sql%(id_, name_)
        return msg
    
    # get all data from a table
    def getAllData(self, table):
        sql = "select * from %s;"%table
        msg = self.cursor.execute(sql)
        print "msg> ",sql
        
        data = self.cursor.fetchall()
        return data
    
    def insertStudent(self, id_, name, gender, birth):
        sql = "insert into tbl_student(id, name, gender, birthday) values (%s,%s,%s,%s)"
        msg = self.cursor.execute(sql, (id_, name, gender, birth))
        
        
# test process
if __name__ == "__main__":
    obj = InsertTestData()
    try:
        for i in range(1,100):
            obj.insertStudent(str(i),'Fuck', 'F', '19990909')
    except Exception,e:
        pass
    data = obj.getAllData('tbl_student')
    print data

######
