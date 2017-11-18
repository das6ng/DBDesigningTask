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
        try:
            msg = self.cursor.execute(sql_drop_table % table)
            print "msg> ",sql_drop_table%table
        except Exception,e:
            print "msg>Cannot drop table ",table,"  ",e
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
        try:
            msg = self.cursor.execute(sql_dept)
            print "msg> department table created."
        except Exception,e:
            print "[!]Error when createDepartmentTable.  ",e

    # "course" table
    def createCourseTable(self):
        try:
            msg = self.cursor.execute(sql_course)
            print "msg> course table created."
        except Exception,e:
            print "[!]Error when createCourseTable. ",e

    # "class" table
    def createClassTable(self):
        try:
            msg = self.cursor.execute(sql_class)
            print "msg> class table created."
        except Exception,e:
            print "[!]Error when createClassTable. ",e

    # "teacher" table
    def createTeacherTable(self):
        try:
            msg = self.cursor.execute(sql_teacher)
            print "msg> teacher table created."
        except Exception,e:
            print "[!]Error when createTeacherTable. ",e

    # "students" table
    def createStudentTable(self):
        try:
            msg = self.cursor.execute(sql_student)
            print "msg> student table created."
        except Exception,e:
            print "[!]Error when createStudentTable. ",e

    # "teachingplan" table
    def createTeachingplanTable(self):
        try:
            msg = self.cursor.execute(sql_plan)
            print "msg> plan table created."
        except Exception,e:
            print "[!]Error when createTeachingplanTable. ",e

    # "teaching" table
    def createTeachingTable(self):
        try:
            msg = self.cursor.execute(sql_teaching)
            self.cursor.execute(sql_teaching_check)
            print "msg> teaching table created."
        except Exception,e:
            print "[!]Error when createTeachingTable. ",e

    # "course choice" table
    def createCoursechoiceTable(self):
        try:
            msg = self.cursor.execute(sql_choice)
            print "msg> choice table created."
        except Exception,e:
            print "[!]Error when createCoursechoiceTable. ",e

    def createViews(self):
        try:
            self.cursor.execute(sql_view_stu)
            self.cursor.execute(sql_view_teach_stu)
            self.cursor.execute(sql_view_choice_info)
            self.cursor.execute(sql_view_sum_compl)
            self.cursor.execute(sql_view_sum_elec)
        except Exception,e:
            print "[!]Error when create views. ",e

    def dropViews(self):
        try:
            self.cursor.execute("stu_base_info")
            self.cursor.execute("teach_stu_info")
            self.cursor.execute("choice_info")
            self.cursor.execute("sum_compl_fail")
            self.cursor.execute("sum_elect_fail")
        except Exception,e:
            print "except>Error when drop views.  ",e

### Test process ###
if __name__ == "__main__":
    c = initObj()

    def testTable():
        c.dropTable('test')
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
        c.dropTable('tbl_coursechoice')
        c.dropTable('tbl_teachingplan')
        c.dropTable('tbl_teaching')
        c.dropTable('tbl_student')
        c.dropTable('tbl_teacher')
        c.dropTable('tbl_course')
        c.dropTable('tbl_department')
        c.dropTable('tbl_class')

    def createAllTables():
        c.createDepartmentTable()
        c.createCourseTable()
        c.createClassTable()
        c.createTeacherTable()
        c.createStudentTable()
        c.createTeachingplanTable()
        c.createTeachingTable()
        c.createCoursechoiceTable()

    c.dropViews()
    # drop tables
    for i in range(1,3):
        dropAllTables()
        print " #",i
    # create tables
    createAllTables()
    c.createViews()

###################
