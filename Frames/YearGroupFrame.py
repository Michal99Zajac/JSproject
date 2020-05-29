import tkinter as tk

from Tables.YearGroup import YearGroup

from Frames.extendTk import MultiListBox


class YearGroupPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.main_label()

        self.group_listbox()
        self.refresh_button()
        self.buttons()


    def main_label(self):
        label = tk.Label(
            self,
            text="Year Group Page",
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
        #Create Year Group Button
        btn_create = tk.Button(
            self,
            text="Create Group",
            command=lambda : self.create_group()
        )
        btn_create.pack()
        #Delete Year Group Button
        btn_delete = tk.Button(
            self,
            text="Delete Group",
            command=lambda : self.delete_group()
        )
        btn_delete.pack()
        #Show Year Group Button
        btn_show = tk.Button(
            self,
            text="Show Group",
            command=lambda : self.show_group()
        )
        btn_show.pack()


    def group_listbox(self):
        f_group = tk.Frame(master=self)
        f_group.pack()
        l_group = tk.Label(master=f_group, text="select group")
        l_group.pack()

        data = [
            ('number',10),
            ('field of study', 20),
            ('department', 20),
            ('students', 10) #numbers of students
        ]

        self.list_groups = MultiListBox(master=f_group, data=data)
        self.refresh()
        self.list_groups.pack()


    def create_group(self):
        self.controller.show_frame("CreateYearGroupPage")


    def delete_group(self):
        idx = self.list_groups.index(tk.ACTIVE)
        del_group = self.controller.year_groups.pop(idx)

        del_group.delete(self.controller.db)
        self.controller.db.commit_conn()

        del del_group

        #refresh create subject lab group listbox
        #refresh update subject lab group listbox
        #refresh subject

        self.controller.frames["YearAddStudentPage"].refresh_student_listbox()
        self.restart()


    def show_group(self):
        idx = self.list_groups.index(tk.ACTIVE)
        group = self.controller.year_groups[idx]

        self.controller.frames["YearStudentPage"].set_group(group)
        self.controller.frames["YearStudentPage"].refresh_student_listbox()
        self.controller.show_frame("YearStudentPage")


    def restart(self):
        self.refresh()
        self.controller.show_frame("YearGroupPage")


    def refresh_button(self):
        f_refresh = tk.Frame(master=self)
        f_refresh.pack()
        btn_refresh = tk.Button(
            master=f_refresh,
            text="refresh",
            command=lambda : self.restart()
        )
        btn_refresh.pack()


    def refresh(self):
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



class CreateYearGroupPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.main_label()
        self.return_button()
        self.home_button()

        self.number_entry()
        self.field_listbox()
        self.submit()

    
    def main_label(self):
        label = tk.Label(
            self,
            text="Create Group",
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
        self.controller.show_frame("YearGroupPage")


    def home_refresh(self):
        self.refresh()
        self.controller.show_frame("StartPage")


    def refresh(self):
        self.e_number.delete(0, tk.END)


    def number_entry(self):
        f_number = tk.Frame(master=self)
        f_number.pack()

        l_number = tk.Label(master=f_number, text="number")
        l_number.pack()

        self.e_number = tk.Entry(master=f_number)
        self.e_number.pack()


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

    
    def submit(self):
        f_submit = tk.Frame(master=self)
        f_submit.pack()

        sub_btn = tk.Button(
            master=f_submit,
            text="submit",
            command=lambda : self.create_group()
        )
        sub_btn.pack()


    def create_group(self):
        idx = self.list_fields.index(tk.ACTIVE)
        
        field = self.controller.fields[idx]

        self.controller.year_groups.append(YearGroup(
            number=self.e_number.get(),
            field=field
        ))

        #update Subject

        self.refresh()
        self.controller.db.commit_conn()
        self.controller.frames["YearGroupPage"].restart()



class YearStudentPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        if controller.year_groups:
            self.group = controller.year_groups[0]

        self.controller = controller
        
        self.main_label()
        self.return_button()
        self.home_button()

        self.add_button()
        self.delete_button()
        self.student_listbox()


    def set_group(self, group):
        self.group = group


    def main_label(self):
        label = tk.Label(
            self,
            text="Year Group",
            font=self.controller.title_font
        )
        label.pack(side=tk.TOP, fill=tk.X, pady=10)


    def return_button(self):
        btn_return = tk.Button(
            self,
            text="return",
            command=lambda : self.controller.show_frame("YearGroupPage")
        )
        btn_return.pack()

    
    def home_button(self):
        btn_home = tk.Button(
            self,
            text="Return to Home Page",
            command=lambda : self.controller.show_frame("StartPage")
        )
        btn_home.pack()


    def student_listbox(self):
        f_student = tk.Frame(master=self)
        f_student.pack()
        l_student = tk.Label(master=f_student, text="select student")
        l_student.pack()

        data = [
            ('id', 10),
            ('name', 20),
            ('second name', 20),
            ('lastname', 20),
            ('ssn', 20),
            ('email', 20),
            ('field of study', 30),
            ('department', 20),
            ('place of residence', 40)
        ]

        self.list_students = MultiListBox(master=f_student, data=data)
        self.list_students.pack()
        self.refresh_student_listbox()


    def refresh_student_listbox(self):
        self.list_students.delete(0, tk.END)
        try:
            for i, student in enumerate(self.group.get_students()):
                try:
                    field = student.get_field_of_study().get_name()
                    try:
                        department = student.get_field_of_study().get_department().get_name()
                    except AttributeError:
                        department = "NULL"
                except AttributeError:
                    field = "NULL"

                output = (
                    student.get_id(),
                    student.get_name(),
                    student.get_sec_name(),
                    student.get_lastname(),
                    student.get_ssn(),
                    student.get_email(),
                    field,
                    department,
                    student.get_place_of_residence()
                    )
                self.list_students.insert(i,output)
        except AttributeError:
            pass


    def add_button(self):
        add_btn = tk.Button(
            master=self,
            text="add Student",
            command=lambda : self.add_student()
        )
        add_btn.pack()


    def delete_button(self):
        delete_btn = tk.Button(
            master=self,
            text="del Student",
            command=lambda : self.del_student()
        )
        delete_btn.pack()


    def add_student(self):
        self.controller.frames["YearAddStudentPage"].set_group(self.group)
        self.controller.frames["YearAddStudentPage"].refresh_student_listbox()
        self.controller.show_frame("YearAddStudentPage")


    def del_student(self):
        idx = self.list_students.index(tk.ACTIVE)
        student = list(self.group.get_students())[idx]

        self.group.delete_student(student, self.controller.db)
        self.controller.db.commit_conn()

        self.controller.frames["YearGroupPage"].refresh()
        self.refresh_student_listbox()



class YearAddStudentPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        if self.controller.lab_groups:
            self.group = self.controller.lab_groups[0]

        self.main_label()
        self.return_button()
        self.student_listbox()
        self.submit()


    def set_group(self, group):
        self.group = group

    
    def main_label(self):
        label = tk.Label(
            self,
            text="Add Student",
            font=self.controller.title_font
        )
        label.pack(side=tk.TOP, fill=tk.X, pady=10)


    def student_listbox(self):
        f_student = tk.Frame(master=self)
        f_student.pack()
        l_student = tk.Label(master=f_student, text="select student")
        l_student.pack()

        data = [
            ('id', 10),
            ('name', 20),
            ('second name', 20),
            ('lastname', 20),
            ('ssn', 20),
            ('email', 20),
            ('field of study', 30),
            ('department', 20),
            ('place of residence', 40)
        ]

        self.list_students = MultiListBox(master=f_student, data=data)
        self.list_students.pack()


    def return_button(self):
        btn_return = tk.Button(
            self,
            text="return",
            command=lambda : self.controller.show_frame("YearStudentPage")
        )
        btn_return.pack()


    def refresh_student_listbox(self):
        self.list_students.delete(0, tk.END)
        for i, student in enumerate(self.avi_students()):
                try:
                    field = student.get_field_of_study().get_name()
                    try:
                        department = student.get_field_of_study().get_department().get_name()
                    except AttributeError:
                        department = "NULL"
                except AttributeError:
                    field = "NULL"

                output = (
                    student.get_id(),
                    student.get_name(),
                    student.get_sec_name(),
                    student.get_lastname(),
                    student.get_ssn(),
                    student.get_email(),
                    field,
                    department,
                    student.get_place_of_residence()
                    )
                self.list_students.insert(i,output)


    def avi_students(self):
        return [student for student in self.controller.students if student not in YearGroup.all_students and student.get_field_of_study() == self.group.get_field()]


    def submit(self):
        sub_btn = tk.Button(
            master=self,
            text="submit",
            command=lambda : self.add_student()
        )
        sub_btn.pack()


    def add_student(self):
        idx = self.list_students.index(tk.ACTIVE)
        student = self.avi_students()[idx]
        self.group.insert(student, self.controller.db)
        self.controller.db.commit_conn()

        self.controller.frames["YearStudentPage"].refresh_student_listbox()
        self.controller.frames["YearGroupPage"].refresh()
        self.controller.show_frame("YearStudentPage")