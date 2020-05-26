import sqlite3

from Tables.Building import Building
from Tables.Dean import Dean
from Tables.DeansEmp import DeansEmp
from Tables.Department import Department
from Tables.ExeGroup import ExeGroup
from Tables.FieldOfStudy import FieldOfStudy
from Tables.LabGroup import LabGroup
from Tables.Room import Room
from Tables.Student import Student
from Tables.Subject import Subject
from Tables.Teacher import Teacher
from Tables.YearGroup import YearGroup

class TableDatabase(object):
    """
    class TableDatabase create connection
    to SQLite database and that can create
    tables
    """

    def __init__(self, db_file):
        self.conn = None
        
        #create connection
        try:
            self.conn = sqlite3.connect(db_file)
        except sqlite3.Error:
            print(sqlite3.Error)

        self.create_tables()

    def __str__(self):
        return 'Table Database class'

    def create_tab(self, table_sql):
        """
        function execute sql script for database
        :param table_sql: database file
        """
        try:
            cur = self.conn.cursor()
            cur.execute(table_sql)
        except sqlite3.Error:
            print(sqlite3.Error)

    def get_conn(self):
        """
        :return: connection object
        """
        return self.conn

    def close_conn(self):
        """
        function close connection
        """
        self.conn.close()

    def commit_conn(self):
        """
        function commit transaction
        """
        self.conn.commit()

    def cursor_conn(self):
        """
        :return: cursor connection
        """
        return self.conn.cursor()

    def create_tables(self):
        Building.create_tab(self)
        Dean.create_tab(self)
        Room.create_tab(self)
        Department.create_tab(self)
        DeansEmp.create_tab(self)
        FieldOfStudy.create_tab(self)
        Student.create_tab(self)
        ExeGroup.create_tab(self)
        LabGroup.create_tab(self)
        YearGroup.create_tab(self)
        Teacher.create_tab(self)
        Subject.create_tab(self)

    #create all objects from db
    def fetch_students(self, ls_fields_of_study):
        ls_students = []
        row = None
        for row in Student.select_all(self):
            for field in ls_fields_of_study:
                if row[6] == field.get_id():
                    ls_students.append(Student(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5],
                        field,
                        row[7]
                    ))
                    break
        else:
            if row != None:
                Student.set_idx(row[0])

        return ls_students

    def fetch_buildings(self):
        ls_buildings = []
        row = None
        for row in Building.select_all(self):
            ls_buildings.append(Building(
                row[0],
                row[1],
                row[2],
                row[3]
            ))
        else:
            if row != None:
                Building.set_idx(row[0])

        return ls_buildings

    def fetch_deans(self):
        ls_deans = []
        row = None
        for row in Dean.select_all(self):
            ls_deans.append(Dean(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6]
            ))
        else:
            if row != None:
                Dean.set_idx(row[0])

        return ls_deans

    def fetch_deans_emps(self, ls_departments):
        ls_deans_emps = []
        row = None
        for row in DeansEmp.select_all(self):
            for dept in ls_departments:
                if row[6] == dept.get_id():
                    ls_deans_emps.append(DeansEmp(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5],
                        dept
                    ))
                    break
        else:
            if row != None:
                DeansEmp.set_idx(row[0])

        return ls_deans_emps

    def fetch_rooms(self, ls_buildings):
        ls_rooms = []
        row = None
        for row in Room.select_all(self):
            for building in ls_buildings:
                if row[1] == building.get_id():
                    ls_rooms.append(Room(
                        row[0],
                        building,
                        row[2],
                        row[3]
                    ))
                    break
        else:
            if row != None:
                Room.set_idx(row[0])

        return ls_rooms

    def fetch_teachers(self, ls_departments):
        ls_teachers = []
        row = None
        for row in Teacher.select_all(self):
            for dept in ls_departments:
                if row[7] == dept.get_id():
                    ls_teachers.append(Teacher(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5],
                        row[6],
                        dept,
                        row[8]
                    ))
                    break
        else:
            if row != None:
                Teacher.set_idx(row[0])

        return ls_teachers

    def fetch_departments(self, ls_buildings, ls_deans):
        ls_departments = []

        row = None
        for row in Department.select_all(self):
            building_instance = None
            dean_instance = None
            for building in ls_buildings:
                if row[1] == building.get_id():
                    building_instance = building
                    break

            for dean in ls_deans:
                if row[5] == dean.get_id():
                    dean_instance = dean
                    break

            ls_departments.append(Department(
                        row[0],
                        building_instance,
                        row[2],
                        row[3],
                        row[4], 
                        dean_instance
                    ))
        else:
            if row != None:
                Department.set_idx(row[0])

        return ls_departments

    def fetch_fields_of_study(self, ls_departments, ls_deans_emps):
        ls_fields = []
        row = None
        for row in FieldOfStudy.select_all(self):
            dept_instance = None
            deans_emp_instance = None
            for dept in ls_departments:
                if row[2] == dept.get_id():
                    dept_instance = dept
                    break
            for deans_emp in ls_deans_emps:
                if row[3] == deans_emp.get_id():
                    deans_emp_instance = deans_emp
                    break
            
            ls_fields.append(FieldOfStudy(
                row[0],
                row[1],
                dept_instance,
                deans_emp_instance
            ))
        else:
            if row != None:
                FieldOfStudy.set_idx(row[0])

        return ls_fields

    def fetch_exe_groups(self, ls_students, ls_fields_of_study):
        ls_exe_groups = []
        field_num = {} #field_num = {field_id: [nums]}

        #create dict field_num
        for row in ExeGroup.select_all(self):
            if row[3] not in field_num.keys():
                field_num[row[3]] = [row[1]]
            else:
                if row[1] not in field_num[row[3]]:
                    field_num[row[3]].append(row[1])

        #create instances
        for field in field_num:
            field_instance = None

            #attaching field_id to an instance
            for f in ls_fields_of_study:
                if field == f.get_id():
                    field_instance = f
                    break

            for number in field_num[field]:
                students = {}

                #create dict students = {student: id_exe_group}
                for row in ExeGroup.select_all(self):
                    if field == row[3] and number == row[1]:
                        for student in ls_students:
                            if student.get_id() == row[2]:
                                students[student] = row[0]
                                break
                    
                ls_exe_groups.append(ExeGroup(
                    number,
                    field_instance,
                    students
                ))

        return ls_exe_groups

    def fetch_lab_groups(self, ls_students, ls_fields_of_study):
        ls_lab_groups = []
        field_num = {} #field_num = {field_id: [nums]}

        #create dict field_num
        for row in LabGroup.select_all(self):
            if row[3] not in field_num.keys():
                field_num[row[3]] = [row[1]]
            else:
                if row[1] not in field_num[row[3]]:
                    field_num[row[3]].append(row[1])

        #create instances
        for field in field_num:
            field_instance = None

            #attaching field_id to an instance
            for f in ls_fields_of_study:
                if field == f.get_id():
                    field_instance = f
                    break

            for number in field_num[field]:
                students = {}

                #create dict students = {student: id_lab_group}
                for row in LabGroup.select_all(self):
                    if field == row[3] and number == row[1]:
                        for student in ls_students:
                            if student.get_id() == row[2]:
                                students[student] = row[0]
                                break
                
                ls_lab_groups.append(LabGroup(
                    number,
                    field_instance,
                    students
                ))

        return ls_lab_groups

    def fetch_year_groups(self, ls_students, ls_fields_of_study):
        ls_year_groups = []
        field_num = {} #field_num = {field_id: [nums]}

        #create dict field_num
        for row in YearGroup.select_all(self):
            if row[3] not in field_num.keys():
                field_num[row[3]] = [row[1]]
            else:
                if row[1] not in field_num[row[3]]:
                    field_num[row[3]].append(row[1])

        #create instances
        for field in field_num:
            field_instance = None

            #attaching field_id to an instance
            for f in ls_fields_of_study:
                if field == f.get_id():
                    field_instance = f
                    break

            for number in field_num[field]:
                students = {}

                #create dict students = {student: id_year_group}
                for row in YearGroup.select_all(self):
                    if field == row[3] and number == row[1]:
                        for student in ls_students:
                            if student.get_id() == row[2]:
                                students[student] = row[0]
                                break
                
                ls_year_groups.append(YearGroup(
                    number,
                    field_instance,
                    students
                ))

        return ls_year_groups

    def fetch_subjects(self, ls_teachers, ls_lab_groups, ls_exe_groups, ls_year_groups, ls_rooms, ls_fields_of_study):
        ls_subjects = [] #list of instances

        subjects = [] #list of tuples

        #ultra object
        uteacher = Teacher(999999, "-------", "--------", "---------", 00000, "--------", "acd", None, "----------")
        uroom = Room(999999, None, 9999999, 0)

        #leter! Change to search differently in sql!
        for row in Subject.select_all(self):
            teacher_instance = None
            room_instance = None
            field_of_study_instance = None
            lab_group_instance = None
            exe_group_instance = None
            year_group_instance = None

            #search  correct teacher
            for teacher in ls_teachers:
                if row[1] == teacher.get_id():
                    teacher_instance = teacher
                    break
            else:
                teacher_instance = uteacher
            

            #search correct lab group
            if row[2] != None:
                for lab in ls_lab_groups:
                    if row[2] in lab.get_idxes():
                        lab_group_instance = lab
                        break

            #search correct exe group
            if row[3] != None:
                for exe in ls_exe_groups:
                    if row[3] in exe.get_idxes():
                        exe_group_instance = exe
                        break

            #search correct year group
            if row[4] != None:
                for year in ls_year_groups:
                    if row[4] in year.get_idxes():
                        year_group_instance = year
                        break

            #search correct room
            for room in ls_rooms:
                if row[5] == room.get_id():
                    room_instance = room
                    break
            else:
                room_instance = uroom

            #search correct field of study
            for field in ls_fields_of_study:
                if row[6] == field.get_id():
                    field_of_study_instance = field
                    break

            temp_subject = (
                teacher_instance.get_id(),
                # lab_group_instance,
                # exe_group_instance,
                # year_group_instance,
                room_instance.get_id(),
                field_of_study_instance.get_id(),
                row[7],
                row[8],
                row[9],
                row[10]
            )

            #chceck if this scheme has already been used
            if temp_subject not in subjects:
                subs = Subject.get_groups_id(self, temp_subject)
                ls_sub = []
                
                for sub in subs:
                    ls_sub.append(sub[0])

                ls_subjects.append(Subject(
                    ls_sub,
                    teacher_instance,
                    lab_group_instance,
                    exe_group_instance,
                    year_group_instance,
                    room_instance,
                    field_of_study_instance,
                    row[7],
                    row[8],
                    row[9],
                    row[10]
                ))
                subjects.append(temp_subject)
            
        return ls_subjects         
        