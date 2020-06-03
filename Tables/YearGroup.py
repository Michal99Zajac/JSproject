import sqlite3

class YearGroup(object):
    field_num = {}
    all_students = []

    @staticmethod
    def create_tab(db):
        """
        ***function must be execute after create
        student and year_group table***\n
        function create table year_group
        """

        sql = """CREATE TABLE IF NOT EXISTS year_group (
            id_year_group INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            year_group_number INTEGER NOT NULL,
            id_student INTEGER,
            id_field_of_study INTEGER NOT NULL,
            FOREIGN KEY (id_student) REFERENCES student(id_student)
            ON UPDATE CASCADE
            ON DELETE CASCADE,
            FOREIGN KEY (id_field_of_study) REFERENCES field_of_study(id_field_of_study)
            ON UPDATE CASCADE
            ON DELETE CASCADE
        );
        """

        if db.get_conn() is not None:
            db.create_tab(sql)
        else:
            print("Error! Cant create year_group table")

    @staticmethod
    def select_all(db):
        cur = db.cursor_conn()
        cur.execute("SELECT * FROM year_group ORDER BY year_group_number")
        rows = cur.fetchall()

        return rows

    def __init__(self, number = 10, field = None, students = {}):
        self.__number = None
        self.__field = None
        self.__students = None
        try:
            if field in YearGroup.field_num.keys():
                if number not in YearGroup.field_num[field]:
                    self.__number = number
                    self.__field = field
                    YearGroup.field_num[self.__field].append(self.__number)
                else:
                    raise ValueError
            else:
                self.__number = number
                self.__field = field
                YearGroup.field_num[self.__field] = [self.__number]
        except ValueError:
            print("Number and field_od_study in group is booked")

        self.__students = students #{student: id_year}

        for student in self.__students:
            YearGroup.all_students.append(student)

    def show_group(self, db):
        sql = """SELECT * FROM year_group
        WHERE year_group_number = ? AND id_field_of_study = ?
        """

        cur = db.cursor_conn()
        cur.execute(sql, (self.__number, self.__field.get_id()))
        rows = cur.fetchall()

        return rows

    #add student
    def insert(self, student, db):
        sql = """INSERT INTO year_group(
            year_group_number,
            id_student,
            id_field_of_study
        ) VALUES (?,?,?)
        """

        YearGroup.all_students.append(student)

        values = (
            self.__number,
            student.get_id(),
            self.__field.get_id()
        )

        cur = None
        if db.get_conn() is not None:
            cur = db.cursor_conn()
            cur.execute(sql, values)
            self.__students[student] = cur.lastrowid
        else:
            print("Error! Cant insert in year_group table")


    def update(self, db):
        sql = """UPDATE year_group SET
        year_group_number = ?,
        id_field_of_study = ?
        WHERE id_year_group = ?
        """

        cur = None
        cur = db.cursor_conn()
        for student in  self.__students:
            values = (
                self.__number,
                self.__field.get_id(),
                self.__students[student]
            )

            if db.get_conn() is not None:
                cur.execute(sql, values)
            else:
                print("Error! Cant update in year_group table")

    #remove group
    def delete(self, db):
        sql = """DELETE FROM year_group WHERE year_group_number = ? AND id_field_of_study = ?"""

        if db.get_conn() is not None:
            cur = db.cursor_conn()
            cur.execute(sql, (self.__number, self.__field.get_id()))

            for student in self.__students:
                YearGroup.all_students.remove(student)

            self.__students = {}
        else:
            print("Error! Cant delete in year_group table")

    #remove student
    def delete_student(self, student, db):
        sql = """DELETE FROM year_group WHERE id_student = ?"""

        if db.get_conn() is not None:
            cur = db.cursor_conn()
            YearGroup.all_students.remove(student)
            del self.__students[student]
            cur.execute(sql, (student.get_id(),))
        else:
            print("Error! Cant delete student in year_group table")

    def get_id(self):
        ids = []
        for student in self.__students:
            ids.append(self.__students[student])

        return ids

    def set_number(self, number):
        try:
            if number not in YearGroup.field_num[self.__field]:
                YearGroup.field_num[self.__field].remove(self.__number)
                self.__number = number
                YearGroup.field_num[self.__field].append(self.__number)
            else:
                raise ValueError
        except ValueError:
            print("Number is booked")

    def set_field(self, field):
        try:
            if field in YearGroup.field_num.keys():
                if self.__number not in YearGroup.field_num[field]:
                    YearGroup.field_num[self.__field].remove(self.__number)
                    self.__field = field
                    YearGroup.field_num[self.__field].append(self.__number)
                else:
                    raise ValueError
            else:
                YearGroup.field_num[self.__field].remove(self.__number)
                self.__field = field
                YearGroup.field_num[self.__field] = [self.__number]
        except ValueError:
            print("Number of group in field is booked")

    def get_number(self):
        return self.__number

    def get_field(self):
        return self.__field

    def get_students(self):
        return self.__students.keys()

    def get_idxes(self):
        return self.__students.values()

    def get_all_students(self):
        return self.__students