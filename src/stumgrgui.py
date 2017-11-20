#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from functions import Functions

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import easygui
from prettytable import PrettyTable

class MainWin(object):
    def __init__(self):
        self.root = Tk()
        self.root.geometry("480x280")
        self.root.title("Student Manager")
        self.root.resizable(FALSE,FALSE)
        self.Fun = Functions()
    
    def init(self):
        btns = []
        btn_cmds = [self.insertStu, self.getStu,
                    self.insertGrade, self.getChoice,
                    self.getAve, self.getTeached,
                    self.getDismiss, self.exit]
        btn_tags = ["add student", "find student",
                    "insert grade", "get choice",
                    "get average", "get teached",
                    "get to be dismissed", "Exit"]
        y = 30
        for i in range(0,4):
            btns.append(Button(self.root,command=btn_cmds[i],text=btn_tags[i]))
            btns[i].pack(side=LEFT, padx=5, pady=5)
            btns[i].place(height=40,width=150, x=60, y=y)
            y += 50
        y = 30
        for i in range(4,8):
            btns.append(Button(self.root,command=btn_cmds[i],text=btn_tags[i]))
            btns[i].pack(side=LEFT, padx=5, pady=5)
            btns[i].place(height=40,width=150, x=260, y=y)
            y += 50
            
    
    def start(self):
        self.root.mainloop()
    
    def exit(self):
        sure = messagebox.askyesno(message='Exit Student manager?',icon='question',title='Exit')
        if sure:
            quit()
    
    def insertStu(self):
        win = Toplevel()
        win.title("Add Student")
        win.geometry("300x220")
        win.resizable(FALSE,FALSE)
        lbl_tags=["ID:","Name:","Gender:","Birthday:","Class:"]
        info=[StringVar(),StringVar(),StringVar(),StringVar(),StringVar()]
        id_label = Label(win,text=lbl_tags[0])
        id_entry = Entry(win, textvariable=info[0])
        name_label = Label(win,text=lbl_tags[1])
        name_entry = Entry(win, textvariable=info[1])
        gender_label = Label(win,text=lbl_tags[2])
        gender_combo = ttk.Combobox(win, textvariable=info[2])
        gender_combo['values'] = ('Female', 'Male', 'Others')
        birth_label = Label(win,text=lbl_tags[3])
        birth_entry = Entry(win, textvariable=info[3])
        class_label = Label(win,text=lbl_tags[4])
        class_entry = Entry(win, textvariable=info[4])
        labels = [id_label, name_label, gender_label, 
                  birth_label, class_label]
        entries = [id_entry, name_entry, gender_combo, 
                   birth_entry, class_entry]
        lbl_x = 10
        etr_x = 90
        y = 10
        i = 0
        for i in range(0,5):
            lbl = labels[i]
            etr = entries[i]
            lbl.pack()
            etr.pack()
            lbl.place(height=30,width=80, x=lbl_x, y=y)
            etr.place(height=30,width=180, x=etr_x, y=y)
            y += 31
        def addstu():
            data = []
            for each in info:
                data.append(each.get())
            sel = messagebox.askokcancel(message="Check the information:\n ID: %s\nName: %s\nGender: %s\nBirthday: %s\nClass: %s"%(data[0], data[1], data[2], data[3], data[4]), icon='question', title='Check Info')
            if sel:
                if data[2] == 'Female':
                    data[2] = 'F'
                elif data[2] == 'Male':
                    data[2]='M'
                elif data[2] == 'Others':
                    data[2]='X'
                else:
                    messagebox.showinfo(message="Wrong information.Please check!", icon='error', title='Wrong Value')
                    return
                try:
                    self.Fun.insertStudent(data[0], data[1], data[2], data[3], data[4])
                    messagebox.showinfo(message="Student successfully added!", title='Success')
                except Exception,e:
                    messagebox.showinfo(message="Failed to add student.\n%s"%e, icon='error', title='Failure')
        def cancel():
            win.destroy()
        btn_add = Button(win,command=addstu,text="Add")
        btn_cancel = Button(win,command=cancel,text="Cancel")
        btn_add.pack()
        btn_cancel.pack()
        btn_add.place(height=30,width=80, x=50, y=175)
        btn_cancel.place(height=30,width=80, x=150, y=175)
    
    def getStu(self):
        win = Toplevel()
        win.title("Search Student")
        win.geometry("300x100")
        win.resizable(FALSE,FALSE)
        sel = StringVar()
        id_rb = ttk.Radiobutton(win, text='by ID', variable=sel, value='id')
        name_rb = ttk.Radiobutton(win, text='by name', variable=sel, value='name')
        dept_rb = ttk.Radiobutton(win, text='by department', variable=sel, value='dept')
        key = StringVar()
        key_entry = Entry(win, textvariable=key)
        def getstu():
            mode = sel.get()
            value = key.get()
            try:
                data = self.Fun.getStuInfo(value,mode)
                if data:
                    result = '   id     name   dept   gender birthday'
                    for each in data:
                        result += "\n"+"  ".join(each)
                else:
                    result = "None"
                easygui.codebox(msg="Results:",title="Result",text=result)
            except:
                easygui.exceptionbox()
        btn_ok = Button(win,command=getstu,text="Search")
        id_rb.pack()
        name_rb.pack()
        dept_rb.pack()
        key_entry.pack()
        btn_ok.pack()
        id_rb.place(height=20,width=80, x=5, y=5)
        name_rb.place(height=20,width=80, x=5, y=25)
        dept_rb.place(height=20,width=80, x=5, y=45)
        key_entry.place(height=30,width=180, x=95, y=6)
        btn_ok.place(height=25,width=80, x=140, y=40)
    
    def insertGrade(self):
        win = Toplevel()
        win.title("Modifiy Scores")
        win.geometry("260x45")
        win.resizable(FALSE,FALSE)
        sel = True
        def insertScore():
            try:
                fieldNames = ["Student ID:", "Course ID:","Score:"]
                values = []
                values = easygui.multenterbox("Enter Info:", "Update Score",fieldNames)
                data = self.Fun.insertGrade(values[0],values[1],int(values[2]),sel)
                messagebox.showinfo(message="Successful!", title='Success')
            except:
                easygui.exceptionbox()
        def insertN():
            sel = False
            insertScore()
        def insertS():
            sel = True
            insertScore()
        btn_ok = Button(win,command=insertN,text="Normal Exam")
        btn_no = Button(win,command=insertS,text="Second Exam")
        btn_ok.pack()
        btn_no.pack()
        btn_ok.place(height=30,width=100, x=12, y=6)
        btn_no.place(height=30,width=100, x=132, y=6)
    
    def getChoice(self):
        fieldNames = ["Student ID:"]
        values = []
        values = easygui.multenterbox("Enter Student ID:", "get Average Score",fieldNames)
        try:
            data = self.Fun.getCourseChoice(values[0])
            result = 'Sid Sname Cid Cname weight semester nature grades regrades'
            if data:
                for each in data:
                    result += "\n"+each[0]
                    result += "  "+each[1]
                    result += "  "+each[2]
                    result += "  "+each[3]
                    result += "  "+str(each[4])
                    result += "  "+str(each[5])
                    result += "  "+each[6]
                    result += "  "+str(each[7])
                    result += "  "+str(each[8])
            else:
                result = "None"
            easygui.codebox(msg="Results:",title="Result",text=result)
        except:
            easygui.exceptionbox()

    def getAve(self):
        fieldNames = ["Student ID:"]
        values = []
        values = easygui.multenterbox("Enter Student ID:", "get Average Score",fieldNames)
        value = values[0]
        full = messagebox.askyesno(message="Including elective courses?", icon='question', title='Check')
        try:
            ave = self.Fun.getAverage(value,full)
            messagebox.showinfo(message="Result:\nID: %s\nAverage Score: %s"%(value,ave), title='Result')
        except:
            easygui.exceptionbox()
        
    def getTeached(self):
        fieldNames = ["Student ID:"]
        values = []
        values = easygui.multenterbox("Enter Student ID:", "get Average Score",fieldNames)
        try:
            data = self.Fun.getTeached(values[0])
            result = "  Tid   Tname"
            if data:
                for each in data:
                    result += "\n"+"  ".join(each)
            else:
                result = "None"
            easygui.codebox(msg="Results:",title="Result",text=result)
        except:
            easygui.exceptionbox()
    
    def getDismiss(self):
        try:
            data = self.Fun.getTobeDismissed()
            result = "  id   name"
            if data:
                for each in data:
                    result += "\n"+"  ".join(each)
            else:
                result = "None"
            easygui.codebox(msg="Results:",title="Result",text=result)
        except:
            easygui.exceptionbox()

if __name__ == "__main__":
    mw = MainWin()
    mw.init()
    mw.start()

