import sqlite3

class Room(object):
    bud_num = {} #{building: [numbers]}
    id_room = 0

    @staticmethod
    def create_tab(db):
        """
        ***function must be execute after create
        building table***\n
        function create table room
        """
        sql = """CREATE TABLE IF NOT EXISTS room (
            id_room INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            id_building INTEGER NOT NULL,
            room_number INTEGER NOT NULL,
            is_deans_office INTEGER NOT NULL,
            FOREIGN KEY (id_building) REFERENCES building(id_building)
        );
        """

        if db.get_conn() is not None:
            db.create_tab(sql)
        else:
            print("Error! Cant create room table")

    @staticmethod
    def set_idx(id_room):
        Room.id_room = id_room

    @staticmethod
    def select_all(db):
        cur = db.cursor_conn()
        cur.execute("SELECT * FROM room")
        
        return cur.fetchall()

    @staticmethod
    def get_lastrowid(db):
        cur = db.cursor_conn()
        cur.execute("SELECT * FROM room")

        return cur.lastrowid

    def __init__(self, id_room = 0, building = None, number = 0, is_dean = 0):
        Room.id_room += 1
        if id_room == 0:
            self.__id_room = Room.id_room
        else:
            self.__id_room = id_room

        try:
            if building in Room.bud_num.keys():
                if number not in Room.bud_num[building]:
                    self.__number = number
                    self.__building = building
                    Room.bud_num[self.__building].append(self.__number)
                else:
                    raise ValueError
            else:
                self.__number = number
                self.__building = building
                Room.bud_num[self.__building] = [self.__number]
        except ValueError:
            print("Number in building is booked")

        if is_dean == 0 or is_dean == 1:
            self.__is_dean = is_dean
        else:
            self.__is_dean = 0

    def insert(self, db):
        sql = """INSERT INTO room(
            id_building,
            room_number,
            is_deans_office
        ) VALUES (?,?,?)
        """

        values = (
            self.__building.get_id(),
            self.__number,
            self.__is_dean
        )

        if db.get_conn() is not None:
            cur = db.cursor_conn()
            cur.execute(sql, values)
        else:
            print("Error! Cant insert in room table")

    def update(self, db):
        sql = """UPDATE room SET
        id_building = ?,
        room_number = ?,
        is_deans_office = ?
        WHERE id_room = ?
        """

        values = (
            self.__building.get_id(),
            self.__number,
            self.__is_dean,
            self.__id_room
        )

        if db.get_conn() is not None:
            cur = db.cursor_conn()
            cur.execute(sql, values)
        else:
            print("Error! Cant update in room table")

    def delete(self, db):
        sql = """DELETE FROM room WHERE id_room = ?"""

        if db.get_conn() is not None:
            cur = db.cursor_conn()
            cur.execute(sql, (self.__id_room,))
        else:
            print("Error! Cant delete room table")

    def get_id(self):
        return self.__id_room

    def get_number(self):
        return self.__number

    def get_building(self):
        return self.__building

    def get_is_dean(self):
        return self.__is_dean

    def set_id(self, id_room):
        self.__id_room = id_room

    def set_is_dean(self, is_dean):
        if is_dean == 0 or is_dean == 1:
            self.__is_dean = is_dean

    def set_number(self, number):
        try:
            if number not in Room.bud_num[self.__building]:
                Room.bud_num[self.__building].remove(self.__number)
                self.__number = number
                Room.bud_num[self.__building].append(self.__number)
            else:
                raise ValueError
        except ValueError:
            print("Number in building is booked")

    def set_building(self, building):
        try:
            if building in Room.bud_num.keys():
                if self.__number not in Room.bud_num[building]:
                    Room.bud_num[self.__building].remove(self.__number)
                    self.__building = building
                    Room.bud_num[self.__building].append(self.__number)
                else:
                    raise ValueError
            else:
                Room.bud_num[self.__building].remove(self.__number)
                self.__building = building
                Room.bud_num[self.__building] = [self.__number]
        except ValueError:
            print("Number in new building is booked")
