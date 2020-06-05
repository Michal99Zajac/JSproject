class ExeGroup(object):
    field_num = {}
    all_students = []

    @staticmethod
    def create_tab(db):
        """
        ***function must be execute after create
        student and field_of_study table***\n
        function create table exercise_group
        """

        sql = """CREATE TABLE IF NOT EXISTS exercise_group (
            id_exercise_group INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            exercise_group_number INTEGER NOT NULL,
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
            print("Error! Cant create exercise_group table")

    @staticmethod
    def select_all(db):
        """func return all exe group data from db

        Args:
            db (TableDatabase): database that you want to search

        Returns:
            List: list of tuples of data
        """
        cur = db.cursor_conn()
        cur.execute("""SELECT * FROM exercise_group
        ORDER BY exercise_group_number""")
        rows = cur.fetchall()

        return rows

    def __init__(self, number = 10, field = None, students = {}):
        """Init ExeGroup

        Args:
            number (int, optional): exe group number. Defaults to 10.
            field (FieldOfStudy, optional): exe group field of std. Defaults to None.
            students (dict, optional): {student obj: id}. Defaults to {}.

        Raises:
            ValueError: if number and field was created
        """
        self.__number = None
        self.__field = None
        try:
            if field in ExeGroup.field_num.keys():
                if number not in ExeGroup.field_num[field]:
                    self.__number = number
                    self.__field = field
                    ExeGroup.field_num[self.__field].append(self.__number)
                else:
                    raise ValueError
            else:
                self.__number = number
                self.__field = field
                ExeGroup.field_num[self.__field] = [self.__number]
        except ValueError:
            print("Number and field_od_study in group is booked")

        self.__students = students  # {student: id_exe}

        for student in self.__students:
            ExeGroup.all_students.append(student)

    def show_group(self, db):
        """func return exe group data from db

        Args:
            db (TableDatabase): database that you want to search

        Returns:
            List: list of tuples of data
        """
        sql = """SELECT * FROM exercise_group
        WHERE exercise_group_number = ? AND id_field_of_study = ?
        """

        cur = db.cursor_conn()
        cur.execute(sql, (self.__number, self.__field.get_id()))
        rows = cur.fetchall()

        return rows

    #add student
    def insert(self, student, db):
        """function insert student to group

        Args:
            db (TableDatabase): database that you want to search
            student (Student): student you want to insert
        """
        sql = """INSERT INTO exercise_group(
            exercise_group_number,
            id_student,
            id_field_of_study
        ) VALUES (?,?,?)
        """

        ExeGroup.all_students.append(student)

        values = (
            self.__number,
            student.get_id(),
            self.__field.get_id()
        )

        cur = None
        if db.get_conn() is not None:
            cur = db.cursor_conn()
            cur.execute(sql, values)
        else:
            print("Error! Cant insert in exercise_group table")

        self.__students[student] = cur.lastrowid

    def update(self, db):
        """function update data to db

        Args:
            db (TableDatabase): database that you want to update
        """
        sql = """UPDATE exercise_group SET
        exercise_group_number = ?,
        id_field_of_study = ?
        WHERE id_exercise_group = ?
        """

        cur = None
        cur = db.cursor_conn()
        for student in self.__students:
            values = (
                self.__number,
                self.__field.get_id(),
                self.__students[student]
            )

            if db.get_conn() is not None:
                cur.execute(sql, values)
            else:
                print("Error! Cant update in exercise_group table")

    #remove group
    def delete(self, db):
        """function delete data from db

        Args:
            db (TableDatabase): database that you want to update
        """
        sql = """DELETE FROM exercise_group WHERE exercise_group_number = ? AND id_field_of_study = ?"""

        if db.get_conn() is not None:
            cur = db.cursor_conn()
            cur.execute(sql, (self.__number, self.__field.get_id()))
            ExeGroup.field_num[self.__field].remove(self.__number)

            for student in self.__students:
                ExeGroup.all_students.remove(student)

            self.__students = {}
        else:
            print("Error! Cant delete in exercise_group table")

    #remove student
    def delete_student(self, student, db):
        """function delete student from group

        Args:
            db (TableDatabase): database that you want to use
            student (Student): student you want to delete
        """
        sql = """DELETE FROM exercise_group WHERE id_student = ?"""

        if db.get_conn() is not None:
            cur = db.cursor_conn()
            ExeGroup.all_students.remove(student)
            del self.__students[student]
            cur.execute(sql, (student.get_id(),))
        else:
            print("Error! Cant delete student in exercise_group table")

    def get_id(self):
        ids = []
        for student in self.__students:
            ids.append(self.__students[student])

        return ids

    def set_number(self, number):
        try:
            if number not in ExeGroup.field_num[self.__field]:
                ExeGroup.field_num[self.__field].remove(self.__number)
                self.__number = number
                ExeGroup.field_num[self.__field].append(self.__number)
            else:
                raise ValueError
        except ValueError:
            print("Number is booked")

    def set_field(self, field):
        try:
            if field in ExeGroup.field_num.keys():
                if self.__number not in ExeGroup.field_num[field]:
                    ExeGroup.field_num[self.__field].remove(self.__number)
                    self.__field = field
                    ExeGroup.field_num[self.__field].append(self.__number)
                else:
                    raise ValueError
            else:
                ExeGroup.field_num[self.__field].remove(self.__number)
                self.__field = field
                ExeGroup.field_num[self.__field] = [self.__number]
        except ValueError:
            print("Number of group in field is booked")

    def get_number(self):
        return self.__number

    def get_field(self):
        return self.__field

    def get_all_students(self):
        return self.__students

    def get_idxes(self):
        return self.__students.values()

    def get_students(self):
        return self.__students.keys()