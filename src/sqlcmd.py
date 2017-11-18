#!/bin/baaash/env python
# -*- coding:utf-8 -*-

# Usage:
#     All sql commands
#   DB name: StuMgr
#

### common sql commands ###
sql_drop_table = "drop table %s;"
sql_select_all = "select * from %s;"

### table creation ###
# department table
sql_dept = """
create table tbl_department(
    id char(2) not null primary key,
    name char(36) not null,

    index ID(id)
);
"""
# course table
sql_course = """
create table tbl_course(
    id char(4) not null primary key,
    name char(36) not null,

    index ID(id)
);
"""
# class table
sql_class = """
create table tbl_class(
    id char(8) not null primary key,
    dept char(2) not null,
    size smallint check (size > -1 and size < 255),

    index ID(id),
    foreign key (dept)
        references tbl_department(id)
);
"""
# teacher table
sql_teacher = """
create table tbl_teacher(
    id char(8) not null primary key,
    name char(36) not null,
    gender char(1) not null check (gender in ('F','M', 'X')),
    dept char(2),

    index ID(id),
    foreign key (dept)
        references tbl_department(id)
);
"""
# student table
sql_student = """
create table tbl_student(
    id char(11) not null primary key,
    name char(36) not null,
    gender char(1) not null check (gender in ('F','M', 'X')),
    birthday char(8),
    class char(8),

    index ID(id),
    foreign key (class)
        references tbl_class(id)
);
"""
# teaching plan table
sql_plan = """
create table tbl_teachingplan(
    dept char(2) not null,
    course char(4) not null,
    semester smallint not null check(semester > 0 and semester < 9),
    nature  char(10) check (nature in ('elective','compulsory')),
    weight smallint check (weight > 0),

    primary key (course, dept),
    foreign key (course)
        references tbl_course(id),
    foreign key (dept)
        references tbl_department(id)
);
"""

# teaching
sql_teaching = """
create table tbl_teaching(
    class char(8),
    course char(4),
    teacher char(8),

    primary key (class,course,teacher),
    foreign key (class)
        references tbl_class(id),
    foreign key (course)
        references tbl_course(id),
    foreign key (teacher)
        references tbl_teacher(id)
);
"""
sql_teaching_check = """
DROP TRIGGER IF EXISTS teaching_check;
CREATE TRIGGER teaching_check BEFORE INSERT ON tbl_teaching
FOR EACH ROW
  BEGIN
    IF NEW.teacher IN (
         SELECT tbl_teaching.teacher
             FROM tbl_teaching
             WHERE tbl_teaching.class = NEW.class
    ) THEN
    SIGNAL SQLSTATE '55555' SET MESSAGE_TEXT =
        'A teacher cannot be assigned to one specific class more than once.';
    END IF;
  END;
"""

# course choice table
sql_choice = """
create table tbl_coursechoice(
    id char(11) not null,
    course char(4) not null,
    semester smallint not null check(semester > 0 and semester < 9),
    grades smallint check(grades > -1 and grades < 101),
    regrades smallint check(grades > -1 and grades < 101),

    primary key (id, course),
    foreign key (id)
        references tbl_student(id),
    foreign key (course)
        references tbl_course(id)
);
"""




### View Creations ###

# stu_base_info
sql_view_stu = """
CREATE VIEW stu_base_info(id,name,dept,gender,birthday) AS
    SELECT DISTINCT S.id, S.name, D.name, S.gender,S.birthday
    FROM tbl_student S, tbl_department D, tbl_class C
    WHERE S.class=C.id and C.dept=D.id
"""

# teach_stu_info
sql_view_teach_stu = """
CREATE VIEW teach_stu_info(Sid, Sname, Tid, Tname) AS
    SELECT DISTINCT S.id, S.name, T.id, T.name
    FROM tbl_student S, tbl_teacher T, tbl_teaching TG
    WHERE S.class=TG.class and TG.teacher=T.id
"""

# choice_info
sql_view_choice_info = """
CREATE VIEW choice_info(Sid,Sname,Cid,Cname,weight,semester,nature,grades,regrades) AS
    SELECT DISTINCT S.id,S.name,C.id,C.name,P.weight,
           P.semester,P.nature,CH.grades,CH.regrades
    FROM tbl_student S, tbl_course C, tbl_teachingplan P, tbl_coursechoice CH, tbl_class CL
    WHERE S.id=CH.id and CH.course=C.id and C.id=P.course and S.class=CL.id and CL.dept=P.dept
"""

# sum_fail_compl
sql_view_sum_compl = """
CREATE VIEW sum_compl_fail(id, name, sum) AS
    SELECT DISTINCT S.id,S.name,SUM(P.weight)
    FROM tbl_student S, tbl_coursechoice CH, tbl_teachingplan P
    WHERE S.id=CH.id and CH.course=P.course and P.nature='compulsory'
          and not (CH.grades>=60 or CH.regrades>=60)
    group by (S.id)
;
"""

# sum_fail_elec
sql_view_sum_elec = """
CREATE VIEW sum_elect_fail(id, name, sum) AS
    SELECT DISTINCT S.id,S.name,SUM(P.weight)
    FROM tbl_student S, tbl_coursechoice CH, tbl_teachingplan P
    WHERE S.id=CH.id and CH.course=P.course and P.nature='elective'
          and not (CH.grades>=60 or CH.regrades>=60)
    group by (S.id)
;
"""
