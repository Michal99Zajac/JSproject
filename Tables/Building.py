import sqlite3

class Building(object):
    id_bud = 0

    @staticmethod
    def set_idx(id_bud):
        Building.id_bud = id_bud

    @staticmethod
    def status_id():
        return Building.id_bud

    @staticmethod
    def create_tab(db):
        """
        function create table building
        """

        sql = """CREATE TABLE IF NOT EXISTS building (
            id_building INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            street_name TEXT NOT NULL,
            building_name TEXT NOT NULL,
            building_number INTEGER NOT NULL
        );
        """

        if db.get_conn() is not None:
            db.create_tab(sql)
        else:
            print("Error! Cant create building table")

    @staticmethod
    def select_all(db):
        cur = db.cursor_conn()
        cur.execute("SELECT * FROM building")

        return cur.fetchall()

    @staticmethod
    def get_lastrowid(db):
        cur = db.cursor_con()
        cur.execute("SELECT * FROM building")

        return cur.lastrowid

    def __init__(self, id_building = 0, street_name = '', name = '', number = ''):
        Building.id_bud += 1
        #set id_building automatically or manual
        if id_building == 0:
            self.__id_building = Building.id_bud
        else:
            self.__id_building = id_building

        self.__street_name = street_name
        self.__name = name
        self.__number = number

    def insert(self, db):
        sql = """INSERT INTO building(
            street_name,
            building_name,
            building_number
        ) VALUES (?,?,?)
        """

        values = (
            self.__street_name,
            self.__name,
            self.__number
        )

        if db.get_conn() is not None:
            cur = db.cursor_conn()
            cur.execute(sql, values)
        else:
            print("Error! Cant insert in building table")

    def update(self, db):
        sql = """UPDATE building SET
        street_name = ?,
        building_name = ?,
        building_number = ?
        WHERE id_building = ?
        """

        values = (
            self.__street_name,
            self.__name,
            self.__number,
            self.__id_building
        )

        if db.get_conn() is not None:
            cur = db.cursor_conn()
            cur.execute(sql, values)
        else:
            print("Error! Cant update in building table")

    def delete(self, db):
        sql = """DELETE FROM building WHERE id_building = ?"""

        if db.get_conn() is not None:
            cur = db.cursor_conn()
            cur.execute(sql, (self.__id_building,))
        else:
            print("Error! Cant delete in building table")

    def get_id(self):
        return self.__id_building

    def get_street_name(self):
        return self.__street_name

    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number

    def set_id(self, id_building):
        self.__id_building = id_building

    def set_street_name(self, street_name):
        self.__street_name = street_name

    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__name = number