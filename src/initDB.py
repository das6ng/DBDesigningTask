#!/bin/baaash/env python
# -*- coding:utf-8 -*-

# Usage:
#     initialize the Database
#

import pymysql

from connectDB import connectDB

sql_dept = """
create table tbl_department(
    id char(2) not null primary key,
    name char(36) not null,
    
    index ID(id)
);
"""
sql_course = """
create table tbl_course(
    id char(4) not null primary key,
    name char(36) not null,
    
    index ID(id)
);
"""
sql_class = """
create table tbl_class(
    id char(2) not null primary key,
    dept char(36) not null,
    size smallint check (size > -1 and size < 255),

    index ID(id),
    foreign key (dept)
        references tbl_department(id)
);
"""
sql_teacher = """
create table tbl_teacher(
    id char(2) not null primary key,
    name char(36) not null,
    gender char(1) not null check (gender in ('F','M', 'X')),
    dept char(36) not null,

    index ID(id),
    foreign key (dept)
        references tbl_department(id)
);
"""
sql_student = """
create table tbl_student(
    id char(11) not null primary key,
    name char(36) not null,
    gender char(1) not null check (gender in ('F','M', 'X')),
    birthday char(8),
    dept char(2),

    index ID(id),
    foreign key (dept)
        references tbl_department(id)
);
"""
sql_plan = """
create table tbl_teachingplan(
    class char(2) not null,
    course char(4) not null,
    dept char(2) not null,
    semester smallint check(semester > 0 and semester < 9),
    nature  char(10) check (nature in ('elective','compulsory')),
    weight smallint check (weight > 0),
    
    primary key (class, course, dept),
    foreign key (class)
        references tbl_class(id),
    foreign key (course)
        references tbl_course(id),
    foreign key (dept)
        references tbl_department(id)
);
"""
sql_choice = """
create table tbl_coursechoice(
    id char(11) not null,
    course char(4) not null,
    grades smallint check(grades > -1 and grades < 101),
    regrades smallint check(grades > -1 and grades < 101),

    primary key (id, course),
    foreign key (id)
        references tbl_student(id),
    foreign key (course)
        references tbl_course(id)
);
"""

class initObj(object):
    
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
    
    # ddrop a table
    def dropTable(self, table):
        sql = "drop table %s;"%table
        msg = self.cursor.execute(sql)
        print "msg> ",sql
        return msg
    
    # get all data from a table
    def getAllData(self, table):
        sql = "select * from %s;"%table
        msg = self.cursor.execute(sql)
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
