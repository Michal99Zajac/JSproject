import tkinter as tk

from Tables.Subject import Subject

from tk_extension.multilistBox import MultiListBox

class SubjectPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.main_label()

        self.year_button()
        self.exe_button()
        self.lab_button()
        self.return_button()


    def main_label(self):
        label = tk.Label(
            self,
            text="Subject Page",
            font=self.controller.title_font
        )
        label.pack(side=tk.TOP, fill=tk.X, pady=10)


    def year_button(self):
        year_btn = tk.Button(
            master=self,
            text="Show Year Subject",
            command=lambda : self.controller.show_frame("YearSubjectPage")
        )
        year_btn.pack()


    def exe_button(self):
        exe_btn = tk.Button(
            master=self,
            text="Show Exe Subject",
            command=lambda : self.controller.show_frame("ExeSubjectPage")
        )
        exe_btn.pack()


    def lab_button(self):
        lab_btn = tk.Button(
            master=self,
            text="Show Lab Subject",
            command=lambda : self.controller.show_frame("LabSubjectPage")
        )
        lab_btn.pack()


    def return_button(self):
        return_btn = tk.Button(
            self,
            text="Return to Home Page",
            command=lambda : self.controller.show_frame("StartPage")
        )
        return_btn.pack()
        

class YearSubjectPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.main_label()

        self.subject_listbox()
        self.refresh_button()
        self.buttons()


    def main_label(self):
        label = tk.Label(
            master=self,
            text="Year Subjects Page",
            font=self.controller.title_font
        )
        label.pack(side=tk.TOP, fill=tk.X, pady=10)

    
    def buttons(self):
        #Return Home Page
        btn_return = tk.Button(
            self,
            text="Return to Home Page",
            command=lambda : self.controller.show_frame("StartPage")
        )
        btn_return.pack()
        #Create Year Subject
        btn_create = tk.Button(
            self,
            text="Create Subject",
            command=lambda : self.create_subject()
        )
        btn_create.pack()
        #Delete Year Subject
        btn_delete = tk.Button(
            self,
            text="Delete Subject",
            command=lambda : self.delete_subject()
        )
        btn_delete.pack()


    def subject_listbox(self):
        f_subject = tk.Frame(master=self)
        f_subject.pack()
        l_subject = tk.Label(master=f_subject, text="select subject")
        l_subject.pack()

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

        self.list_subjects = MultiListBox(master=f_subject, data=data)
        self.refresh()
        self.list_subjects.pack()

    
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
        f_refresh = tk.Frame(master=self)
        f_refresh.pack()
        btn_refresh = tk.Button(
            master=f_refresh,
            text="refresh",
            command=lambda : self.restart()
        )
        btn_refresh.pack()


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
        label.pack(side=tk.TOP, fill=tk.X, pady=10)


    def return_button(self):
        btn_return = tk.Button(
            self,
            text="return",
            command=lambda : self.return_refresh()
        )
        btn_return.pack()

    def home_button(self):
        btn_home = tk.Button(
            self,
            text="Return to Home Page",
            command=lambda : self.home_refresh()
        )
        btn_home.pack()


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
        f_day = tk.Frame(master=self)
        f_day.pack()

        l_day = tk.Label(master=f_day, text="day")
        l_day.pack()

        self.e_day = tk.Entry(master=f_day)
        self.e_day.pack()


    def start_entry(self):
        f_start = tk.Frame(master=self)
        f_start.pack()

        l_start = tk.Label(master=f_start, text="start")
        l_start.pack()

        self.e_start = tk.Entry(master=f_start)
        self.e_start.pack()


    def stop_entry(self):
        f_stop = tk.Frame(master=self)
        f_stop.pack()

        l_stop = tk.Label(master=f_stop, text="stop")
        l_stop.pack()

        self.e_stop = tk.Entry(master=f_stop)
        self.e_stop.pack()


    def name_entry(self):
        f_name = tk.Frame(master=self)
        f_name.pack()

        l_name = tk.Label(master=f_name, text="name")
        l_name.pack()

        self.e_name = tk.Entry(master=f_name)
        self.e_name.pack()


    def field_listbox(self):
        f_field = tk.Frame(master=self)
        f_field.pack()
        
        data = [
            ('field of study', 20),
            ('department', 20)
        ]
        self.list_fields = MultiListBox(master=f_field, data=data)
        self.list_fields.pack()
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
        f_room = tk.Frame(master=self)
        f_room.pack()

        data = [
            ('room number', 10),
            ('building', 20)
        ]
        self.list_rooms = MultiListBox(master=f_room, data=data)
        self.list_rooms.pack()
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


    def year_listbox(self):
        f_group = tk.Frame(master=self)
        f_group.pack()
        
        data = [
            ('number',10),
            ('field of study', 20),
            ('department', 20),
            ('students', 10) #numbers of students
        ]

        self.list_groups = MultiListBox(master=f_group, data=data)
        self.refresh_year_listbox()
        self.list_groups.pack()


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


            output = (
                group.get_number(),
                field,
                dept,
                len(group.get_students())
            )

            self.list_groups.insert(i, output)


    def teacher_listbox(self):
        f_teacher = tk.Frame(master=self)
        f_teacher.pack()

        data = [
            ('name', 10),
            ('lastname', 10)
        ]

        self.list_teachers = MultiListBox(master=f_teacher, data=data)
        self.list_teachers.pack()
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
        f_submit = tk.Frame(master=self)
        f_submit.pack()

        sub_btn = tk.Button(
            master=f_submit,
            text="submit",
            command=lambda : self.create_subject()
        )
        sub_btn.pack()


    def create_subject(self):
        teacher_idx = self.list_teachers.index(tk.ACTIVE)
        teacher = self.controller.teachers[teacher_idx]

        room_idx = self.list_rooms.index(tk.ACTIVE)
        room = self.controller.rooms[room_idx]

        field_idx = self.list_fields.index(tk.ACTIVE)
        field = self.controller.fields[field_idx]

        group_idx = self.list_groups.index(tk.ACTIVE)
        group = self.controller.year_groups[group_idx]

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
        label.pack(side=tk.TOP, fill=tk.X, pady=10)


    def buttons(self):
        #Return Home Page
        btn_return = tk.Button(
            self,
            text="Return to Home Page",
            command=lambda : self.controller.show_frame("StartPage")
        )
        btn_return.pack()
        #Create Exe Subject
        btn_create = tk.Button(
            self,
            text="Create Subject",
            command=lambda : self.create_subject()
        )
        btn_create.pack()
        #Delete Exe Subject
        btn_delete = tk.Button(
            self,
            text="Delete Subject",
            command=lambda : self.delete_subject()
        )
        btn_delete.pack()


    def subject_listbox(self):
        f_subject = tk.Frame(master=self)
        f_subject.pack()
        l_subject = tk.Label(master=f_subject, text="select subject")
        l_subject.pack()

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

        self.list_subjects = MultiListBox(master=f_subject, data=data)
        self.refresh()
        self.list_subjects.pack()


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
        f_refresh = tk.Frame(master=self)
        f_refresh.pack()
        btn_refresh = tk.Button(
            master=f_refresh,
            text="refresh",
            command=lambda : self.restart()
        )
        btn_refresh.pack()


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
        label.pack(side=tk.TOP, fill=tk.X, pady=10)


    def return_button(self):
        btn_return = tk.Button(
            self,
            text="return",
            command=lambda : self.return_refresh()
        )
        btn_return.pack()


    def home_button(self):
        btn_home = tk.Button(
            self,
            text="Return to Home Page",
            command=lambda : self.home_refresh()
        )
        btn_home.pack()


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
        f_day = tk.Frame(master=self)
        f_day.pack()

        l_day = tk.Label(master=f_day, text="day")
        l_day.pack()

        self.e_day = tk.Entry(master=f_day)
        self.e_day.pack()


    def start_entry(self):
        f_start = tk.Frame(master=self)
        f_start.pack()

        l_start = tk.Label(master=f_start, text="start")
        l_start.pack()

        self.e_start = tk.Entry(master=f_start)
        self.e_start.pack()


    def stop_entry(self):
        f_stop = tk.Frame(master=self)
        f_stop.pack()

        l_stop = tk.Label(master=f_stop, text="stop")
        l_stop.pack()

        self.e_stop = tk.Entry(master=f_stop)
        self.e_stop.pack()


    def name_entry(self):
        f_name = tk.Frame(master=self)
        f_name.pack()

        l_name = tk.Label(master=f_name, text="name")
        l_name.pack()

        self.e_name = tk.Entry(master=f_name)
        self.e_name.pack()


    def field_listbox(self):
        f_field = tk.Frame(master=self)
        f_field.pack()
        
        data = [
            ('field of study', 20),
            ('department', 20)
        ]
        self.list_fields = MultiListBox(master=f_field, data=data)
        self.list_fields.pack()
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
        f_room = tk.Frame(master=self)
        f_room.pack()

        data = [
            ('room number', 10),
            ('building', 20)
        ]
        self.list_rooms = MultiListBox(master=f_room, data=data)
        self.list_rooms.pack()
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
        f_group = tk.Frame(master=self)
        f_group.pack()
        
        data = [
            ('number',10),
            ('field of study', 20),
            ('department', 20),
            ('students', 10) #numbers of students
        ]

        self.list_groups = MultiListBox(master=f_group, data=data)
        self.refresh_exe_listbox()
        self.list_groups.pack()


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


            output = (
                group.get_number(),
                field,
                dept,
                len(group.get_students())
            )

            self.list_groups.insert(i, output)


    def teacher_listbox(self):
        f_teacher = tk.Frame(master=self)
        f_teacher.pack()

        data = [
            ('name', 10),
            ('lastname', 10)
        ]

        self.list_teachers = MultiListBox(master=f_teacher, data=data)
        self.list_teachers.pack()
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
        f_submit = tk.Frame(master=self)
        f_submit.pack()

        sub_btn = tk.Button(
            master=f_submit,
            text="submit",
            command=lambda : self.create_subject()
        )
        sub_btn.pack()


    def create_subject(self):
        teacher_idx = self.list_teachers.index(tk.ACTIVE)
        teacher = self.controller.teachers[teacher_idx]

        room_idx = self.list_rooms.index(tk.ACTIVE)
        room = self.controller.rooms[room_idx]

        field_idx = self.list_fields.index(tk.ACTIVE)
        field = self.controller.fields[field_idx]

        group_idx = self.list_groups.index(tk.ACTIVE)
        group = self.controller.exe_groups[group_idx]

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
        label.pack(side=tk.TOP, fill=tk.X, pady=10)


    def buttons(self):
        #Return Home Page
        btn_return = tk.Button(
            self,
            text="Return to Home Page",
            command=lambda : self.controller.show_frame("StartPage")
        )
        btn_return.pack()
        #Create Year Subject
        btn_create = tk.Button(
            self,
            text="Create Subject",
            command=lambda : self.create_subject()
        )
        btn_create.pack()
        #Delete Year Subject
        btn_delete = tk.Button(
            self,
            text="Delete Subject",
            command=lambda : self.delete_subject()
        )
        btn_delete.pack()


    def subject_listbox(self):
        f_subject = tk.Frame(master=self)
        f_subject.pack()
        l_subject = tk.Label(master=f_subject, text="select subject")
        l_subject.pack()

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

        self.list_subjects = MultiListBox(master=f_subject, data=data)
        self.refresh()
        self.list_subjects.pack()


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
        f_refresh = tk.Frame(master=self)
        f_refresh.pack()
        btn_refresh = tk.Button(
            master=f_refresh,
            text="refresh",
            command=lambda : self.restart()
        )
        btn_refresh.pack()


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
        label.pack(side=tk.TOP, fill=tk.X, pady=10)


    def return_button(self):
        btn_return = tk.Button(
            self,
            text="return",
            command=lambda : self.return_refresh()
        )
        btn_return.pack()


    def home_button(self):
        btn_home = tk.Button(
            self,
            text="Return to Home Page",
            command=lambda : self.home_refresh()
        )
        btn_home.pack()


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
        f_day = tk.Frame(master=self)
        f_day.pack()

        l_day = tk.Label(master=f_day, text="day")
        l_day.pack()

        self.e_day = tk.Entry(master=f_day)
        self.e_day.pack()


    def start_entry(self):
        f_start = tk.Frame(master=self)
        f_start.pack()

        l_start = tk.Label(master=f_start, text="start")
        l_start.pack()

        self.e_start = tk.Entry(master=f_start)
        self.e_start.pack()


    def stop_entry(self):
        f_stop = tk.Frame(master=self)
        f_stop.pack()

        l_stop = tk.Label(master=f_stop, text="stop")
        l_stop.pack()

        self.e_stop = tk.Entry(master=f_stop)
        self.e_stop.pack()


    def name_entry(self):
        f_name = tk.Frame(master=self)
        f_name.pack()

        l_name = tk.Label(master=f_name, text="name")
        l_name.pack()

        self.e_name = tk.Entry(master=f_name)
        self.e_name.pack()


    def field_listbox(self):
        f_field = tk.Frame(master=self)
        f_field.pack()
        
        data = [
            ('field of study', 20),
            ('department', 20)
        ]
        self.list_fields = MultiListBox(master=f_field, data=data)
        self.list_fields.pack()
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
        f_room = tk.Frame(master=self)
        f_room.pack()

        data = [
            ('room number', 10),
            ('building', 20)
        ]
        self.list_rooms = MultiListBox(master=f_room, data=data)
        self.list_rooms.pack()
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
        f_group = tk.Frame(master=self)
        f_group.pack()
        
        data = [
            ('number',10),
            ('field of study', 20),
            ('department', 20),
            ('students', 10) #numbers of students
        ]

        self.list_groups = MultiListBox(master=f_group, data=data)
        self.refresh_lab_listbox()
        self.list_groups.pack()


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


            output = (
                group.get_number(),
                field,
                dept,
                len(group.get_students())
            )

            self.list_groups.insert(i, output)


    def teacher_listbox(self):
        f_teacher = tk.Frame(master=self)
        f_teacher.pack()

        data = [
            ('name', 10),
            ('lastname', 10)
        ]

        self.list_teachers = MultiListBox(master=f_teacher, data=data)
        self.list_teachers.pack()
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
        f_submit = tk.Frame(master=self)
        f_submit.pack()

        sub_btn = tk.Button(
            master=f_submit,
            text="submit",
            command=lambda : self.create_subject()
        )
        sub_btn.pack()


    def create_subject(self):
        teacher_idx = self.list_teachers.index(tk.ACTIVE)
        teacher = self.controller.teachers[teacher_idx]

        room_idx = self.list_rooms.index(tk.ACTIVE)
        room = self.controller.rooms[room_idx]

        field_idx = self.list_fields.index(tk.ACTIVE)
        field = self.controller.fields[field_idx]

        group_idx = self.list_groups.index(tk.ACTIVE)
        group = self.controller.lab_groups[group_idx]

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
