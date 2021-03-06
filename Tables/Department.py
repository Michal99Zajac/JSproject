class Department(object):
    id_dept = 0
    buildings = []
    deans = []

    @staticmethod
    def set_idx(id_dept):
        """function set var id_dept

        Args:
            id_dept (int): new idx for class
        """
        Department.id_dept = id_dept

    @staticmethod
    def status_id():
        """func return variable id_dept

        Returns:
            int: current id_dept in class
        """
        return Department.id_dept

    @staticmethod
    def select_all(db):
        """func return all departments data from db

        Args:
            db (TableDatabase): database that you want to search

        Returns:
            List: list of tuples of data
        """
        cur = db.cursor_conn()
        cur.execute("SELECT * FROM department")

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
            name TEXT,
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

    def __init__(self, id_dept=0, building=None, name='', off_start='', off_stop='', dean=None):
        """Init Department

        Args:
            id_dept (int, optional): id of department. Defaults to 0.
            building (Building, optional): department building.
            Defaults to None.
            name (str, optional): department name. Defaults to ''.
            off_start (str, optional): department office start. Defaults to ''.
            off_stop (str, optional): department office stop. Defaults to ''.
            dean (Dean, optional): department dean. Defaults to None.
        """
        Department.id_dept += 1
        # set id_student automatically or manual
        if id_dept == 0:
            self.__id_dept = Department.id_dept
        else:
            self.__id_dept = id_dept

        self.__building = building
        self.__dean = dean
        Department.buildings.append(self.__building)
        Department.deans.append(self.__dean)

        self.__name = name
        self.__off_start = off_start
        self.__off_stop = off_stop

    def insert(self, db):
        """function insert data to db

        Args:
            db (TableDatabase): database that you want to fill
        """
        sql = """INSERT INTO department(
            id_building,
            name,
            deans_office_start,
            deans_office_stop,
            id_dean
        ) VALUES (?,?,?,?,?)
        """

        try:
            building_id = self.__building.get_id()
        except AttributeError:
            building_id = "NULL"

        try:
            dean_id = self.__dean.get_id()
        except AttributeError:
            dean_id = "NULL"

        values = (
            building_id,
            self.__name,
            self.__off_start,
            self.__off_stop,
            dean_id
        )

        if db.get_conn() is not None:
            cur = db.cursor_conn()
            cur.execute(sql, values)
        else:
            print("Error! Cant insert in department table")

    def update(self, db):
        """function update data to db

        Args:
            db (TableDatabase): database that you want to update
        """
        sql = """UPDATE department SET
        id_building = ?,
        name = ?,
        deans_office_start = ?,
        deans_office_stop = ?,
        id_dean = ?
        WHERE id_department = ?
        """

        try:
            dean = self.__dean.get_id()
        except AttributeError:
            dean = "NULL"

        try:
            building = self.__building.get_id()
        except AttributeError:
            building = "NULL"

        values = (
            building,
            self.__name,
            self.__off_start,
            self.__off_stop,
            dean,
            self.__id_dept
        )

        if db.get_conn() is not None:
            cur = db.cursor_conn()
            cur.execute(sql, values)
        else:
            print("Error! Cant update in department table")

    def delete(self, db):
        """function delete data from db

        Args:
            db (TableDatabase): database that you want to update
        """
        sql = """DELETE FROM department WHERE id_department = ?"""

        Department.buildings.remove(self.__building)
        Department.deans.remove(self.__dean)

        if db.get_conn() is not None:
            cur = db.cursor_conn()
            cur.execute(sql, (self.__id_dept,))
        else:
            print("Error! Cant delete in department table")

    def get_id(self):
        return self.__id_dept

    def get_building(self):
        return self.__building

    def get_name(self):
        return self.__name

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

    def set_name(self, name):
        self.__name = name

    def set_building(self, building):
        Department.buildings.remove(self.__building)
        self.__building = building
        Department.buildings.append(self.__building)

    def set_dean(self, dean):
        Department.deans.remove(self.__dean)
        self.__dean = dean
        Department.deans.append(self.__dean)
