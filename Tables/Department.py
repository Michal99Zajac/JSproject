import sqlite3

class Department(object):
    id_dept = 0
    buildings = []
    deans = []

    @staticmethod
    def set_idx(id_dept):
        Department.id_dept = id_dept

    @staticmethod
    def status_id():
        return Department.id_dept

    @staticmethod
    def select_all(db):
        cur = db.cursor_conn()
        cur.execute("SELECT * FROM department")

        return cur.fetchall()

    @staticmethod
    def get_lastrowid(db):
        cur = db.cursor_conn()
        cur.execute("SELECT * FROM department")

        return cur.lastrowid

    @staticmethod
    def create_tab(db):
        """
        ***function must be execute after create
        building and dean table***\n
        function create table department
        """

        sql = """CREATE TABLE IF NOT EXISTS department (
            id_department INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            id_building INTEGER NOT NULL,
            deans_office_start TEXT,
            deans_office_stop TEXT,
            id_dean INTEGER NOT NULL,
            FOREIGN KEY (id_building) REFERENCES building(id_building),
            FOREIGN KEY (id_dean) REFERENCES dean(id_dean)
            ON UPDATE CASCADE
            ON DELETE CASCADE
        );
        """

        if db.get_conn() is not None:
            db.create_tab(sql)
        else:
            print("Error! Cant create department table")

    def __init__(self, id_dept = 0, building = None, off_start = '', off_stop = '', dean = None):
        Department.id_dept += 1
        #set id_student automatically or manual
        if id_dept == 0:
            self.__id_dept = Department.id_dept
        else:
            self.__id_dept = id_dept

        try:
            if building not in Department.buildings and dean not in Department.deans:
                self.__building = building
                self.__dean = dean
                Department.buildings.append(self.__building)
                Department.deans.append(self.__dean)
            else:
                raise ValueError
        except ValueError:
            Department.id_dept -= 1
            print("Error! Building or Dean is booked")

        self.__off_start = off_start
        self.__off_stop = off_stop

    def insert(self, db):
        sql = """INSERT INTO department(
            id_building,
            deans_office_start,
            deans_office_stop,
            id_dean
        ) VALUES (?,?,?,?)
        """

        values = (
            self.__building.get_id(),
            self.__off_start,
            self.__off_stop,
            self.__dean.get_id()
        )

        if db.get_conn() is not None:
            cur = db.cursor_conn()
            cur.execute(sql, values)
        else:
            print("Error! Cant insert in department table")

    def update(self, db):
        sql = """UPDATE department SET
        id_building = ?,
        deans_office_start = ?,
        deans_office_stop = ?,
        id_dean = ?
        WHERE id_department = ?
        """

        values = (
            self.__building.get_id(),
            self.__off_start,
            self.__off_stop,
            self.__dean.get_id(),
            self.__id_dept
        )

        if db.get_conn() is not None:
            cur = db.cursor_conn()
            cur.execute(sql, values)
        else:
            print("Error! Cant update in department table")

    def delete(self, db):
        sql = """DELETE FROM department WHERE id_department"""

        if db.get_conn() is not None:
            cur = db.cursor_conn()
            cur.execute(sql, (self.__id_dept,))
        else:
            print("Error! Cant delete in department table")

    def get_id(self):
        return self.__id_dept

    def get_building(self):
        return self.__building

    def get_dean(self):
        return self.__dean

    def get_off_start(self):
        return self.__off_start

    def get_off_stop(self):
        return self.__off_stop

    def set_id(self, id_dept):
        self.__id_dept = id_dept

    def set_off_start(self, off_start):
        self.__off_start = off_start
    
    def set_off_stop(self, off_stop):
        self.__off_stop = off_stop

    def set_building(self, building):
        if building not in Department.buildings:
            Department.buildings.remove(self.__building)
            self.__building = building
            Department.buildings.append(self.__building)

    def set_dean(self, dean):
        if dean not in Department.deans:
            Department.deans.remove(self.__dean)
            self.__dean = dean
            Department.deans.append(self.__dean)

