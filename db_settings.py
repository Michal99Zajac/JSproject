import sqlite3

from sqlite3 import Error



def create_db_connection(db_file):
    """
    create a database connection to a SQLite database.
    If SQLite database doesn't exist, then database will be created.
    :param db_file: database file
    :return Connection object or None
    """

    conn = None

    try:
        conn = sqlite3.connect(db_file)
    except Error:
        print(Error)

    return conn


def create_table(conn, create_table_sql):
    """
    create a table from create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    """

    try:
        curs = conn.cursor()
        curs.execute(create_table_sql)
    except Error:
        print(Error)


#create tables section

def create_students_table_sql(conn):
    """
    create a table Students with parameters:
    id_student, name, second_name, lastname, pesel,
    email, field_of_study, place_of_residence

    :param conn: Connection object
    """

    students_table_sql = """CREATE TABLE IF NOT EXISTS Students (
        id_student INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        name TEXT NOT NULL,
        second_name TEXT NOT NULL,
        lastname TEXT NOT NULL,
        pesel INTEGER NOT NULL,
        email TEXT,
        id_field_of_study INTEGER NOT NULL,
        place_of_residence TEXT NOT NULL,
        FOREIGN KEY (id_field_of_study) REFERENCES Fields_of_study(id_field_of_study)                                
    );
    """

    if conn is not None:
        create_table(conn, students_table_sql)
    else:
        print("Error! Cant create Students table")


def create_lab_group_table_sql(conn):
    """
    create a table Laboratory_groups with parameters:
    id_labolatory_group, labolatory_group_number,
    students

    :param conn: Connection object
    """

    lab_group_table_sql = """CREATE TABLE IF NOT EXISTS Laboratory_groups (
        id_labolatory_group INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        labolatory_group_number INTEGER NOT NULL,
        students INTEGER,
        FOREIGN KEY (students) REFERENCES Students(id_student)
    );
    """

    if conn is not None:
        create_table(conn, lab_group_table_sql)
    else:
        print("Error! Cant create Labolatory_groups table")


def create_exe_group_table_sql(conn):
    """
    create a table Exercise_groups with parameters:
    id_exercise_group, exercise_group_number,
    students

    :param conn: Connection object
    """

    exe_group_table_sql = """CREATE TABLE IF NOT EXISTS Exercise_groups (
        id_exercise_group INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        exercise_group_number INTEGER NOT NULL,
        students INTEGER,
        FOREIGN KEY (students) REFERENCES Students(id_student)
    );
    """

    if conn is not None:
        create_table(conn, exe_group_table_sql)
    else:
        print("Error! Cant create Exercise_groups table")


def create_year_group_table_sql(conn):
    """
    create a table Year_groups with parameters:
    id_year_group, year_group_number,
    students

    :param conn: Connection object
    """

    year_group_table_sql = """CREATE TABLE IF NOT EXISTS Year_groups (
        id_year_group INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        C INTEGER NOT NULL,
        students INTEGER,
        FOREIGN KEY (students) REFERENCES Students(id_student)
    );
    """

    if conn is not None:
        create_table(conn, year_group_table_sql)
    else:
        print("Error! Cant create Year_groups table")


def create_fields_of_study_table_sql(conn):
    """
    create a table Fields_of_study with parameters:
    id_field_of_study, name, id_department,
    id_leader_of_field_of_study

    :param conn: Connection object
    """

    f_of_study_table_sql = """CREATE TABLE IF NOT EXISTS Fields_of_study (
        id_field_of_study INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        name TEXT NOT NULL,
        id_department INTEGER NOT NULL,
        id_leader_of_field_of_study INTEGER NOT NULL,
        FOREIGN KEY (id_department) REFERENCES Departments(id_department),
        FOREIGN KEY (id_leader_of_field_of_study) REFERENCES deans_office_employees(id_deans_office_employees)
    );
    """

    if conn is not None:
        create_table(conn, f_of_study_table_sql)
    else:
        print("Error! Cant create Fields_of_study table")

    
def create_subjects_table_sql(conn):
    """
    create a table Subjects with parameters:
    id_subject, id_teacher, id_laboratory_group,
    id_exercise_group, id_year_group, room,
    day, hour_start, hour_end, id_field_of_study,
    name

    :param conn: Connection object
    """

    subject_table_sql = """CREATE TABLE IF NOT EXISTS Subjects (
        id_subject INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        id_teacher INTEGER NOT NULL,
        id_labolatory_group INTEGER,
        id_exercise_group INTEGER,
        id_year_group INTEGER,
        id_room INTEGER,
        day TEXT,
        hour_start TEXT,
        hour_end TEXT,
        id_field_of_study INTEGER NOT NULL,
        name TEXT NOT NULL,
        FOREIGN KEY (id_teacher) REFERENCES Teachers(id_teacher),
        FOREIGN KEY (id_labolatory_group) REFERENCES Laboratory_groups(id_labolatory_group),
        FOREIGN KEY (id_exercise_group) REFERENCES Exercise_groups(id_exercise_group),
        FOREIGN KEY (id_year_group) REFERENCES Year_groups(id_year_group),
        FOREIGN KEY (id_room) REFERENCES Rooms(id_room),
        FOREIGN KEY (id_field_of_study) REFERENCES Fields_of_study(id_field_of_study)
    );
    """

    if conn is not None:
        create_table(conn, subject_table_sql)
    else:
        print("Error! Cant create Subjects table")
    

def create_rooms_table_sql(conn):
    """
    create a table Rooms with parameters:
    id_room, id_building, room_number,
    is_deans_office

    :param conn: Connection object
    """

    room_table_sql = """CREATE TABLE IF NOT EXISTS Rooms (
        id_room INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        id_building INTEGER NOT NULL,
        room_number INTEGER NOT NULL,
        is_deans_office INTEGER NOT NULL,
        FOREIGN KEY (id_building) REFERENCES Buildings(id_building)
    );
    """

    if conn is not None:
        create_table(conn, room_table_sql)
    else:
        print("Error! Cant create Rooms table")

    
def create_buildings_table_sql(conn):
    """
    create a table Building with parameters:
    id_building, street_name, building_name,
    building_number

    :param conn: Connection object
    """

    building_table_sql = """CREATE TABLE IF NOT EXISTS Buildings (
        id_building INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        street_name TEXT NOT NULL,
        building_name TEXT NOT NULL,
        building_number INTEGER NOT NULL
    );
    """

    if conn is not None:
        create_table(conn, building_table_sql)
    else:
        print("Error! Cant create Buildings table")


def create_department_table_sql(conn):
    """
    create a table Departments with parameters:
    id_department, id_building,
    deans_office_start, deans_office_stop,
    dean

    :param conn: Connection object
    """

    department_table_sql = """CREATE TABLE IF NOT EXISTS Departments (
        id_department INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        id_building INTEGER NOT NULL,
        deans_office_start TEXT,
        deans_office_stop TEXT,
        id_dean INTEGER NOT NULL,
        FOREIGN KEY (id_building) REFERENCES Buildings(id_building),
        FOREIGN KEY (id_dean) REFERENCES Deans(id_dean)
    );
    """

    if conn is not None:
        create_table(conn, department_table_sql)
    else:
        print("Error! Cant create Departments table")


def create_deans_table_sql(conn):
    """
    create a table Deans with parameters:
    id_dean, name, lastname, second_name, pesel,
    email, place_of_residence

    :param conn: Connection object
    """

    deans_table_sql = """CREATE TABLE IF NOT EXISTS Deans (
        id_dean INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        name TEXT NOT NULL,
        lastname TEXT NOT NULL,
        second_name TEXT,
        pesel INTEGER NOT NULL,
        email TEXT,
        place_of_residence TEXT NOT NULL
    );
    """

    if conn is not None:
        create_table(conn, deans_table_sql)
    else:
        print("Error! Cant create Deans table")


def create_dean_office_emp_table_sql(conn):
    """
    create a table deans_office_employees with parameters:
    id_deans_office_employee, name, second_name,
    lastname, pesel, email, id_department

    :param conn: Connection object
    """

    dean_off_emp = """CREATE TABLE IF NOT EXISTS Deans_office_employees (
        id_deans_office_employees INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        name TEXT NOT NULL,
        second_name TEXT,
        lastname TEXT NOT NULL,
        pesel INTEGER NOT NULL,
        email TEXT,
        id_department INTEGER NOT NULL,
        FOREIGN KEY (id_department) REFERENCES Departments(id_department)
    );
    """

    if conn is not None:
        create_table(conn, dean_off_emp)
    else:
        print("Error! Cant create Deans_office_employees table")


def create_teachers_table_sql(conn):
    """
    create a table Teachers with parameters:
    id_teacher, name, second_name, lastname,
    pesel, email, academic_degree, id_department,
    place_of_residence

    :param conn: Connection object
    """

    teacher_table_sql = """CREATE TABLE IF NOT EXISTS Teachers (
        id_teacher INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        name TEXT NOT NULL,
        second_name TEXT,
        lastname TEXT NOT NULL,
        pesel INTEGER NOT NULL,
        email TEXT,
        academic_degree TEXT NOT NULL,
        id_department INTEGER NOT NULL,
        place_of_residence TEXT NOT NULL,
        FOREIGN KEY (id_department) REFERENCES Departments(id_department)
    );
    """

    if conn is not None:
        create_table(conn, teacher_table_sql)
    else:
        print("Error! Cant create Teachers table")


def create_all_tabels_sql(conn):
    """
    create all tables required to start application

    :param conn: Connection object
    :return: 0
    """

    #create table Buildings
    create_buildings_table_sql(conn)

    #create table Deans
    create_deans_table_sql(conn)

    #create table Rooms
    create_rooms_table_sql(conn)

    #create table Department
    create_department_table_sql(conn)

    #create table Deans_office_employees
    create_dean_office_emp_table_sql(conn)

    #create table Fields_of_study
    create_fields_of_study_table_sql(conn)

    #create table Students
    create_students_table_sql(conn)

    #create table Teachers
    create_teachers_table_sql(conn)

    #create table Year_group
    create_year_group_table_sql(conn)

    #create table Exercise_group
    create_exe_group_table_sql(conn)

    #create table Laboratory_group
    create_lab_group_table_sql(conn)

    #create table Subjects
    create_subjects_table_sql(conn)

    return 0


#insert vlaues to tables section

def create_teachers(conn, values):
    """
    insert data to table Teachers

    :param conn: Connection object
    :param values: tuple with informations
    :return cur.lastrowid: id of a given teacher
    """

    sql = """INSERT INTO Teachers(
        name,
        second_name,
        lastname,
        pesel,
        email,
        academic_degree,
        id_department,
        place_of_residence,
        ) VALUES (?,?,?,?,?,?,?,?)
        """

    cur = conn.cursor()
    try:
        cur.execute(sql,values)
    except Error:
        print(Error)

    return cur.lastrowid


def create_dean_office_emp(conn, values):
    """
    insert data to table Deans_office_employees

    :param conn: Connection object
    :param values: tuple with informations
    :return cur.lastrowid: id of a given Dean_office_employe
    """

    sql = """INSERT INTO Deans_office_employees(
        name,
        second_name,
        lastname,
        pesel,
        email,
        id_department
    ) VALUES (?,?,?,?,?,?)
    """

    cur = conn.cursor()
    try:
        cur.execute(sql,values)
    except Error:
        print(Error)

    return cur.lastrowid


def create_deans(conn, values):
    """
    insert data to table Deans

    :param conn: Connection object
    :param values: tuple with informations
    :return cur.lastrowid: id of a given dean
    """

    sql = """INSERT INTO Deans(
        name,
        lastname,
        second_name,
        pesel,
        email,
        place_of_residence
    ) VALUES (?,?,?,?,?,?)
    """

    cur = conn.cursor()
    try:
        cur.execute(sql,values)
    except Error:
        print(Error)

    return cur.lastrowid


def create_department(conn, values):
    """
    insert data to table Departments

    :param conn: Connection object
    :param values: tuple with informations
    :return cur.lastrowid: id of a given department
    """

    sql = """INSERT INTO Departments(
        id_building,
        deans_office_start,
        deans_office_stop,
        id_dean
    ) VALUES (?,?,?,?)
    """
    
    cur = conn.cursor()
    try:
        cur.execute(sql,values)
    except Error:
        print(Error)

    return cur.lastrowid


def create_building(conn, values):
    """
    insert data to table Buildings

    :param conn: Connection object
    :param values: tuple with informations
    :return cur.lastrowid: id of a given building
    """

    sql = """INSERT INTO Buildings(
        street_name,
        building_name,
        building_number
    ) VALUES (?,?,?)
    """

    cur = conn.cursor()
    try:
        cur.execute(sql,values)
    except Error:
        print(Error)

    return cur.lastrowid


def create_room(conn, values):
    """
    insert data to table Rooms

    :param conn: Connection object
    :param values: tuple with informations
    :return cur.lastrowid: id of a given room
    """
    
    sql = """INSERT INTO Rooms(
        id_building,
        room_number,
        is_deans_office
    ) VALUES (?,?,?)
    """

    cur = conn.cursor()
    try:
        cur.execute(sql,values)
    except Error:
        print(Error)

    return cur.lastrowid


def create_subject(conn, values):
    """
    insert data to table Subjects

    :param conn: Connection object
    :param values: tuple with informations
    :return cur.lastrowid: id of a given subjects
    """

    sql = """INSERT INTO Subjects(
        id_teacher,
        id_labolatory_group,
        id_exercise_group,
        id_year_group,
        id_room,
        day,
        hour_start,
        hour_end,
        id_field_of_study,
        name
    ) VALUES (?,?,?,?,?,?,?,?,?,?)
    """

    cur = conn.cursor()
    try:
        cur.execute(sql,values)
    except Error:
        print(Error)

    return cur.lastrowid


def create_field_of_study(conn, values):
    """
    insert data to table Fields_of_study

    :param conn: Connection object
    :param values: tuple with informations
    :return cur.lastrowid: id of a given field_of_study
    """

    sql = """INSERT INTO Fields_of_study(
        name,
        id_department,
        id_leader_of_field_of_study
    ) VALUES (?,?,?)
    """

    cur = conn.cursor()
    try:
        cur.execute(sql,values)
    except Error:
        print(Error)

    return cur.lastrowid


def create_year_group(conn,values):
    """
    insert data to table Year_groups

    :param conn: Connection object
    :param values: tuple with informations
    :return cur.lastrowid: id of a given year_group
    """

    sql = """INSERT INTO Year_groups(
        Year_groups,
        students
    ) VALUES (?,?)
    """

    cur = conn.cursor()
    try:
        cur.execute(sql,values)
    except Error:
        print(Error)

    return cur.lastrowid


def create_exe_group(conn, values):
    """
    insert data to table Exercise_groups

    :param conn: Connection object
    :param values: tuple with informations
    :return cur.lastrowid: id of a given exercise_group
    """

    sql = """INSERT INTO Exercise_groups(
        exercise_group_number,
        students
    ) VALUES (?,?)
    """

    cur = conn.cursor()
    try:
        cur.execute(sql,values)
    except Error:
        print(Error)

    return cur.lastrowid


def create_lab_group(conn, values):
    """
    insert data to table Laboratory_groups

    :param conn: Connection object
    :param values: tuple with informations
    :return cur.lastrowid: id of a given laboratory_group
    """

    sql = """INSERT INTO Laboratory_groups(
        labolatory_group_number,
        students
    ) VALUES (?,?)
    """

    cur = conn.cursor()
    try:
        cur.execute(sql,values)
    except Error:
        print(Error)

    return cur.lastrowid


def create_student(conn, values):
    """
    insert data to table Students

    :param conn: Connection object
    :param values: tuple with informations
    :return cur.lastrowid: id of a given student
    """

    sql = """INSERT INTO Students(
        name,
        second_name,
        lastname,
        pesel,
        email,
        id_field_of_study,
        place_of_residence
    ) VALUES (?,?,?,?,?,?,?)
    """

    cur = conn.cursor()
    try:
        cur.execute(sql,values)
    except Error:
        print(Error)

    return cur.lastrowid
