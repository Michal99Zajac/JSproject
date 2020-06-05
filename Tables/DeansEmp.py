class DeansEmp(object):
    id_emp = 0

    @staticmethod
    def set_idx(id_emp):
        """function set var id_emp

        Args:
            id_emp (int): new idx for class
        """
        DeansEmp.id_emp = id_emp

    @staticmethod
    def status_id():
        """func return variable id_emp

        Returns:
            int: [description]
        """
        return DeansEmp.id_emp

    @staticmethod
    def select_all(db):
        """func return all deans office employees
        data from db

        Args:
            db (TableDatabase): database that you want to search

        Returns:
            List: list of tuples of data
        """
        cur = db.cursor_conn()
        cur.execute("SELECT * FROM deans_office_employee")

        return cur.fetchall()

    @staticmethod
    def get_lastrowid(db):
        """function return last row id

        Args:
            db (TableDatabase): database that you want to search

        Returns:
            [int]: last row id
        """
        cur = db.cursor_conn()
        cur.execute("SELECT * FROM deans_office_employee")

        return cur.lastrowid

    @staticmethod
    def create_tab(db):
        """
        ***function must be execute after create
        department table***\n
        function create table deans_office_employee
        """

        sql = """CREATE TABLE IF NOT EXISTS deans_office_employee (
            id_deans_office_employee INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name TEXT NOT NULL,
            second_name TEXT,
            lastname TEXT NOT NULL,
            pesel INTEGER NOT NULL,
            email TEXT,
            id_department INTEGER NOT NULL,
            FOREIGN KEY (id_department) REFERENCES department(id_department)
            ON UPDATE CASCADE
            ON DELETE CASCADE
        );
        """

        if db.get_conn() is not None:
            db.create_tab(sql)
        else:
            print("Error! Cant create deans_office_employee table")

    def __init__(self, id_emp = 0, name = '', sec_name = '', lastname = '', ssn = 1000, email = '', department = None):
        """Init Deans Office Employee

        Args:
            id_emp (int, optional): if of deans emp. Defaults to 0.
            name (str, optional): deans emp name. Defaults to ''.
            sec_name (str, optional): deans emp second name. Defaults to ''.
            lastname (str, optional): deans emp lastname. Defaults to ''.
            ssn (int, optional): deans emp ssn. Defaults to 1000.
            email (str, optional): deans emp email. Defaults to ''.
            department ([Department], optional): deans emp department. Defaults to None.
        """
        DeansEmp.id_emp += 1
        #set id_student automatically or manual
        if id_emp == 0:
            self.__id_emp = DeansEmp.id_emp
        else:
            self.__id_emp = id_emp

        self.__name = name
        self.__sec_name = sec_name
        self.__lastname = lastname
        self.__ssn = ssn
        self.__email = email
        self.__department = department

    def insert(self, db):
        """function insert data to db

        Args:
            db (TableDatabase): database that you want to fill
        """
        sql = """INSERT INTO deans_office_employee(
            name,
            second_name,
            lastname,
            pesel,
            email,
            id_department
        ) VALUES (?,?,?,?,?,?)
        """

        try:
            department_id = self.__department.get_id()
        except AttributeError:
            department_id = "NULL"
        
        values = (
            self.__name,
            self.__sec_name,
            self.__lastname,
            self.__ssn,
            self.__email,
            department_id
        )

        if db.get_conn() is not None:
            cur = db.cursor_conn()
            cur.execute(sql, values)
        else:
            print("Error! Cant insert in deans_office_employee table")

    def update(self, db):
        """function update data to db

        Args:
            db (TableDatabase): database that you want to update
        """
        sql = """UPDATE deans_office_employee SET
        name = ?,
        second_name = ?,
        lastname = ?,
        pesel = ?,
        email = ?,
        id_department = ?
        WHERE id_deans_office_employee = ?
        """

        try:
            department_id = self.__department.get_id()
        except AttributeError:
            department_id = "NULL"

        values = (
            self.__name,
            self.__sec_name,
            self.__lastname,
            self.__ssn,
            self.__email,
            department_id,
            self.__id_emp
        )

        if db.get_conn() is not None:   
            cur = db.cursor_conn()
            cur.execute(sql, values)
        else:
            print("Error! Cant update in deans_office_employee table")

    def delete(self, db):
        """function delete data to db

        Args:
            db (TableDatabase): database that you want to update
        """
        sql = """
        DELETE FROM deans_office_employee WHERE
        id_deans_office_employee = ?"""

        if db.get_conn() is not None:
            cur = db.cursor_conn()
            cur.execute(sql, (self.__id_emp,))
        else:
            print("Error! Cant delete in deans_office_employee table")

    def get_id(self):
        return self.__id_emp

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

    def get_department(self):
        return self.__department

    def set_id(self, id_emp):
        self.__id_emp = id_emp

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

    def set_department(self, department):
        self.__department = department
