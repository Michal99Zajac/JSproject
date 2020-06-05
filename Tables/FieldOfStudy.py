class FieldOfStudy(object):
    id_field = 0
    dep_name = {}  # {dept:[names]}

    @staticmethod
    def set_idx(id_fie):
        """function set var id_field

        Args:
            id_field (int): new idx for class
        """
        FieldOfStudy.id_field = id_fie


    @staticmethod
    def status_id():
        """func return variable id_field

        Returns:
            int: current id_field in class
        """
        return FieldOfStudy.id_field


    @staticmethod
    def select_all(db):
        """func return all fields of study data from db

        Args:
            db (TableDatabase): database that you want to search

        Returns:
            List: list of tuples of data
        """
        cur = db.cursor_conn()
        cur.execute("SELECT * FROM field_of_study")
        rows = cur.fetchall()

        return rows


    @staticmethod
    def get_lastrowid(db):
        """function return last row id

        Args:
            db (TableDatabase): database that you want to search

        Returns:
            int: last row id
        """
        cur = db.cursor_conn()
        cur.execute("SELECT * FROM field_of_study")
        
        return cur.lastrowid


    @staticmethod
    def create_tab(db):
        """
        ***function must be execute after create
        department and deans_office_employee tables***\n
        function create table field_of_study
        """

        sql = """CREATE TABLE IF NOT EXISTS field_of_study (
            id_field_of_study INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name TEXT NOT NULL,
            id_department INTEGER NOT NULL,
            id_leader_of_field INTEGER NOT NULL,
            FOREIGN KEY (id_department) REFERENCES department(id_department)
            ON UPDATE CASCADE
            ON DELETE CASCADE,
            FOREIGN KEY (id_leader_of_field) REFERENCES deans_office_employee(id_deans_office_employee)
            ON UPDATE CASCADE
            ON DELETE CASCADE
        );
        """

        if db.get_conn() is not None:
            db.create_tab(sql)
        else:
            print("Error! Cant create field_of_study table")


    def __init__(self, id_field = 0, name = '', department = None, do_emp = None):
        """Init FieldOfStudy

        Args:
            id_field (int, optional): id of field of study. Defaults to 0.
            name (str, optional): field of study name. Defaults to ''.
            department (Department, optional): f department. Defaults to None.
            do_emp (DeansEmp, optional): field of study deans off emp. Defaults to None.

        Raises:
            ValueError: if department and name was created
        """
        FieldOfStudy.id_field += 1
        if id_field == 0:
            self.__id_field = FieldOfStudy.id_field
        else:
            self.__id_field = id_field

        try:
            if department in FieldOfStudy.dep_name.keys():
                if name not in FieldOfStudy.dep_name[department]:
                    self.__name = name
                    self.__department = department
                    FieldOfStudy.dep_name[self.__department].append(self.__name)
                else:
                    raise ValueError
            else:
                self.__name = name
                self.__department = department
                FieldOfStudy.dep_name[self.__department] = [self.__name]
        except ValueError:
            self.__name = 'NULL'
            print("Name of field of study in department is booked")
        finally:
            self.__do_emp = do_emp
        


    def insert(self, db):
        """function insert data to db

        Args:
            db (TableDatabase): database that you want to fill
        """
        sql = """INSERT INTO field_of_study(
            name,
            id_department,
            id_leader_of_field
        ) VALUES (?,?,?)
        """

        try:
            dept_id = self.__department.get_id()
        except AttributeError:
            dept_id = "NULL"

        try:
            do_emp_id = self.__do_emp.get_id()
        except AttributeError:
            do_emp_id = "NULL"

        values = (
            self.__name,
            dept_id,
            do_emp_id
        )

        if db.get_conn() is not None:    
            cur = db.cursor_conn()
            cur.execute(sql, values)
        else:
            print("Error! Cant insert in field_of_study table")


    def update(self, db):
        """function update data to db

        Args:
            db (TableDatabase): database that you want to update
        """
        sql = """UPDATE field_of_study SET
        name = ?,
        id_department = ?,
        id_leader_of_field = ?
        WHERE id_field_of_study = ?
        """

        try:
            dept_id = self.__department.get_id()
        except AttributeError:
            dept_id = "NULL"

        try:
            do_emp_id = self.__do_emp.get_id()
        except AttributeError:
            do_emp_id = "NULL"

        values = (
            self.__name,
            dept_id,
            do_emp_id,
            self.__id_field
        )

        if db.get_conn() is not None:   
            cur = db.cursor_conn()
            cur.execute(sql, values)
        else:
            print("Error! Cant update in field_of_study table")


    def delete(self, db):
        """function delete data to db

        Args:
            db (TableDatabase): database that you want to update
        """
        sql = """DELETE FROM field_of_study WHERE id_field_of_study = ?"""

        if db.get_conn() is not None:
            cur = db.cursor_conn()
            cur.execute(sql, (self.__id_field,))
        else:
            print("Error! Cant delete field_of_study table")


    def get_id(self):
        return self.__id_field


    def get_name(self):
        return self.__name


    def get_department(self):
        return self.__department


    def get_leader(self):
        return self.__do_emp


    def set_name(self, name):
        try:
            if name not in FieldOfStudy.dep_name[self.__department]:
                FieldOfStudy.dep_name[self.__department].remove(self.__name)
                self.__name = name
                FieldOfStudy.dep_name[self.__department].append(self.__name)
            else:
                raise ValueError
        except ValueError:
            print("Name in field_of_study is booked")


    def set_department(self, department):
        try:
            if department in FieldOfStudy.dep_name.keys():
                if self.__name not in FieldOfStudy.dep_name[department]:
                    FieldOfStudy.dep_name[self.__department].remove(self.__name)
                    self.__department = department
                    FieldOfStudy.dep_name[self.__department].append(self.__name)
                else:
                    raise ValueError
            else:
                FieldOfStudy.dep_name[self.__department].remove(self.__name)
                self.__department = department
                FieldOfStudy.dep_name[self.__department] = [self.__name]
        except ValueError:
            print("Name of field of study in new department is booked")


    def set_leader(self, do_emp):
        self.__do_emp = do_emp
        