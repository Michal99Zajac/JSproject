import tkinter as tk

from Tables.Subject import Subject

from tk_extension.multilistBox import MultiListBox

class SubjectPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.columnconfigure([x for x in range(2)], minsize=875)
        self.rowconfigure([x for x in range(4)], minsize=225)
        self.controller = controller

        self.year_button()
        self.exe_button()
        self.lab_button()
        self.return_button()


    def year_button(self):
        year_btn = tk.Button(
            master=self,
            text="Show Year Subject",
            command=lambda : self.controller.show_frame("YearSubjectPage"),
            font=self.controller.normal_font,
        )
        year_btn.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)


    def exe_button(self):
        exe_btn = tk.Button(
            master=self,
            text="Show Exe Subject",
            command=lambda : self.controller.show_frame("ExeSubjectPage"),
            font=self.controller.normal_font,
        )
        exe_btn.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)


    def lab_button(self):
        lab_btn = tk.Button(
            master=self,
            text="Show Lab Subject",
            command=lambda : self.controller.show_frame("LabSubjectPage"),
            font=self.controller.normal_font,
        )
        lab_btn.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)


    def return_button(self):
        return_btn = tk.Button(
            self,
            text="Home",
            command=lambda : self.controller.show_frame("StartPage"),
            font=self.controller.normal_font,
        )
        return_btn.grid(row=3, column=0, sticky="nsew", padx=5, pady=5)
        

class YearSubjectPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.columnconfigure([x for x in range(7)], minsize=250)
        self.rowconfigure([x for x in range(9)], minsize=100)
        self.controller = controller
        self.main_label()

        self.subject_listbox()
        self.refresh_button()
        self.buttons()


    def main_label(self):
        label = tk.Label(
            master=self,
            text="Year Subjects",
            font=self.controller.title_font
        )
        label.grid(row = 0, column = 6, sticky="nsew", padx=5, pady=5)

    
    def buttons(self):
        #Return Home Page
        btn_home = tk.Button(
            self,
            text="Home",
            command=lambda : self.controller.show_frame("StartPage"),
            font=self.controller.normal_font,
        )
        btn_home.grid(row=3, column=6, sticky="nsew", padx=5, pady=5)
        #Create Year Subject
        btn_create = tk.Button(
            self,
            text="Create Subject",
            command=lambda : self.create_subject(),
            font=self.controller.normal_font,
        )
        btn_create.grid(row=1, column=6, sticky="nsew", padx=5, pady=5)
        #Delete Year Subject
        btn_delete = tk.Button(
            self,
            text="Delete Subject",
            command=lambda : self.delete_subject(),
            font=self.controller.normal_font,
        )
        btn_delete.grid(row=2, column=6, sticky="nsew", padx=5, pady=5)
        #Return button
        btn_return = tk.Button(
            self,
            text="Return",
            command=lambda : self.controller.show_frame("SubjectPage"),
            font=self.controller.normal_font,
        )
        btn_return.grid(row=4, column=6, sticky="nsew", padx=5, pady=5)


    def subject_listbox(self):

        data = [
            ('name', 10),
            ('teacher', 10),
            ('room', 5),
            ('building', 10), #from room
            ('field', 10),
            ('department', 10), #from field
            ('day', 10),
            ('start', 5),
            ('stop', 5),
            ('group number', 5)
        ]

        self.list_subjects = MultiListBox(master=self, data=data)
        self.refresh()
        self.list_subjects.grid(row=0, column=0, columnspan=6, rowspan=9, sticky="nswe", padx=5, pady=5)

    
    def create_subject(self):
        self.controller.show_frame("CreateYearSubjectPage")


    def delete_subject(self):
        idx = self.list_subjects.index(tk.ACTIVE)
        del_subject = self.year_subjects()[idx]

        del_subject.delete(self.controller.db)
        self.controller.db.commit_conn()
        self.controller.subjects.remove(del_subject)

        del del_subject

        self.restart()


    def refresh_button(self):
        btn_refresh = tk.Button(
            master=self,
            text="refresh",
            command=lambda : self.restart(),
            font=self.controller.normal_font,
        )
        btn_refresh.grid(row=8, column=6, sticky="nsew", padx=5, pady=5)


    def restart(self):
        self.refresh()
        self.controller.show_frame("YearSubjectPage")


    def refresh(self):
        self.list_subjects.delete(0, tk.END)
        subjects = self.year_subjects()
        for i, subject in enumerate(subjects):
            try:
                teacher = subject.get_teacher().get_name() + " " + subject.get_teacher().get_lastname()
            except AttributeError:
                teacher = "NULL"

            try:
                room = subject.get_room().get_number()
                building = subject.get_room().get_building().get_name()
            except AttributeError:
                room = "NULL"
                building = "NULL"

            try:
                field = subject.get_field().get_name()
                department = subject.get_field().get_department().get_name()
            except AttributeError:
                field = "NULL"
                department = "NULL"

            try:
                group = subject.get_group().get_number()
            except AttributeError:
                group = "NULL"


            output = (
                subject.get_name(),
                teacher,
                room,
                building,
                field,
                department,
                subject.get_day(),
                subject.get_start(),
                subject.get_end(),
                group
            )

            self.list_subjects.insert(i, output)

    def year_subjects(self):
        return [subject for subject in self.controller.subjects if subject.is_year_subject()]
    


class CreateYearSubjectPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.columnconfigure([x for x in range(9)], minsize=250)
        self.rowconfigure([x for x in range(18)], minsize=40)
        self.controller = controller
        
        self.main_label()
        self.return_button()
        self.home_button()
        
        self.submit()
        self.day_entry()
        self.start_entry()
        self.stop_entry()
        self.name_entry()
        self.field_listbox()
        self.room_listbox()
        self.year_listbox()
        self.teacher_listbox()


    def main_label(self):
        label = tk.Label(
            self,
            text="Create Subject",
            font=self.controller.title_font
        )
        label.grid(row=0, column=0, rowspan=1, columnspan=4, sticky="news", padx=5, pady=5)


    def return_button(self):
        btn_return = tk.Button(
            self,
            text="return",
            command=lambda : self.return_refresh(),
            font=self.controller.normal_font,
        )
        btn_return.grid(row=16, column=0, rowspan=2, columnspan=2, sticky="news", padx=5, pady=5)

    def home_button(self):
        btn_home = tk.Button(
            self,
            text="Home",
            command=lambda : self.home_refresh(),
            font=self.controller.normal_font,
        )
        btn_home.grid(row=16, column=2,rowspan=2, columnspan=2, sticky="news", padx=5, pady=5)


    def return_refresh(self):
        self.refresh()
        self.controller.show_frame("YearSubjectPage")


    def home_refresh(self):
        self.refresh()
        self.controller.show_frame("StartPage")


    def refresh(self):
        self.e_day.delete(0, tk.END)
        self.e_start.delete(0, tk.END)
        self.e_stop.delete(0, tk.END)
        self.e_name.delete(0, tk.END)


    def day_entry(self):
        l_day = tk.Label(master=self, text="day", font=self.controller.normal_font, anchor=tk.W, relief=tk.RAISED)
        l_day.grid(row=1, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)

        self.e_day = tk.Entry(master=self, font=self.controller.entry_font)
        self.e_day.grid(row=2, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)


    def start_entry(self):
        l_start = tk.Label(master=self, text="start", font=self.controller.normal_font, anchor=tk.W, relief=tk.RAISED)
        l_start.grid(row=3, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)

        self.e_start = tk.Entry(master=self, font=self.controller.entry_font)
        self.e_start.grid(row=4, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)


    def stop_entry(self):
        l_stop = tk.Label(master=self, text="stop",font=self.controller.normal_font, anchor=tk.W, relief=tk.RAISED)
        l_stop.grid(row=5, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)

        self.e_stop = tk.Entry(master=self, font=self.controller.entry_font)
        self.e_stop.grid(row=6, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)


    def name_entry(self):
        l_name = tk.Label(master=self, text="name", font=self.controller.normal_font, anchor=tk.W, relief=tk.RAISED)
        l_name.grid(row=7, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)

        self.e_name = tk.Entry(master=self, font=self.controller.entry_font)
        self.e_name.grid(row=8, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)


    def field_listbox(self):
        l_field = tk.Label(master=self, text="field", font=self.controller.normal_font, relief=tk.RAISED)
        l_field.grid(row=9, column=0, rowspan=1, columnspan=4, sticky="nswe", pady=5, padx=5)
        
        data = [
            ('field of study', 20),
            ('department', 20)
        ]
        self.list_fields = MultiListBox(master=self, data=data)
        self.list_fields.grid(row=10, column=0, rowspan=4, columnspan=4, sticky="nswe", pady=5, padx=5)
        self.refresh_field_listbox()


    def refresh_field_listbox(self):
        self.list_fields.delete(0, tk.END)
        for i, field in enumerate(self.controller.fields):
            try:
                dept = field.get_department().get_name()
            except AttributeError:
                dept = "NULL"

            output = (
                field.get_name(),
                dept
            )

            self.list_fields.insert(i, output)


    def room_listbox(self):
        l_room = tk.Label(master=self, text="room", font=self.controller.normal_font, relief=tk.RAISED)
        l_room.grid(row=0, column=4, rowspan=1, columnspan=3, sticky="nswe", pady=5, padx=5)

        data = [
            ('room number', 10),
            ('building', 20)
        ]
        self.list_rooms = MultiListBox(master=self, data=data)
        self.list_rooms.grid(row=1, column=4, rowspan=4, columnspan=3, sticky="nswe", pady=5, padx=5)
        self.refresh_room_listbox()


    def refresh_room_listbox(self):
        self.list_rooms.delete(0, tk.END)
        for i, room in enumerate(self.controller.rooms):
            try:
                building = room.get_building().get_name()
            except AttributeError:
                building = "NULL"

            try:
                room_number = room.get_number()
            except AttributeError:
                room_number = "NULL"

            output = (
                room_number,
                building
            )

            self.list_rooms.insert(i, output)


    def year_listbox(self):
        l_group = tk.Label(master=self, text="year groups", font=self.controller.normal_font, relief=tk.RAISED)
        l_group.grid(row=6, column=4, rowspan=1, columnspan=3, sticky="nswe", pady=5, padx=5)
        
        data = [
            ('number',10),
            ('field of study', 20),
            ('department', 20),
            ('students', 10) #numbers of students
        ]

        self.list_groups = MultiListBox(master=self, data=data)
        self.refresh_year_listbox()
        self.list_groups.grid(row=7, column=4, rowspan=4, columnspan=3, sticky="nswe", pady=5, padx=5)


    def refresh_year_listbox(self):
        self.list_groups.delete(0, tk.END)
        for i, group in enumerate(self.controller.year_groups):
            try:
                field = group.get_field().get_name()
                try:
                    dept = group.get_field().get_department().get_name()
                except AttributeError:
                    dept = "NULL"
            except AttributeError:
                field = "NULL"
                dept = "NULL"


            output = (
                group.get_number(),
                field,
                dept,
                len(group.get_students())
            )

            self.list_groups.insert(i, output)


    def teacher_listbox(self):
        l_teacher = tk.Label(master=self, text="teacher", font=self.controller.normal_font, relief=tk.RAISED)
        l_teacher.grid(row=12, column=4, rowspan=1, columnspan=3, sticky="nswe", pady=5, padx=5)

        data = [
            ('name', 10),
            ('lastname', 10)
        ]

        self.list_teachers = MultiListBox(master=self, data=data)
        self.list_teachers.grid(row=13, column=4, rowspan=4, columnspan=3, sticky="nswe", pady=5, padx=5)
        self.refresh_teacher_listbox()


    def refresh_teacher_listbox(self):
        self.list_teachers.delete(0, tk.END)
        for i, teacher in enumerate(self.controller.teachers):
            try:
                name = teacher.get_name()
            except AttributeError:
                name = "NULL"

            try:
                lastname = teacher.get_lastname()
            except AttributeError:
                lastname = "NULL"

            output = (
                name,
                lastname
            )

            self.list_teachers.insert(i, output)


    def submit(self):
        sub_btn = tk.Button(
            master=self,
            text="submit",
            command=lambda : self.create_subject(),
            font=self.controller.normal_font,
        )
        sub_btn.grid(row=14, column=0, rowspan=2, columnspan=4, sticky="nswe", pady=5, padx=5)


    def create_subject(self):
        try:
            teacher_idx = self.list_teachers.index(tk.ACTIVE)
            teacher = self.controller.teachers[teacher_idx]
        except IndexError:
            teacher = None

        try:
            room_idx = self.list_rooms.index(tk.ACTIVE)
            room = self.controller.rooms[room_idx]
        except IndexError:
            room = None

        try:
            field_idx = self.list_fields.index(tk.ACTIVE)
            field = self.controller.fields[field_idx]
        except IndexError:
            field = None

        try:
            group_idx = self.list_groups.index(tk.ACTIVE)
            group = self.controller.year_groups[group_idx]
        except IndexError:
            group = None

        self.controller.subjects.append(Subject(
            teacher=teacher,
            year_group=group,
            room=room,
            field=field,
            day=self.e_day.get(),
            start=self.e_start.get(),
            end=self.e_stop.get(),
            name=self.e_name.get()
        ))

        self.refresh()
        self.controller.subjects[-1].insert(self.controller.db)
        self.controller.db.commit_conn()
        self.controller.frames["YearSubjectPage"].restart()


class ExeSubjectPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.columnconfigure([x for x in range(7)], minsize=250)
        self.rowconfigure([x for x in range(9)], minsize=100)
        self.controller = controller
        self.main_label()

        self.subject_listbox()
        self.refresh_button()
        self.buttons()


    def main_label(self):
        label = tk.Label(
            master=self,
            text="Exe Subjects Page",
            font=self.controller.title_font
        )
        label.grid(row = 0, column = 6, sticky="nsew", padx=5, pady=5)


    def buttons(self):
        #Return Home Page
        btn_home = tk.Button(
            self,
            text="Home",
            command=lambda : self.controller.show_frame("StartPage"),
            font=self.controller.normal_font,
        )
        btn_home.grid(row=3, column=6, sticky="nsew", padx=5, pady=5)
        #Create Exe Subject
        btn_create = tk.Button(
            self,
            text="Create Subject",
            command=lambda : self.create_subject(),
            font=self.controller.normal_font,
        )
        btn_create.grid(row=1, column=6, sticky="nsew", padx=5, pady=5)
        #Delete Exe Subject
        btn_delete = tk.Button(
            self,
            text="Delete Subject",
            command=lambda : self.delete_subject(),
            font=self.controller.normal_font,
        )
        btn_delete.grid(row=2, column=6, sticky="nsew", padx=5, pady=5)
        #Return button
        btn_return = tk.Button(
            self,
            text="Return",
            command=lambda : self.controller.show_frame("SubjectPage"),
            font=self.controller.normal_font,
        )
        btn_return.grid(row=4, column=6, sticky="nsew", padx=5, pady=5)


    def subject_listbox(self):
        data = [
            ('name', 20),
            ('teacher', 20),
            ('room', 20),
            ('building', 10), #from room
            ('field', 20),
            ('department', 20), #from field
            ('day', 10),
            ('start', 10),
            ('stop', 10),
            ('group number', 10)
        ]

        self.list_subjects = MultiListBox(master=self, data=data)
        self.refresh()
        self.list_subjects.grid(row=0, column=0, columnspan=6, rowspan=9, sticky="nswe", padx=5, pady=5)


    def create_subject(self):
        self.controller.show_frame("CreateExeSubjectPage")

    
    def delete_subject(self):
        idx = self.list_subjects.index(tk.ACTIVE)
        del_subject = self.exe_subjects()[idx]

        del_subject.delete(self.controller.db)
        self.controller.db.commit_conn()
        self.controller.subjects.remove(del_subject)

        del del_subject

        self.restart()


    def refresh_button(self):
        btn_refresh = tk.Button(
            master=self,
            text="refresh",
            command=lambda : self.restart(),
            font=self.controller.normal_font,
        )
        btn_refresh.grid(row=8, column=6, sticky="nsew", padx=5, pady=5)


    def restart(self):
        self.refresh()
        self.controller.show_frame("ExeSubjectPage")


    def refresh(self):
        self.list_subjects.delete(0, tk.END)
        subjects = self.exe_subjects()
        for i, subject in enumerate(subjects):
            try:
                teacher = subject.get_teacher().get_name() + " " + subject.get_teacher().get_lastname()
            except AttributeError:
                teacher = "NULL"

            try:
                room = subject.get_room().get_number()
                building = subject.get_room().get_building().get_name()
            except AttributeError:
                room = "NULL"
                building = "NULL"

            try:
                field = subject.get_field().get_name()
                department = subject.get_field().get_department().get_name()
            except AttributeError:
                field = "NULL"
                department = "NULL"

            try:
                group = subject.get_group().get_number()
            except AttributeError:
                group = "NULL"


            output = (
                subject.get_name(),
                teacher,
                room,
                building,
                field,
                department,
                subject.get_day(),
                subject.get_start(),
                subject.get_end(),
                group
            )

            self.list_subjects.insert(i, output)


    def exe_subjects(self):
        return [subject for subject in self.controller.subjects if subject.is_exe_subject()]    


class CreateExeSubjectPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.columnconfigure([x for x in range(9)], minsize=250)
        self.rowconfigure([x for x in range(18)], minsize=40)
        self.controller = controller

        self.main_label()
        self.return_button()
        self.home_button()
        
        self.submit()
        self.day_entry()
        self.start_entry()
        self.stop_entry()
        self.name_entry()
        self.field_listbox()
        self.room_listbox()
        self.exe_listbox()
        self.teacher_listbox()


    def main_label(self):
        label = tk.Label(
            self,
            text="Create Subject",
            font=self.controller.title_font
        )
        label.grid(row=0, column=0, rowspan=1, columnspan=4, sticky="news", padx=5, pady=5)


    def return_button(self):
        btn_return = tk.Button(
            self,
            text="return",
            command=lambda : self.return_refresh(),
            font=self.controller.normal_font,
        )
        btn_return.grid(row=16, column=0, rowspan=2, columnspan=2, sticky="news", padx=5, pady=5)


    def home_button(self):
        btn_home = tk.Button(
            self,
            text="Home",
            command=lambda : self.home_refresh(),
            font=self.controller.normal_font,
        )
        btn_home.grid(row=16, column=2,rowspan=2, columnspan=2, sticky="news", padx=5, pady=5)


    def return_refresh(self):
        self.refresh()
        self.controller.show_frame("ExeSubjectPage")


    def home_refresh(self):
        self.refresh()
        self.controller.show_frame("StartPage")


    def refresh(self):
        self.e_day.delete(0, tk.END)
        self.e_start.delete(0, tk.END)
        self.e_stop.delete(0, tk.END)
        self.e_name.delete(0, tk.END)


    def day_entry(self):
        l_day = tk.Label(master=self, text="day", font=self.controller.normal_font, anchor=tk.W, relief=tk.RAISED)
        l_day.grid(row=1, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)

        self.e_day = tk.Entry(master=self, font=self.controller.entry_font)
        self.e_day.grid(row=2, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)


    def start_entry(self):
        l_start = tk.Label(master=self, text="start", font=self.controller.normal_font, anchor=tk.W, relief=tk.RAISED)
        l_start.grid(row=3, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)

        self.e_start = tk.Entry(master=self, font=self.controller.entry_font)
        self.e_start.grid(row=4, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)


    def stop_entry(self):
        l_stop = tk.Label(master=self, text="stop", font=self.controller.normal_font, anchor=tk.W, relief=tk.RAISED)
        l_stop.grid(row=5, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)

        self.e_stop = tk.Entry(master=self, font=self.controller.entry_font)
        self.e_stop.grid(row=6, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)


    def name_entry(self):
        l_name = tk.Label(master=self, text="name", font=self.controller.normal_font, anchor=tk.W, relief=tk.RAISED)
        l_name.grid(row=7, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)

        self.e_name = tk.Entry(master=self, font=self.controller.entry_font)
        self.e_name.grid(row=8, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)


    def field_listbox(self):
        l_field = tk.Label(master=self, text="field", font=self.controller.normal_font, relief=tk.RAISED)
        l_field.grid(row=9, column=0, rowspan=1, columnspan=4, sticky="nswe", pady=5, padx=5)
        
        data = [
            ('field of study', 20),
            ('department', 20)
        ]

        self.list_fields = MultiListBox(master=self, data=data)
        self.list_fields.grid(row=10, column=0, rowspan=4, columnspan=4, sticky="nswe", pady=5, padx=5)
        self.refresh_field_listbox()


    def refresh_field_listbox(self):
        self.list_fields.delete(0, tk.END)
        for i, field in enumerate(self.controller.fields):
            try:
                dept = field.get_department().get_name()
            except AttributeError:
                dept = "NULL"

            output = (
                field.get_name(),
                dept
            )

            self.list_fields.insert(i, output)


    def room_listbox(self):
        l_room = tk.Label(master=self, text="room", font=self.controller.normal_font, relief=tk.RAISED)
        l_room.grid(row=0, column=4, rowspan=1, columnspan=3, sticky="nswe", pady=5, padx=5)

        data = [
            ('room number', 10),
            ('building', 20)
        ]
        self.list_rooms = MultiListBox(master=self, data=data)
        self.list_rooms.grid(row=1, column=4, rowspan=4, columnspan=3, sticky="nswe", pady=5, padx=5)
        self.refresh_room_listbox()


    def refresh_room_listbox(self):
        self.list_rooms.delete(0, tk.END)
        for i, room in enumerate(self.controller.rooms):
            try:
                building = room.get_building().get_name()
            except AttributeError:
                building = "NULL"

            output = (
                room.get_number(),
                building
            )

            self.list_rooms.insert(i, output)


    def exe_listbox(self):
        l_group = tk.Label(master=self, text="exe groups", font=self.controller.normal_font, relief=tk.RAISED)
        l_group.grid(row=6, column=4, rowspan=1, columnspan=3, sticky="nswe", pady=5, padx=5)
        
        data = [
            ('number',10),
            ('field of study', 20),
            ('department', 20),
            ('students', 10) #numbers of students
        ]

        self.list_groups = MultiListBox(master=self, data=data)
        self.refresh_exe_listbox()
        self.list_groups.grid(row=7, column=4, rowspan=4, columnspan=3, sticky="nswe", pady=5, padx=5)


    def refresh_exe_listbox(self):
        self.list_groups.delete(0, tk.END)
        for i, group in enumerate(self.controller.exe_groups):
            try:
                field = group.get_field().get_name()
                try:
                    dept = group.get_field().get_department().get_name()
                except AttributeError:
                    dept = "NULL"
            except AttributeError:
                field = "NULL"
                dept = "NULL"


            output = (
                group.get_number(),
                field,
                dept,
                len(group.get_students())
            )

            self.list_groups.insert(i, output)


    def teacher_listbox(self):
        l_teacher = tk.Label(master=self, text="teacher", font=self.controller.normal_font, relief=tk.RAISED)
        l_teacher.grid(row=12, column=4, rowspan=1, columnspan=3, sticky="nswe", pady=5, padx=5)

        data = [
            ('name', 10),
            ('lastname', 10)
        ]

        self.list_teachers = MultiListBox(master=self, data=data)
        self.list_teachers.grid(row=13, column=4, rowspan=4, columnspan=3, sticky="nswe", pady=5, padx=5)
        self.refresh_teacher_listbox()


    def refresh_teacher_listbox(self):
        self.list_teachers.delete(0, tk.END)
        for i, teacher in enumerate(self.controller.teachers):
            try:
                name = teacher.get_name()
            except AttributeError:
                name = "NULL"

            try:
                lastname = teacher.get_lastname()
            except AttributeError:
                lastname = "NULL"

            output = (
                name,
                lastname
            )

            self.list_teachers.insert(i, output)


    def submit(self):
        sub_btn = tk.Button(
            master=self,
            text="submit",
            command=lambda : self.create_subject(),
            font=self.controller.normal_font,
        )
        sub_btn.grid(row=14, column=0, rowspan=2, columnspan=4, sticky="nswe", pady=5, padx=5)


    def create_subject(self):
        try:
            teacher_idx = self.list_teachers.index(tk.ACTIVE)
            teacher = self.controller.teachers[teacher_idx]
        except IndexError:
            teacher = None

        try:
            room_idx = self.list_rooms.index(tk.ACTIVE)
            room = self.controller.rooms[room_idx]
        except IndexError:
            room = None

        try:
            field_idx = self.list_fields.index(tk.ACTIVE)
            field = self.controller.fields[field_idx]
        except IndexError:
            field = None

        try:
            group_idx = self.list_groups.index(tk.ACTIVE)
            group = self.controller.exe_groups[group_idx]
        except IndexError:
            group = None

        self.controller.subjects.append(Subject(
            teacher=teacher,
            exe_group=group,
            room=room,
            field=field,
            day=self.e_day.get(),
            start=self.e_start.get(),
            end=self.e_stop.get(),
            name=self.e_name.get()
        ))

        self.refresh()
        self.controller.subjects[-1].insert(self.controller.db)
        self.controller.db.commit_conn()
        self.controller.frames["ExeSubjectPage"].restart()
        

class LabSubjectPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.columnconfigure([x for x in range(7)], minsize=250)
        self.rowconfigure([x for x in range(9)], minsize=100)
        self.controller = controller
        self.main_label()

        self.subject_listbox()
        self.refresh_button()
        self.buttons()


    def main_label(self):
        label = tk.Label(
            master=self,
            text="Lab Subjects Page",
            font=self.controller.title_font
        )
        label.grid(row = 0, column = 6, sticky="nsew", padx=5, pady=5)


    def buttons(self):
        #Return Home Page
        btn_home = tk.Button(
            self,
            text="Home",
            command=lambda : self.controller.show_frame("StartPage"),
            font=self.controller.normal_font,
        )
        btn_home.grid(row=3, column=6, sticky="nsew", padx=5, pady=5)
        #Create Year Subject
        btn_create = tk.Button(
            self,
            text="Create Subject",
            command=lambda : self.create_subject(),
            font=self.controller.normal_font,
        )
        btn_create.grid(row=1, column=6, sticky="nsew", padx=5, pady=5)
        #Delete Year Subject
        btn_delete = tk.Button(
            self,
            text="Delete Subject",
            command=lambda : self.delete_subject(),
            font=self.controller.normal_font,
        )
        btn_delete.grid(row=2, column=6, sticky="nsew", padx=5, pady=5)
        #Return button
        btn_return = tk.Button(
            self,
            text="Return",
            command=lambda : self.controller.show_frame("SubjectPage"),
            font=self.controller.normal_font,
        )
        btn_return.grid(row=4, column=6, sticky="nsew", padx=5, pady=5)


    def subject_listbox(self):
        data = [
            ('name', 20),
            ('teacher', 20),
            ('room', 20),
            ('building', 10), #from room
            ('field', 20),
            ('department', 20), #from field
            ('day', 10),
            ('start', 10),
            ('stop', 10),
            ('group number', 10)
        ]

        self.list_subjects = MultiListBox(master=self, data=data)
        self.refresh()
        self.list_subjects.grid(row=0, column=0, columnspan=6, rowspan=9, sticky="nswe", padx=5, pady=5)


    def create_subject(self):
        self.controller.show_frame("CreateLabSubjectPage")


    def delete_subject(self):
        idx = self.list_subjects.index(tk.ACTIVE)
        del_subject = self.lab_subjects()[idx]

        del_subject.delete(self.controller.db)
        self.controller.db.commit_conn()
        self.controller.subjects.remove(del_subject)

        del del_subject

        self.restart()


    def refresh_button(self):
        btn_refresh = tk.Button(
            master=self,
            text="refresh",
            command=lambda : self.restart(),
            font=self.controller.normal_font,
        )
        btn_refresh.grid(row=8, column=6, sticky="nsew", padx=5, pady=5)


    def restart(self):
        self.refresh()
        self.controller.show_frame("LabSubjectPage")


    def refresh(self):
        self.list_subjects.delete(0, tk.END)
        subjects = self.lab_subjects()
        for i, subject in enumerate(subjects):
            try:
                teacher = subject.get_teacher().get_name() + " " + subject.get_teacher().get_lastname()
            except AttributeError:
                teacher = "NULL"

            try:
                room = subject.get_room().get_number()
                building = subject.get_room().get_building().get_name()
            except AttributeError:
                room = "NULL"
                building = "NULL"

            try:
                field = subject.get_field().get_name()
                department = subject.get_field().get_department().get_name()
            except AttributeError:
                field = "NULL"
                department = "NULL"

            try:
                group = subject.get_group().get_number()
            except AttributeError:
                group = "NULL"


            output = (
                subject.get_name(),
                teacher,
                room,
                building,
                field,
                department,
                subject.get_day(),
                subject.get_start(),
                subject.get_end(),
                group
            )

            self.list_subjects.insert(i, output)


    def lab_subjects(self):
        return [subject for subject in self.controller.subjects if subject.is_lab_subject()]    


class CreateLabSubjectPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.columnconfigure([x for x in range(9)], minsize=250)
        self.rowconfigure([x for x in range(18)], minsize=40)
        self.controller = controller

        self.main_label()
        self.return_button()
        self.home_button()
        
        self.submit()
        self.day_entry()
        self.start_entry()
        self.stop_entry()
        self.name_entry()
        self.field_listbox()
        self.room_listbox()
        self.lab_listbox()
        self.teacher_listbox()


    def main_label(self):
        label = tk.Label(
            self,
            text="Create Subject",
            font=self.controller.title_font
        )
        label.grid(row=0, column=0, rowspan=1, columnspan=4, sticky="news", padx=5, pady=5)


    def return_button(self):
        btn_return = tk.Button(
            self,
            text="return",
            command=lambda : self.return_refresh(),
            font=self.controller.normal_font,
        )
        btn_return.grid(row=16, column=0, rowspan=2, columnspan=2, sticky="news", padx=5, pady=5)


    def home_button(self):
        btn_home = tk.Button(
            self,
            text="Home",
            command=lambda : self.home_refresh(),
            font=self.controller.normal_font,
        )
        btn_home.grid(row=16, column=2,rowspan=2, columnspan=2, sticky="news", padx=5, pady=5)


    def return_refresh(self):
        self.refresh()
        self.controller.show_frame("LabSubjectPage")

    
    def home_refresh(self):
        self.refresh()
        self.controller.show_frame("StartPage")


    def refresh(self):
        self.e_day.delete(0, tk.END)
        self.e_start.delete(0, tk.END)
        self.e_stop.delete(0, tk.END)
        self.e_name.delete(0, tk.END)

    
    def day_entry(self):
        l_day = tk.Label(master=self, text="day", font=self.controller.normal_font, anchor=tk.W, relief=tk.RAISED)
        l_day.grid(row=1, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)

        self.e_day = tk.Entry(master=self, font=self.controller.entry_font)
        self.e_day.grid(row=2, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)


    def start_entry(self):
        l_start = tk.Label(master=self, text="start", font=self.controller.normal_font, anchor=tk.W, relief=tk.RAISED)
        l_start.grid(row=3, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)

        self.e_start = tk.Entry(master=self, font=self.controller.entry_font)
        self.e_start.grid(row=4, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)


    def stop_entry(self):
        l_stop = tk.Label(master=self, text="stop", font=self.controller.normal_font, anchor=tk.W, relief=tk.RAISED)
        l_stop.grid(row=5, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)

        self.e_stop = tk.Entry(master=self, font=self.controller.entry_font)
        self.e_stop.grid(row=6, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)


    def name_entry(self):
        l_name = tk.Label(master=self, text="name", font=self.controller.normal_font, anchor=tk.W, relief=tk.RAISED)
        l_name.grid(row=7, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)

        self.e_name = tk.Entry(master=self, font=self.controller.entry_font)
        self.e_name.grid(row=8, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)


    def field_listbox(self):
        l_field = tk.Label(master=self, text="field", font=self.controller.normal_font, relief=tk.RAISED)
        l_field.grid(row=9, column=0, rowspan=1, columnspan=4, sticky="nswe", pady=5, padx=5)
        
        data = [
            ('field of study', 20),
            ('department', 20)
        ]
        self.list_fields = MultiListBox(master=self, data=data)
        self.list_fields.grid(row=10, column=0, rowspan=4, columnspan=4, sticky="nswe", pady=5, padx=5)
        self.refresh_field_listbox()


    def refresh_field_listbox(self):
        self.list_fields.delete(0, tk.END)
        for i, field in enumerate(self.controller.fields):
            try:
                dept = field.get_department().get_name()
            except AttributeError:
                dept = "NULL"

            output = (
                field.get_name(),
                dept
            )

            self.list_fields.insert(i, output)


    def room_listbox(self):
        l_room = tk.Label(master=self, text="room", font=self.controller.normal_font, relief=tk.RAISED)
        l_room.grid(row=0, column=4, rowspan=1, columnspan=3, sticky="nswe", pady=5, padx=5)

        data = [
            ('room number', 10),
            ('building', 20)
        ]
        self.list_rooms = MultiListBox(master=self, data=data)
        self.list_rooms.grid(row=1, column=4, rowspan=4, columnspan=3, sticky="nswe", pady=5, padx=5)
        self.refresh_room_listbox()


    def refresh_room_listbox(self):
        self.list_rooms.delete(0, tk.END)
        for i, room in enumerate(self.controller.rooms):
            try:
                building = room.get_building().get_name()
            except AttributeError:
                building = "NULL"

            output = (
                room.get_number(),
                building
            )

            self.list_rooms.insert(i, output)


    def lab_listbox(self):
        l_group = tk.Label(master=self, text="lab groups", font=self.controller.normal_font, relief=tk.RAISED)
        l_group.grid(row=6, column=4, rowspan=1, columnspan=3, sticky="nswe", pady=5, padx=5)
        
        data = [
            ('number',10),
            ('field of study', 20),
            ('department', 20),
            ('students', 10) #numbers of students
        ]

        self.list_groups = MultiListBox(master=self, data=data)
        self.refresh_lab_listbox()
        self.list_groups.grid(row=7, column=4, rowspan=4, columnspan=3, sticky="nswe", pady=5, padx=5)


    def refresh_lab_listbox(self):
        self.list_groups.delete(0, tk.END)
        for i, group in enumerate(self.controller.lab_groups):
            try:
                field = group.get_field().get_name()
                try:
                    dept = group.get_field().get_department().get_name()
                except AttributeError:
                    dept = "NULL"
            except AttributeError:
                field = "NULL"
                dept = "NULL"


            output = (
                group.get_number(),
                field,
                dept,
                len(group.get_students())
            )

            self.list_groups.insert(i, output)


    def teacher_listbox(self):
        l_teacher = tk.Label(master=self, text="teacher", font=self.controller.normal_font, relief=tk.RAISED)
        l_teacher.grid(row=12, column=4, rowspan=1, columnspan=3, sticky="nswe", pady=5, padx=5)

        data = [
            ('name', 10),
            ('lastname', 10)
        ]

        self.list_teachers = MultiListBox(master=self, data=data)
        self.list_teachers.grid(row=13, column=4, rowspan=4, columnspan=3, sticky="nswe", pady=5, padx=5)
        self.refresh_teacher_listbox()


    def refresh_teacher_listbox(self):
        self.list_teachers.delete(0, tk.END)
        for i, teacher in enumerate(self.controller.teachers):
            try:
                name = teacher.get_name()
            except AttributeError:
                name = "NULL"

            try:
                lastname = teacher.get_lastname()
            except AttributeError:
                lastname = "NULL"

            output = (
                name,
                lastname
            )

            self.list_teachers.insert(i, output)


    def submit(self):
        sub_btn = tk.Button(
            master=self,
            text="submit",
            command=lambda : self.create_subject(),
            font=self.controller.normal_font,
        )
        sub_btn.grid(row=14, column=0, rowspan=2, columnspan=4, sticky="nswe", pady=5, padx=5)


    def create_subject(self):
        try:
            teacher_idx = self.list_teachers.index(tk.ACTIVE)
            teacher = self.controller.teachers[teacher_idx]
        except IndexError:
            teacher = None

        try:
            room_idx = self.list_rooms.index(tk.ACTIVE)
            room = self.controller.rooms[room_idx]
        except IndexError:
            room = None

        try:
            field_idx = self.list_fields.index(tk.ACTIVE)
            field = self.controller.fields[field_idx]
        except IndexError:
            field = None

        try:
            group_idx = self.list_groups.index(tk.ACTIVE)
            group = self.controller.lab_groups[group_idx]
        except IndexError:
            group = None

        self.controller.subjects.append(Subject(
            teacher=teacher,
            lab_group=group,
            room=room,
            field=field,
            day=self.e_day.get(),
            start=self.e_start.get(),
            end=self.e_stop.get(),
            name=self.e_name.get()
        ))

        self.refresh()
        self.controller.subjects[-1].insert(self.controller.db)
        self.controller.db.commit_conn()
        self.controller.frames["LabSubjectPage"].restart()
