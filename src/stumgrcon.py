#!/bin/baaash/env python
# -*- coding:utf-8 -*-

from prettytable import PrettyTable
from functions import Functions

def displayMenu():
    print "#####################"
    print "#  Student Manager  #"
    print "#                   #"
    print "# 1.insert student  #"
    print "# 2.modifiy grade   #"
    print "# 3.get student info#"
    print "# 4.get choice      #"
    print "# 5.get average     #"
    print "# 6.search teached  #"
    print "# 7.show dismissing #"
    print "#                   #"
    print "# 0.exit            #"
    print "#                   #"
    print "#####################"
    sel = 0
    while True:
        sel = int(raw_input('> '))
        if sel<0 or sel>7:
            print "wrong choice retry."
        else:
            break
    return sel

def insertStu(Fun):
    while True:
        print "Student info: "
        id_ = raw_input('id: ')
        name = raw_input('name: ')
        gender = raw_input("gender<'F' 'M' or 'X'>: ")
        birth = raw_input('birthday<example "20010902">: ')
        class_ = raw_input('class: ')
        try:
            Fun.insertStudent(id_,name,gender,birth,class_)
            print "Sucess!"
        except Exception,e:
            print "Failed.",e
        sel = raw_input('continue?[y/n] ')
        if sel=='n' or sel=='N':
            break
            
def modifyGrade(Fun):
    while True:
        id_ = raw_input("student id: ")
        course = raw_input("course id: ")
        redo = False
        sel = raw_input('normal grades?[y/n] ')
        if sel=='n' or sel=='N':
            redo = True
        grade = raw_input("grades: ")
        try:
            Fun.insertGrade(id_,course,grade,redo)
            print "Success!"
        except Exception,e:
            print "Failed!"
        sel = raw_input('continue?[y/n] ')
        if sel=='n' or sel=='N':
            break

def getStuInfo(Fun):
    while True:
        mode = raw_input('by what?[id/name/dept] ')
        key = raw_input('key: ')
        try:
            data = Fun.getStuInfo(key, mode)
        except Exception,e:
            print "Failed to get student information.",e
            return
        pt = PrettyTable()
        pt._set_field_names('id name dept gender birthday'.split())
        for each in data:
            pt.add_row(each)
        print pt
        sel = raw_input('continue?[y/n] ')
        if sel=='n' or sel=='N':
            break

def getChoice(Fun):
    while True:
        id_ = raw_input('student id: ')
        try:
            data = Fun.getCourseChoice(id_)
        except Exception,e:
            print "Failed to get choice information.",e
            return
        pt = PrettyTable()
        pt._set_field_names('Sid Sname Cid Cname weight semester nature grades regrades'.split())
        for each in data:
            pt.add_row(each)
        print pt
        sel = raw_input('continue?[y/n] ')
        if sel=='n' or sel=='N':
            break
            
def getAve(Fun):
    while True:
        id_ = raw_input('student id: ')
        sel = raw_input('including elective?[Y/n] ')
        full = True
        if sel=='n' or sel=='N':
            full = False
        try:
            ave = Fun.getAverage(id_,full)
        except Exception,e:
            print "Failed to get average information.",e
            return
        print "Average scroe: ",ave
        sel = raw_input('continue?[y/n] ')
        if sel=='n' or sel=='N':
            break
        
def getTeachInfo(Fun):
    while True:
        id_ = raw_input('student id: ')
        try:
            data = Fun.getTeached(id_)
        except Exception,e:
            print "Failed to get teaching information.",e
            return
        pt = PrettyTable()
        pt._set_field_names('Tid Tname'.split())
        for each in data:
            pt.add_row(each)
        print pt
        sel = raw_input('continue?[y/n] ')
        if sel=='n' or sel=='N':
            break

def showDismiss(Fun):
    try:
        data = Fun.getTobeDismissed()
    except Exception,e:
        print "Failed to get teaching information.",e
        return
    pt = PrettyTable()
    pt._set_field_names('id name'.split())
    for each in data:
        pt.add_row(each)
    print pt


if __name__ == "__main__":
    Fun = Functions()
    while True:
        try:
            sel = displayMenu()
        except Exception,e:
            continue
        if sel==1:
            insertStu(Fun)
        elif sel==2:
            modifyGrade(Fun)
        elif sel==3:
            getStuInfo(Fun)
        elif sel==4:
            getChoice(Fun)
        elif sel==5:
            getAve(Fun)
        elif sel==6:
            getTeachInfo(Fun)
        elif sel==7:
            showDismiss(Fun)
        elif sel==0:
            quit()
