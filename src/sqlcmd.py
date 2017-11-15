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
    dept char(36) not null,
    size smallint check (size > -1 and size < 255),

    index ID(id),
    foreign key (dept)
        references tbl_department(id)
        on update cascade
);
"""
# teacher table
sql_teacher = """
create table tbl_teacher(
    id char(8) not null primary key,
    name char(36) not null,
    gender char(1) not null check (gender in ('F','M', 'X')),
    dept char(36) not null,

    index ID(id),
    foreign key (dept)
        references tbl_department(id)
        on update cascade
);
"""
# student table
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
        on update cascade
        on delete set null
);
"""
# teaching plan table
sql_plan = """
create table tbl_teachingplan(
    course char(4) not null,
    dept char(2) not null,
    semester smallint not null check(semester > 0 and semester < 9),
    nature  char(10) check (nature in ('elective','compulsory')),
    weight smallint check (weight > 0),
    teacher char(8),

    foreign key (course)
        references tbl_course(id)
        on update cascade,
    foreign key (dept)
        references tbl_department(id)
        on update cascade,
    foreign key (teacher)
        references tbl_teacher(id)
        on update cascade
        on delete set null
);
"""
# course choice table
sql_choice = """
create table tbl_coursechoice(
    id char(11) not null,
    course char(4) not null,
    grades smallint check(grades > -1 and grades < 101),
    regrades smallint check(grades > -1 and grades < 101),

    primary key (id, course),
    foreign key (id)
        references tbl_student(id)
        on update cascade,
    foreign key (course)
        references tbl_course(id)
        on update cascade
);
"""
