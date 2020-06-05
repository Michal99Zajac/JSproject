class Subject(object):
    id_subject = 0
    group_name = {}  # {group: [name]}

    @staticmethod
    def set_idx(id_sub):
        """function set var id_subject

        Args:
            id_sub (int): new idx for class
        """
        Subject.id_subject = id_sub

    @staticmethod
    def status_id():
        """func return variable id_subject

        Returns:
            int: current id_subject in class
        """
        return Subject.id_subject

    @staticmethod
    def select_all(db):
        """func return all subjects data from db

        Args:
            db (TableDatabase): database that you want to search

        Returns:
            List: list of tuples of data
        """
        cur = db.cursor_conn()
        cur.execute("SELECT * FROM subject")

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
        cur.execute("SELECT * FROM subject")

        return cur.lastrowid

    @staticmethod
    def get_groups_id(db, data):
        """function return ids of group

        Args:
            db (TableDatabase): database that you want to search
            data (tuple): group data

        Returns:
            List: list of ids
        """

        sql = """SELECT id_subject FROM subject WHERE
        id_teacher=? AND
        id_room=? AND
        id_field_of_study=? AND
        day=? AND
        hour_start=? AND
        hour_end=? AND
        name=?
        """

        cur = db.cursor_conn()
        cur.execute(sql, data)

        return cur.fetchall()

    @staticmethod
    def create_tab(db):
        """
        ***function must be execute after create
        teacher, field_of_study, laboratory_group,
        exercise_group, year_group
        and room table***\n
        function create table subject
        """

        sql = """CREATE TABLE IF NOT EXISTS subject (
            id_subject INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            id_teacher INTEGER NOT NULL,
            id_labolatory_group INTEGER,
            id_exercise_group INTEGER,
            id_year_group INTEGER,
            id_room INTEGER,
            id_field_of_study INTEGER NOT NULL,
            day TEXT,
            hour_start TEXT,
            hour_end TEXT,
            name TEXT NOT NULL,
            FOREIGN KEY (id_teacher)
            REFERENCES teacher(id_teacher)
            ON UPDATE CASCADE
            ON DELETE CASCADE,
            FOREIGN KEY (id_labolatory_group)
            REFERENCES laboratory_group(id_labolatory_group)
            ON UPDATE CASCADE
            ON DELETE CASCADE,
            FOREIGN KEY (id_exercise_group)
            REFERENCES exercise_group(id_exercise_group)
            ON UPDATE CASCADE
            ON DELETE CASCADE,
            FOREIGN KEY (id_year_group)
            REFERENCES year_group(id_year_group)
            ON UPDATE CASCADE
            ON DELETE CASCADE,
            FOREIGN KEY (id_room)
            REFERENCES room(id_room)
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
            print("Error! Cant create subject table")

    def __init__(self, id_sub=[], teacher=None, lab_group=None, exe_group=None, year_group=None, room=None, field=None, day='', start='', end='', name=''):
        """Init Subject

        Args:
            id_sub (list, optional): id of subject. Defaults to [0,].
            teacher ([Teacher, optional): subject teacher. Defaults to None.
            lab_group (LabGroup, optional): subject lab group.
            Defaults to None.
            exe_group (ExeGroup, optional): subject exe group.
            Defaults to None.
            year_group (YearGroup, optional): subject year group.
            Defaults to None.
            room (Room, optional): subject room. Defaults to None.
            field (FieldOfStudy, optional): subject field. Defaults to None.
            day (str, optional): subject day. Defaults to ''.
            start (str, optional): hour when subject start. Defaults to ''.
            end (str, optional): hour when subject end. Defaults to ''.
            name (str, optional): subject name. Defaults to ''.
        """
        self.__lab = False
        self.__exe = False
        self.__year = False
        self.__id_sub = id_sub
        self.__teacher = teacher
        self.__room = room
        self.__field = field
        self.__day = day
        self.__start = start
        self.__end = end
        self.__group = None

        for i, group in enumerate([lab_group, exe_group, year_group]):
            if group is not None:
                self.__group = group

                if i == 0:
                    self.__lab = True
                elif i == 1:
                    self.__exe = True
                elif i == 2:
                    self.__year = True

        try:
            if self.__group in Subject.group_name.keys():
                if name not in Subject.group_name[group]:
                    self.__name = name
                    Subject.group_name[self.__group].append(self.__name)
                else:
                    ValueError
            else:
                self.__name = name
                Subject.group_name[self.__group] = [self.__name]
        except ValueError:
            print("group of subject is booked")

    # add all rows of group
    def insert(self, db):
        """function insert data to db

        Args:
        db (TableDatabase): database that you want to fill
        """

        index = Subject.get_lastrowid(db) + 1

        if self.__lab is True:
            for idx in self.__group.get_idxes():
                sql = """INSERT INTO subject(
                id_teacher,
                id_labolatory_group,
                id_room,
                day,
                hour_start,
                hour_end,
                id_field_of_study,
                name
                ) VALUES (?,?,?,?,?,?,?,?)
                """

                values = (
                    self.__teacher.get_id(),
                    idx,
                    self.__room.get_id(),
                    self.__day,
                    self.__start,
                    self.__end,
                    self.__field.get_id(),
                    self.__name
                )

                if db.get_conn() is not None:
                    cur = db.cursor_conn()
                    cur.execute(sql, values)
                else:
                    print("Error! Cant insert a lab in subject table")

                self.__id_sub.append(index)
                index += 1

        if self.__exe is True:
            for idx in self.__group.get_idxes():
                sql = """INSERT INTO subject(
                id_teacher,
                id_exercise_group,
                id_room,
                day,
                hour_start,
                hour_end,
                id_field_of_study,
                name
                ) VALUES (?,?,?,?,?,?,?,?)
                """

                values = (
                    self.__teacher.get_id(),
                    idx,
                    self.__room.get_id(),
                    self.__day,
                    self.__start,
                    self.__end,
                    self.__field.get_id(),
                    self.__name
                )

                if db.get_conn() is not None:
                    cur = db.cursor_conn()
                    cur.execute(sql, values)
                else:
                    print("Error! Cant insert a exe in subject table")

                self.__id_sub.append(index)
                index += 1

        if self.__year is True:
            for idx in self.__group.get_idxes():
                sql = """INSERT INTO subject(
                id_teacher,
                id_year_group,
                id_room,
                day,
                hour_start,
                hour_end,
                id_field_of_study,
                name
                ) VALUES (?,?,?,?,?,?,?,?)
                """

                values = (
                    self.__teacher.get_id(),
                    idx,
                    self.__room.get_id(),
                    self.__day,
                    self.__start,
                    self.__end,
                    self.__field.get_id(),
                    self.__name
                )

                if db.get_conn() is not None:
                    cur = db.cursor_conn()
                    cur.execute(sql, values)
                else:
                    print("Error! Cant insert a year in subject table")

                self.__id_sub.append(index)
                index += 1

    def update(self, db):
        """function update data to db

        Args:
            db (TableDatabase): database that you want to update
        """
        sql = """UPDATE subject SET
        id_teacher = ?,
        id_room = ?,
        day = ?,
        hour_start = ?,
        hour_end = ?,
        id_field_of_study = ?,
        name = ?
        WHERE id_subject = ?
        """

        for idx in self.__id_sub:
            values = (
                self.__teacher.get_id(),
                self.__room.get_id(),
                self.__day,
                self.__start,
                self.__end,
                self.__field.get_id(),
                self.__name,
                idx
            )

            if db.get_conn() is not None:
                cur = db.cursor_conn()
                cur.execute(sql, values)
            else:
                print("Error! Cant update in subject table")

    def delete(self, db):
        """function delete data from db

        Args:
            db (TableDatabase): database that you want to update
        """
        sql = """DELETE FROM subject WHERE
        id_teacher = ? AND
        id_room = ? AND
        id_field_of_study = ? AND
        name = ? AND
        day = ? AND
        hour_start = ? AND
        hour_end = ?
        """

        values = (
            self.__teacher.get_id(),
            self.__room.get_id(),
            self.__field.get_id(),
            self.__name,
            self.__day,
            self.__start,
            self.__end,
        )

        if db.get_conn() is not None:
            cur = db.cursor_conn()
            cur.execute(sql, values)
        else:
            print("Error! Cant delete field_of_study table")

        self.__id_sub = []

    def get_id(self):
        return self.__id_sub

    def get_name(self):
        return self.__name

    def get_teacher(self):
        return self.__teacher

    def get_room(self):
        return self.__room

    def get_day(self):
        return self.__day

    def get_start(self):
        return self.__start

    def get_end(self):
        return self.__end

    def get_field(self):
        return self.__field

    def get_group(self):
        return self.__group

    def is_lab_subject(self):
        return self.__lab

    def is_exe_subject(self):
        return self.__exe

    def is_year_subject(self):
        return self.__year

    def set_name(self, name):
        try:
            if name not in Subject.group_name[self.__group]:
                Subject.group_name[self.__group].remove(self.__name)
                self.__name = name
                Subject.group_name[self.__group].append(self.__name)
            else:
                raise ValueError
        except ValueError:
            print("Group have this subject")

    def set_teacher(self, teacher):
        self.__teacher = teacher

    def set_room(self, room):
        self.__room = room

    def set_day(self, day):
        self.__day = day

    def set_start(self, start):
        self.__start = start

    def set_end(self, end):
        self.__end = end

    def set_field(self, field):
        self.__field = field
