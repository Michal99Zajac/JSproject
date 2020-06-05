class LabGroup(object):
    field_num = {}  # {field: [num]}
    all_students = []

    @staticmethod
    def create_tab(db):
        """
        ***function must be execute after create
        student and field_of_study table***\n
        function create table laboratory_group
        """

        sql = """CREATE TABLE IF NOT EXISTS laboratory_group (
            id_labolatory_group INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            labolatory_group_number INTEGER NOT NULL,
            id_student INTEGER,
            id_field_of_study INTEGER NOT NULL,
            FOREIGN KEY (id_student) REFERENCES student(id_student)
            ON UPDATE CASCADE
            ON DELETE CASCADE,
            FOREIGN KEY (id_field_of_study)
            REFERENCES field_of_study(id_field_of_study)
            ON UPDATE CASCADE
            ON DELETE CASCADE
        );
        """

        if db.get_conn() is not None:
            db.create_tab(sql)
        else:
            print("Error! Cant create laboratory_group table")

    @staticmethod
    def select_all(db):
        """func return all lab group data from db

        Args:
            db (TableDatabase): database that you want to search

        Returns:
            List: list of tuples of data
        """
        cur = db.cursor_conn()
        cur.execute("""SELECT * FROM laboratory_group
            ORDER BY labolatory_group_number""")
        rows = cur.fetchall()

        return rows

    def __init__(self, number=10, field=None, students={}):
        """Init LabGroup

        Args:
            number (int, optional): lab group number. Defaults to 10.
            field (FieldOfStudy, optional): lab group field of std.
            Defaults to None.
            students (dict, optional): {student obj: id}. Defaults to {}.

        Raises:
            ValueError: if number and field was created
        """
        self.__number = None
        self.__field = None  # object field_of_study
        try:
            if field in LabGroup.field_num.keys():
                if number not in LabGroup.field_num[field]:
                    self.__number = number
                    self.__field = field
                    LabGroup.field_num[self.__field].append(self.__number)
                else:
                    raise ValueError
            else:
                self.__number = number
                self.__field = field
                LabGroup.field_num[self.__field] = [self.__number]
        except ValueError:
            print("Number and field_od_study in group is booked")

        self.__students = students  # {student: id_lab}

        for student in self.__students:
            LabGroup.all_students.append(student)

    def show_group(self, db):
        """func return lab group data from db

        Args:
            db (TableDatabase): database that you want to search

        Returns:
            List: list of tuples of data
        """
        sql = """SELECT * FROM laboratory_group
        WHERE labolatory_group_number = ? AND id_field_of_study = ?
        """

        cur = db.cursor_conn()
        cur.execute(sql, (self.__number, self.__field.get_id()))
        rows = cur.fetchall()

        return rows

    # add student
    def insert(self, student, db):
        """function insert student to group

        Args:
            db (TableDatabase): database that you want to search
            student (Student): student you want to insert
        """
        sql = """INSERT INTO laboratory_group(
            labolatory_group_number,
            id_student,
            id_field_of_study
        ) VALUES (?,?,?)
        """

        LabGroup.all_students.append(student)

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
            print("Error! Cant insert in laboratory_group table")

        self.__students[student] = cur.lastrowid

    def update(self, db):
        """function update data to db

        Args:
            db (TableDatabase): database that you want to update
        """
        sql = """UPDATE laboratory_group SET
        labolatory_group_number = ?,
        id_field_of_study = ?
        WHERE id_labolatory_group = ?
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
                print("Error! Cant update in laboratory_group table")

    # remove group
    def delete(self, db):
        """function delete data from db

        Args:
            db (TableDatabase): database that you want to update
        """
        sql = """DELETE FROM laboratory_group WHERE labolatory_group_number = ?
        AND id_field_of_study = ?"""

        if db.get_conn() is not None:
            cur = db.cursor_conn()
            cur.execute(sql, (self.__number, self.__field.get_id()))
            LabGroup.field_num[self.__field].remove(self.__number)

            for student in self.__students:
                LabGroup.all_students.remove(student)

            self.__students = {}
        else:
            print("Error! Cant delete in laboratory_group table")

    # remove student
    def delete_student(self, student, db):
        """function delete student from group

        Args:
            db (TableDatabase): database that you want to use
            student (Student): student you want to delete
        """
        sql = """DELETE FROM laboratory_group WHERE id_student = ?"""

        if db.get_conn() is not None:
            cur = db.cursor_conn()
            LabGroup.all_students.remove(student)
            del self.__students[student]
            cur.execute(sql, (student.get_id(),))
        else:
            print("Error! Cant delete student in laboratory_group table")

    def get_id(self):
        ids = []
        for student in self.__students:
            ids.append(self.__students[student])

        return ids

    def set_number(self, number):
        try:
            if number not in LabGroup.field_num[self.__field]:
                LabGroup.field_num[self.__field].remove(self.__number)
                self.__number = number
                LabGroup.field_num[self.__field].append(self.__number)
            else:
                raise ValueError
        except ValueError:
            print("Number is booked")

    def set_field(self, field):
        try:
            if field in LabGroup.field_num.keys():
                if self.__number not in LabGroup.field_num[field]:
                    LabGroup.field_num[self.__field].remove(self.__number)
                    self.__field = field
                    LabGroup.field_num[self.__field].append(self.__number)
                else:
                    raise ValueError
            else:
                LabGroup.field_num[self.__field].remove(self.__number)
                self.__field = field
                LabGroup.field_num[self.__field] = [self.__number]
        except ValueError:
            print("Number of group in field is booked")

    def get_number(self):
        return self.__number

    def get_field(self):
        return self.__field

    def get_idxes(self):
        return self.__students.values()

    def get_students(self):
        return self.__students.keys()

    def get_all_students(self):
        return self.__students
