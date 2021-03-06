class Teacher(object):
    id_tea = 0
    acd_degrees = {'dr', 'mgr', 'prof', }

    @staticmethod
    def set_idx(id_tea):
        """function set var id_tea

        Args:
            id_tea (int): new idx for class
        """
        Teacher.id_tea = id_tea

    @staticmethod
    def status_id():
        """func return variable id_tea

        Returns:
            int: current id_tea in class
        """
        return Teacher.id_tea

    @staticmethod
    def select_all(db):
        """func return all teachers data from db

        Args:
            db (TableDatabase): database that you want to search

        Returns:
            List: list of tuples of data
        """
        cur = db.cursor_conn()
        cur.execute("SELECT * FROM teacher")

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
        cur.execute("SELECT * FROM teacher")

        return cur.lastrowid

    @staticmethod
    def create_tab(db):
        """
        ***function must be execute after create
        department table***\n
        function create table teacher
        """

        sql = """CREATE TABLE IF NOT EXISTS teacher (
            id_teacher INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name TEXT NOT NULL,
            second_name TEXT,
            lastname TEXT NOT NULL,
            pesel INTEGER NOT NULL,
            email TEXT,
            academic_degree TEXT NOT NULL,
            id_department INTEGER NOT NULL,
            place_of_residence TEXT NOT NULL,
            FOREIGN KEY (id_department) REFERENCES department(id_department)
            ON UPDATE CASCADE
            ON DELETE CASCADE
        );
        """

        if db.get_conn() is not None:
            db.create_tab(sql)
        else:
            print("Error! Cant create teacher table")

    def __init__(self, id_teacher=0, name='', sec_name='', lastname='', ssn=1000, email='', acd_degree='', department=None, place_of_residence=''):
        """Init Teacher

        Args:
            id_teacher (int, optional): id of teacher. Defaults to 0.
            name (str, optional): [teacher name. Defaults to ''.
            sec_name (str, optional): teacher second name. Defaults to ''.
            lastname (str, optional): teacher lastname. Defaults to ''.
            ssn (int, optional): teacher ssn. Defaults to 1000.
            email (str, optional): teacher email. Defaults to ''.
            acd_degree (str, optional): teacher acd. Defaults to ''.
            department ([Department, optional): teacher dept. Defaults to None.
            place_of_residence (str, optional): teacher place of residence.
            Defaults to ''.
        """
        Teacher.id_tea += 1
        # set id_student automatically or manual
        if id_teacher == 0:
            self.__id_teacher = Teacher.id_tea
        else:
            self.__id_teacher = id_teacher

        self.__name = name
        self.__sec_name = sec_name
        self.__lastname = lastname
        self.__ssn = ssn
        self.__email = email
        self.__department = department
        self.__place_of_residenece = place_of_residence

        if acd_degree in Teacher.acd_degrees:
            self.__acd_degree = acd_degree
        else:
            self.__acd_degree = 'acd'  # deegre const

    def insert(self, db):
        """function insert data to db

        Args:
            db (TableDatabase): database that you want to fill
        """
        sql = """INSERT INTO teacher(
            name,
            second_name,
            lastname,
            pesel,
            email,
            academic_degree,
            id_department,
            place_of_residence
        ) VALUES (?,?,?,?,?,?,?,?)
        """

        try:
            dept_id = self.__department.get_id()
        except AttributeError:
            dept_id = "NULL"

        values = (
            self.__name,
            self.__sec_name,
            self.__lastname,
            self.__ssn,
            self.__email,
            self.__acd_degree,
            dept_id,
            self.__place_of_residenece
        )

        if db.get_conn() is not None:
            cur = db.cursor_conn()
            cur.execute(sql, values)
        else:
            print("Error! Cant insert in teacher table")

    def update(self, db):
        """function update data to db

        Args:
            db (TableDatabase): database that you want to update
        """
        sql = """UPDATE teacher SET
        name = ?,
        second_name = ?,
        lastname = ?,
        pesel = ?,
        email = ?,
        academic_degree = ?,
        id_department = ?,
        place_of_residence = ?
        WHERE id_teacher = ?
        """

        try:
            dept_id = self.__department.get_id()
        except AttributeError:
            dept_id = "NULL"

        values = (
            self.__name,
            self.__sec_name,
            self.__lastname,
            self.__ssn,
            self.__email,
            self.__acd_degree,
            dept_id,
            self.__place_of_residenece,
            self.__id_teacher
        )

        if db.get_conn() is not None:
            cur = db.cursor_conn()
            cur.execute(sql, values)
        else:
            print("Error! Cant update in teacher table")

    def delete(self, db):
        """function delete data from db

        Args:
            db (TableDatabase): database that you want to update
        """
        sql = """DELETE FROM teacher WHERE id_teacher = ?"""

        if db.get_conn() is not None:
            cur = db.cursor_conn()
            cur.execute(sql, (self.__id_teacher,))
        else:
            print("Error! Cant delete in teacher table")

    def get_id(self):
        return self.__id_teacher

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

    def get_acd_degree(self):
        return self.__acd_degree

    def get_place_of_residence(self):
        return self.__place_of_residenece

    def get_department(self):
        return self.__department

    def set_id(self, id_tea):
        self.__id_teacher = id_tea

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

    def set_acd_degree(self, acd_degree):
        if acd_degree in Teacher.acd_degrees:
            self.__acd_degree = acd_degree

    def set_department(self, department):
        self.__department = department

    def set_place_od_residence(self, place_of_residence):
        self.__place_of_residenece = place_of_residence
