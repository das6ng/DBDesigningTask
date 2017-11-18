#!/bin/baaash/env python
# -*- coding:utf-8 -*-

# Usage:
#     insert test data into Database
#

import random
import pymysql

from connectDB import connectDB
from NamePicker import NamePicker

class InsertTestData(object):
    # get a DB connection
    def __init__(self):
        self.DBfd = connectDB()
        self.cursor = self.DBfd.cursor()
        self.np = NamePicker()

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

    def insertDept(self):
        f = open("../data/depts.txt")
        sql = "insert into tbl_department(id,name) values (%s,%s)"
        line = f.readline()
        print "Insert depratments: "
        count = 0
        while line:
            ll = line.split()
            msg = self.cursor.execute(sql, (ll[0],ll[1]))
            print "ll[0], ll[1]"
            line = f.readline()
            count += 1
        f.close()
        return count

    def insertCourses(self):
        f = open("../data/courses.txt")
        sql = "insert into tbl_course(id, name) values (%s,%s)"
        line = f.readline()
        count = 0
        print "Insert courses: "
        while line:
            ll = line.split()
            msg = self.cursor.execute(sql, (ll[0],ll[1]))
            print " ",ll[0]," ",ll[1]
            line = f.readline()
            count += 1
        f.close()
        return count

    def insertClasses(self):
        sql = "insert into tbl_class(id,dept,size) values (%s,%s,%s)"
        depts = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17']
        try:
            print "Insert classes: "
            count = 0
            for dept in depts:
                for clss in range(1,6):
                    id_ = '2020'+dept+str(clss)
                    self.cursor.execute(sql,(id_,dept,40))
                    print " ",id_," ",dept," 40"
                    count += 1
        except Exception,e:
            print e
        return count

    def insertTeachers(self):
        sql = "insert into tbl_teacher(id, name, gender, dept) values (%s,%s,%s,%s)"
        depts = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17']
        print "Insert teachers: "
        count = 0
        for dept in depts:
            for year in range(1998,2004):
                for no in range(10,17):
                    p = self.np.pickPerson()
                    id_ = str(year)+dept+str(no)
                    self.cursor.execute(sql, (id_, p[0], p[1], dept))
                    print id_," ",p[0]," ",p[1]," ",dept
                    count += 1
        return count

    def insertStudent(self, id_, name, gender, birth,class_):
        sql = "insert into tbl_student(id, name, gender, birthday,class) values (%s,%s,%s,%s,%s)"
        msg = self.cursor.execute(sql, (id_, name, gender, birth,class_))

    def insertStudents(self, n=0):
        self.cursor.execute("select id from tbl_class;")
        clss = self.cursor.fetchall()
        print "Insert students: "
        count = 0
        for cls in clss:
            cls = cls[0]
            for num in range(11,31):
                id_ = cls+str(num)
                p = self.np.pickPerson()
                self.insertStudent(id_,p[0], p[1], p[2],cls)
                print id_," ",p[0]," ",p[1]," ",p[2]
                count += 1
        return count

    def insertPlans(self):
        f = open("../data/plans.txt")
        sql = "insert into tbl_teachingplan(dept, course, semester, nature, weight) values (%s,%s,%s,%s,%s)"
        print "Insert plans: "
        count = 0
        line = f.readline()
        while line:
            l = line.split()
            print " ",line,
            self.cursor.execute(sql,(l[0],l[1],l[2],l[3],l[4]))
            count += 1
            line = f.readline()
        f.close()
        return count

    def insertTeaching(self):
        sql = "insert into tbl_teaching(class,course,teacher) values (%s,%s,%s)"
        self.cursor.execute("select dept,course from tbl_teachingplan")
        plans = self.cursor.fetchall()
        count = 0
        for plan in plans:
            self.cursor.execute("select id from tbl_class where id like '____%s_'"%plan[0])
            clss = self.cursor.fetchall()
            for cls in clss:
                cls = cls[0]
                self.cursor.execute("select teacher from tbl_teaching where class=%s"%cls)
                tt = self.cursor.fetchall()
                while True:
                    self.cursor.execute("select id from tbl_teacher where id like '____%s__'"%plan[1][0:2])
                    teachers = self.cursor.fetchall()
                    teacher = random.sample(teachers,1)[0][0]
                    if teacher not in tt:
                        break
                self.cursor.execute(sql,(cls,plan[1],teacher))
                print " ",cls," ",plan[1]," ",teacher
                count += 1
        return count

    def insertChoices(self):
        sql = "insert into tbl_coursechoice(id,course,semester) values (%s,%s,%s)"
        self.cursor.execute("select course,dept,semester from tbl_teachingplan where  nature='compulsory';")
        compls = self.cursor.fetchall()
        count = 0
        print "Insert choices:"
        for each in compls:
            self.cursor.execute("select id from tbl_student where class like '____%s_'"%each[1])
            stus = self.cursor.fetchall()
            for stu in stus:
                stu = stu[0]
                print " ",stu," ",each[0]," ",each[2]
                self.cursor.execute(sql,(stu,each[0],each[2]))
                count += 1
        return count

# test process
if __name__ == "__main__":
    obj = InsertTestData()

    cd = obj.insertDept()
    ct = obj.insertTeachers()
    cC = obj.insertClasses()
    cc = obj.insertCourses()
    cs = obj.insertStudents()
    cp = obj.insertPlans()
    ctc = obj.insertTeaching()
    #ccc = obj.insertChoices()

    print "Total: "
    print " departments: ",cd
    print " teachers: ",ct
    print " classes: ",cC
    print " students: ",cs
    print " courses: ",cc
    print " plans: ",cp
    print " teachings: ",ctc
    #print " choices: ",ccc

######
