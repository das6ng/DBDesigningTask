#!/bin/baaash/env python
# -*- coding:utf-8 -*-

# Usage:
#     initialize the Database
#

import pymysql

from connectDB import connectDB
from sqlcmd import *

class initObj(object):

    # get a DB connection
    def __init__(self):
        self.DBfd = connectDB()
        self.cursor = self.DBfd.cursor()

    # commit changes and close connection
    def __del__(self):
        self.DBfd.commit()
        self.DBfd.close()
        print "--> DB connection close."

    # ddrop a table
    def dropTable(self, table):
        msg = self.cursor.execute(sql_drop_table % table)
        print "msg> ",sql
        return msg

    # get all data from a table
    def getAllData(self, table):
        msg = self.cursor.execute(sql_select_all % table)
        print "msg> ",sql

        data = self.cursor.fetchall()
        return data


    # test table
    def createTestTable(self):
        sql = "create table test(id char(9) not null primary key, name char(16) not null);"
        msg = self.cursor.execute(sql)
        print "msg> ",sql
        return msg

    def insertTestData(self, id_, name_):
        sql = "insert into test(id, name) values (%s, %s);"
        msg = self.cursor.execute(sql, (id_, name_))
        print "msg> ",sql%(id_, name_)
        return msg


    # "department" table
    def createDepartmentTable(self):
        msg = self.cursor.execute(sql_dept)
        print "msg> department table created."

    # "course" table
    def createCourseTable(self):
        msg = self.cursor.execute(sql_course)
        print "msg> course table created."

    # "class" table
    def createClassTable(self):
        msg = self.cursor.execute(sql_class)
        print "msg> class table created."

    # "teacher" table
    def createTeacherTable(self):
        msg = self.cursor.execute(sql_teacher)
        print "msg> teacher table created."

    # "students" table
    def createStudentTable(self):
        msg = self.cursor.execute(sql_student)
        print "msg> student table created."

    # "teachingplan" table
    def createTeachingplanTable(self):
        msg = self.cursor.execute(sql_plan)
        print "msg> plan table created."

    def createCoursechoiceTable(self):
        msg = self.cursor.execute(sql_choice)
        print "msg> choice table created."

### Test process ###
if __name__ == "__main__":
    c = initObj()

    def testTable():
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

    def dropAllTables():
        try:
            c.dropTable('tbl_coursechoice')
        except Exception,e:
            print "except> ",e
            pass
        try:
            c.dropTable('tbl_teachingplan')
        except Exception,e:
            print "except> ",e
            pass
        try:
            c.dropTable('tbl_student')
        except Exception,e:
            print "except> ",e
            pass
        try:
            c.dropTable('tbl_course')
        except Exception,e:
            print "except> ",e
            pass
        try:
            c.dropTable('tbl_department')
        except Exception,e:
            print "except> ",e
            pass
        try:
            c.dropTable('tbl_class')
        except Exception,e:
            print "except> ",e
            pass
        try:
            c.dropTable('tbl_teacher')
        except Exception,e:
            print "except> ",e
            pass

    def createAllTables():
        try:
            c.createDepartmentTable()
            c.createCourseTable()
            c.createClassTable()
            c.createTeacherTable()
        except Exception,e:
            print "->ERROR on createTable. ",e
        try:
            c.createStudentTable()
            print "msg> stu tbl created."
        except Exception,e:
            print "->ERROR on createStudentTable(). ",e
        try:
            c.createTeachingplanTable()
            print "msg> plan tbl created."
        except Exception,e:
            print "->ERROR on createTeachingplanTable(). ",e
        try:
            c.createCoursechoiceTable()
            print "msg> choice tbl created."
        except Exception,e:
            print "->ERROR on createCoursechoiceTable(). ",e

    # drop tables
    for i in range(1,3):
        dropAllTables()
        print " #",i
    # create tables
    createAllTables()

###################
