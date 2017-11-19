#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from functions import Functions

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

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
        win.geometry("300x220")
        win.resizable(FALSE,FALSE)
        sel = StringVar()
        id_rb = ttk.Radiobutton(win, text='by ID', variable=sel, value='id')
        name_rb = ttk.Radiobutton(parent, text='by name', variable=sel, value='name')
        dept_rb = ttk.Radiobutton(parent, text='by department', variable=sel, value='dept')
        key = StringVar()
        key_entry = Entry(win, textvariable=key)
        def getstu():
            pass
        btn_ok = Button(win,commond=getstu,text="Search")
        id_rb.pack()
        name_rb.pack()
        dept_rb.pack()
        key_entry.pack()
        btn_ok.pack()
        id_rb.place(height=30,width=80, x=150, y=175)
        name_rb.place(height=30,width=80, x=150, y=175)
        dept_rb.place(height=30,width=80, x=150, y=175)
        key_entry.place(height=30,width=80, x=150, y=175)
        btn_ok.place(height=30,width=80, x=150, y=175)
        pass
    
    def insertGrade(self):
        win = Toplevel()
        win.title("Search Grades")
        
        pass
        
    def getChoice(self):
        win = Toplevel()
        win.title("Search Choice")
        pass
        
    def getAve(self):
        win = Toplevel()
        win.title("Get Average Grade")
        pass
        
    def getTeached(self):
        win = Toplevel()
        win.title("Search Teached")
        pass
    
    def getDismiss(self):
        win = Toplevel()
        win.title("Search Dismissed")
        pass

if __name__ == "__main__":
    mw = MainWin()
    mw.init()
    mw.start()

