class Student(object):
    id_std = 0

    @staticmethod
    def set_idx(id_std):
        """function set var id_std

        Args:
            id_std (int): new idx for class
        """
        Student.id_std = id_std

    @staticmethod
    def status_id():
        """func return variable id_std

        Returns:
            int: current id_std in class
        """
        return Student.id_std

    @staticmethod
    def select_all(db):
        """func return all students data from db

        Args:
            db (TableDatabase): database that you want to search

        Returns:
            List: list of tuples of data
        """
        cur = db.cursor_conn()
        cur.execute("SELECT * FROM student")

        return cur.fetchall()

    @staticmethod
    def get_lastrowid(db):
        """function return last row id

        Args:
            db (TableDatabase): database that you want to search

        Returns:
            int: last row id
        """
        cur = db.cursor_conn()
        cur.execute("SELECT * FROM student")

        return cur.lastrowid

    @staticmethod
    def create_tab(db):
        """
        ***function must be execute after create
        field_of_study table***\n
        function create table student
        """

        sql = """CREATE TABLE IF NOT EXISTS student (
            id_student INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name TEXT NOT NULL,
            second_name TEXT NOT NULL,
            lastname TEXT NOT NULL,
            pesel INTEGER NOT NULL,
            email TEXT,
            id_field_of_study INTEGER NOT NULL,
            place_of_residence TEXT NOT NULL,
            FOREIGN KEY (id_field_of_study) REFERENCES
            field_of_study(id_field_of_study)
            ON UPDATE CASCADE
            ON DELETE CASCADE
        );
        """
        if db.get_conn() is not None:
            db.create_tab(sql)
        else:
            print("Error! Cant create student table")

    def __init__(self, id_student=0, name='', sec_name='', lastname='', ssn=1000, email='', field_of_study=None, place_of_residence=''):
        """Init Student

        Args:
            id_student (int, optional): id of student. Defaults to 0.
            name (str, optional): student name. Defaults to ''.
            sec_name (str, optional): student second name. Defaults to ''.
            lastname (str, optional): student lastname. Defaults to ''.
            ssn (int, optional): student ssn. Defaults to 1000.
            email (str, optional): student email. Defaults to ''.
            field_of_study (FieldOfStudy, optional): student field of study.
            Defaults to None.
            place_of_residence (str, optional): student place of resid.
            Defaults to ''.
        """
        Student.id_std += 1
        # set id_student automatically or manual
        if id_student == 0:
            self.__id_student = Student.id_std
        else:
            self.__id_student = id_student

        self.__name = name
        self.__sec_name = sec_name
        self.__lastname = lastname
        self.__ssn = ssn  # social security number
        self.__email = email
        self.__field_of_study = field_of_study
        self.__place_of_residence = place_of_residence

    def insert(self, db):
        """function insert data to db

        Args:
            db (TableDatabase): database that you want to fill
        """
        sql = """INSERT INTO student(
            name,
            second_name,
            lastname,
            pesel,
            email,
            id_field_of_study,
            place_of_residence
        ) VALUES (?,?,?,?,?,?,?)
        """

        try:
            field_id = self.__field_of_study.get_id()
        except AttributeError:
            field_id = "NULL"

        values = (
            self.__name,
            self.__sec_name,
            self.__lastname,
            self.__ssn,
            self.__email,
            field_id,
            self.__place_of_residence
            )

        if db.get_conn() is not None:
            cur = db.cursor_conn()
            cur.execute(sql, values)
        else:
            print("Error! Cant insert in student table")

    def update(self, db):
        """function update data to db

        Args:
            db (TableDatabase): database that you want to update
        """
        sql = """UPDATE student SET
        name = ?,
        second_name = ?,
        lastname = ?,
        pesel = ?,
        email = ?,
        id_field_of_study = ?,
        place_of_residence = ?
        WHERE id_student = ?
        """

        try:
            field_id = self.__field_of_study.get_id()
        except AttributeError:
            field_id = "NULL"

        values = (
            self.__name,
            self.__sec_name,
            self.__lastname,
            self.__ssn,
            self.__email,
            field_id,
            self.__place_of_residence,
            self.__id_student
            )

        if db.get_conn() is not None:
            cur = db.cursor_conn()
            cur.execute(sql, values)
        else:
            print("Error! Cant update in student table")

    def delete(self, db):
        """function delete data to db

        Args:
            db (TableDatabase): database that you want to update
        """
        sql = """DELETE FROM student WHERE id_student = ?"""

        if db.get_conn() is not None:
            cur = db.cursor_conn()
            cur.execute(sql, (self.__id_student,))
        else:
            print("Error! Cant delete in student table")

    def get_id(self):
        return self.__id_student

    def get_name(self):
        return self.__name

    def get_sec_name(self):
        return self.__sec_name

    def get_lastname(self):
        return self.__lastname

    def get_ssn(self):
        return self.__ssn

    def get_email(self):
        return self.__email

    def get_id_field_of_study(self):
        return self.__field_of_study.get_id()

    def get_field_of_study(self):
        return self.__field_of_study

    def get_place_of_residence(self):
        return self.__place_of_residence

    def set_id(self, id_student):
        self.__id_student = id_student

    def set_name(self, name):
        self.__name = name

    def set_sec_name(self, sec_name):
        self.__sec_name = sec_name

    def set_lastname(self, lastname):
        self.__lastname = lastname

    def set_ssn(self, ssn):
        self.__ssn = ssn

    def set_email(self, email):
        self.__email = email

    def set_place_of_residence(self, place_of_residence):
        self.__place_of_residence = place_of_residence

    def set_field_of_study(self, field_of_study):
        self.__field_of_study = field_of_study
