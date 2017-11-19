#!/bin/baaash/env python
# -*- coding:utf-8 -*-

# Student Menager APIs

import pymysql

from connectDB import connectDB

class Functions(object):
    # get a DB connection
    def __init__(self):
        self.DBfd = connectDB()
        self.cursor = self.DBfd.cursor()

    # commit changes and close connection
    def __del__(self):
        self.DBfd.commit()
        self.DBfd.close()
        print "--> DB connection close."

    def insertStudent(self, id_, name, gender, birthday, class_):
        sql = "insert into tbl_student(id,name,gender,birthday,class) values('%s','%s','%s','%s','%s');"%(id_, name, gender, birthday, class_)
        self.cursor.execute(sql)

    def insertGrade(self, id_, course, grade, redo=False):
        if not redo:
            self.cursor.execute("update tbl_coursechoice set grades=%s where id='%s' and course='%s'"%(grade,id_,course))
        else:
            self.cursor.execute("update tbl_coursechoice set regrades=%s where id='%s' and course='%s'"%(grade,id_,course))

    def getStuInfo(self, key, mode):
        data = []
        if mode not in ["id", "name", "dept"]:
            raise ValueError('mode="%s",check the arguement mode in["id", "name", "dept"]'%mode)
        if mode == "id":
            self.cursor.execute("select * from stu_base_info where id='%s'"%key)
            data = self.cursor.fetchall()
        elif mode == "name":
            self.cursor.execute("select * from stu_base_info where name='%s'"%key)
            data = self.cursor.fetchall()
        elif mode == "dept":
            self.cursor.execute("select * from stu_base_info where dept='%s'"%key)
            data = self.cursor.fetchall()
        return data

    def getCourseChoice(self, id_):
        self.cursor.execute("select * from choice_info where Sid='%s'"%id_)
        data = self.cursor.fetchall()
        return data

    def getAverage(self, id_, full=True):
        value = 0
        weight = 0
        self.cursor.execute("select weight,nature,grades,regrades from choice_info where Sid='%s'"%id_)
        data = self.cursor.fetchall()
        for each in data:
            wei = int(each[0])
            nature = each[1]
            grade = int(each[2])
            if grade < 60:
                grade = int(each[3])
            if nature == 'compulsory':
                value = (value*weight+grade*wei)/(wei+weight)
                weight += wei
            elif full:
                value = (value*weight+grade*wei)/(wei+weight)
                weight += wei
        return value

    def getTeached(self, id_):
        self.cursor.execute("select Tid,Tname from teach_stu_info where Sid='%s'"%id_)
        data = self.cursor.fetchall()
        return data

    def getTobeDismissed(self):
        self.cursor.execute("select id,name from sum_compl_fail where sum>12 union select id,name from sum_elect_fail where sum>17")
        data = self.cursor.fetchall()
        return data
