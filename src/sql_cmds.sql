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
    id char(2) not null primary key,
    dept char(36) not null,
    size smallint check (size > -1 and size < 255),

    index ID(id),
    foreign key (dept)
        references tbl_department(id)
        on update cascade
);

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

create table tbl_teachingplan(
    class char(2) not null,
    course char(4) not null,
    dept char(2) not null,
    semester smallint check(semester > 0 and semester < 9),
    nature  char(10) check (nature in ('elective','compulsory')),
    weight smallint check (weight > 0),

    primary key (class, course, dept),
    foreign key (class)
        references tbl_class(id)
        on update cascade,
    foreign key (course)
        references tbl_course(id)
        on update cascade,
    foreign key (dept)
        references tbl_department(id)
        on update cascade
);

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
--+---------------+--
