import sqlite3

class Dean(object):
    id_dean = 0

    @staticmethod
    def set_idx(id_dean):
        Dean.id_dean = id_dean

    @staticmethod
    def status_id():
        return Dean.id_dean

    @staticmethod
    def select_all(db):
        cur = db.cursor_conn()
        cur.execute("SELECT * FROM dean")

        return cur.fetchall()

    @staticmethod
    def get_lastrowid(db):
        cur = db.cursor_conn()
        cur.execute("SELECT * FROM dean")

        return cur.lastrowid

    @staticmethod
    def create_tab(db):
        """
        function create table dean
        """

        sql = """CREATE TABLE IF NOT EXISTS dean (
            id_dean INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name TEXT NOT NULL,
            lastname TEXT NOT NULL,
            second_name TEXT,
            pesel INTEGER NOT NULL,
            email TEXT,
            place_of_residence TEXT NOT NULL
        );
        """

        if db.get_conn() is not None:
            db.create_tab(sql)
        else:
            print("Error! Cant create dean table")

    def __init__(self, id_dean = 0, name = '', lastname = '', sec_name = '', ssn = 1000, email = '', place_of_residence = ''):
        Dean.id_dean += 1
        #set id_dean automatically or manual
        if id_dean == 0:
            self.__id_dean = Dean.id_dean
        else:
            self.__id_dean = id_dean

        self.__name = name
        self.__lastname = lastname
        self.__sec_name = sec_name
        self.__ssn = ssn #social security number
        self.__email = email
        self.__place_of_residence = place_of_residence

    def insert(self, db):
        sql = """INSERT INTO dean(
            name,
            lastname,
            second_name,
            pesel,
            email,
            place_of_residence
        ) VALUES (?,?,?,?,?,?)
        """

        values = (
            self.__name,
            self.__lastname,
            self.__sec_name,
            self.__ssn,
            self.__email,
            self.__place_of_residence
        )

        if db.get_conn() is not None:
            cur = db.cursor_conn()
            cur.execute(sql, values)
        else:
            print("Error! Cant insert in dean table")

    def update(self, db):
        sql = """UPDATE dean SET
        name = ?,
        lastname = ?,
        second_name = ?,
        pesel = ?,
        email = ?,
        place_of_residence = ?
        WHERE id_dean = ?
        """

        values = (
            self.__name,
            self.__lastname,
            self.__sec_name,
            self.__ssn,
            self.__email,
            self.__place_of_residence,
            self.__id_dean
        )

        if db.get_conn() is not None:
            cur = db.cursor_conn()
            cur.execute(sql, values)
        else:
            print("Error! Cant update in dean table")

    def delete(self, db):
        sql = """DELETE FROM dean WHERE id_dean = ?"""

        if db.get_conn() is not None:
            cur = db.cursor_conn()
            cur.execute(sql, (self.__id_dean,))
        else:
            print("Error! Cant delete in dean table")

    def get_id(self):
        return self.__id_dean

    def get_name(self):
        return self.__name

    def get_lastname(self):
        return self.__lastname
    
    def get_sec_name(self):
        return self.__sec_name

    def get_ssn(self):
        return self.__ssn

    def get_email(self):
        return self.__email

    def get_place_of_residence(self):
        return self.__place_of_residence

    def set_id(self, id_dean):
        self.__id_dean = id_dean

    def set_name(self, name):
        self.__name = name

    def set_lastname(self, lastname):
        self.__lastname = lastname

    def set_sec_name(self, sec_name):
        self.__sec_name = sec_name

    def set_ssn(self, ssn):
        self.__ssn = ssn

    def set_email(self, email):
        self.__email = email

    def set_place_of_residence(self, place_of_residence):
        self.__place_of_residence = place_of_residence