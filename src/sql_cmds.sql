--+ All MySQL commands needed in StuMgr+--

--+-------- table creations -------+--
create table tbl_department(
    id char(2) not null primary key,
    name char(36) not null,

    index ID(id)
);

create table tbl_course(
    id char(4) not null primary key,
    name char(36) not null,

    index ID(id)
);

create table tbl_class(
    id char(8) not null primary key,
    dept char(2) not null,
    size smallint check (size > -1 and size < 255),

    index ID(id),
    foreign key (dept)
        references tbl_department(id)
);

create table tbl_teacher(
    id char(8) not null primary key,
    name char(36) not null,
    gender char(1) not null check (gender in ('F','M', 'X')),
    dept char(2),

    index ID(id),
    foreign key (dept)
        references tbl_department(id)
);

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

create table tbl_coursechoice(
    id char(11) not null,
    course char(4) not null,
    semester smallint not null check(semester > 0 and semester < 9),
    grades smallint check(grades > -1 and grades < 101),
    regrades smallint check(grades > -1 and grades < 101),

    primary key (id, course,semester),
    foreign key (id)
        references tbl_student(id),
    foreign key (course)
        references tbl_course(id)
);
--+---------------+--
