import tkinter as tk

from Tables.Student import Student

from tk_extension.multilistBox import MultiListBox


class StudentPage(tk.Frame):
    """
    Main Student Page
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.columnconfigure([x for x in range(7)], minsize=250)
        self.rowconfigure([x for x in range(9)], minsize=100)
        self.controller = controller
        self.main_label()
        self.student_listbox()
        self.refresh_button()
        self.buttons()

    def main_label(self):
        """create student main label
        """
        label = tk.Label(
            self,
            text="Student Page",
            font=self.controller.title_font
        )
        label.grid(row=0, column=6, sticky="nsew", padx=5, pady=5)

    def buttons(self):
        """create room page buttons
        """
        # Return Home Button
        btn_return = tk.Button(
            self,
            text="Home",
            command=lambda: self.controller.show_frame("StartPage"),
            font=self.controller.normal_font,
        )
        btn_return.grid(row=4, column=6, sticky="nsew", padx=5, pady=5)
        # Create Student Button
        btn_create = tk.Button(
            self,
            text="Create Student",
            command=lambda: self.controller.show_frame("CreateStudentPage"),
            font=self.controller.normal_font,
        )
        btn_create.grid(row=1, column=6, sticky="nsew", padx=5, pady=5)
        # Delete Student Button
        btn_delete = tk.Button(
            self,
            text="Delete Student",
            command=lambda: self.delete_student(),
            font=self.controller.normal_font,
        )
        btn_delete.grid(row=2, column=6, sticky="nsew", padx=5, pady=5)
        # Change Student Button
        btn_change = tk.Button(
            self,
            text="Change Student",
            command=lambda: self.update_student(),
            font=self.controller.normal_font,
        )
        btn_change.grid(row=3, column=6, sticky="nsew", padx=5, pady=5)

    def student_listbox(self):
        """create student listbox
        """
        data = [
            ('id', 10),
            ('name', 15),
            ('second name', 15),
            ('lastname', 15),
            ('ssn', 15),
            ('email', 20),
            ('field of study', 20),
            ('department', 20),
            ('place of residence', 30)
        ]

        self.list_students = MultiListBox(master=self, data=data)
        self.refresh()
        self.list_students.grid(
            row=0,
            column=0,
            columnspan=6,
            rowspan=9,
            sticky="nswe",
            padx=5,
            pady=5
        )

    def delete_student(self):
        """create student listbox
        """
        idx = self.list_students.index(tk.ACTIVE)
        del_student = self.controller.students.pop(idx)

        del_student.delete(self.controller.db)
        self.delete_from_groups(del_student)
        self.controller.db.commit_conn()

        del del_student
        # config
        self.controller.frames["LabStudentPage"].refresh_student_listbox()
        self.controller.frames["ExeStudentPage"].refresh_student_listbox()
        self.controller.frames["YearStudentPage"].refresh_student_listbox()
        self.restart()

    def delete_from_groups(self, student):
        """func delete student from groups

        Args:
            student (Student): student which we want delete
        """
        # exe group
        for exe_group in self.controller.exe_groups:
            if student in exe_group.get_students():
                exe_group.delete_student(student, self.controller.db)
        # lab group
        for lab_group in self.controller.lab_groups:
            if student in lab_group.get_students():
                lab_group.delete_student(student, self.controller.db)
        # year group
        for year_group in self.controller.year_groups:
            if student in year_group.get_students():
                year_group.delete_student(student, self.controller.db)

    def update_student(self):
        """func set student to update and change
        page to ChangeStudentPage
        """
        idx = self.list_students.index(tk.ACTIVE)
        student = self.controller.students[idx]

        self.controller.frames["ChangeStudentPage"].set_student(student)
        self.controller.frames["ChangeStudentPage"].fill_entry()
        self.controller.show_frame("ChangeStudentPage")

    def restart(self):
        """func restart frame
        """
        self.refresh()
        self.controller.show_frame("StudentPage")

    def refresh_button(self):
        """create refresh button
        """
        btn_refresh = tk.Button(
            master=self,
            text="refresh",
            command=lambda: self.restart(),
            font=self.controller.normal_font,
        )
        btn_refresh.grid(row=8, column=6, sticky="nsew", padx=5, pady=5)

    def refresh(self):
        """func refresh student listbox
        """
        self.list_students.delete(0, tk.END)
        for i, student in enumerate(self.controller.students):
            try:
                field = student.get_field_of_study().get_name()
                try:
                    department = student.get_field_of_study().get_department().get_name()
                except AttributeError:
                    department = "NULL"
            except AttributeError:
                field = "NULL"
                department = "NULL"

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
            self.list_students.insert(i, output)


class CreateStudentPage(tk.Frame):
    """
    Page where we can create student
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.columnconfigure([x for x in range(9)], minsize=250)
        self.rowconfigure([x for x in range(18)], minsize=50)
        self.controller = controller
        self.main_label()
        self.return_button()
        self.home_button()
        self.name_entry()
        self.sec_name_entry()
        self.lastname_entry()
        self.ssn_entry()
        self.email_entry()
        self.place_entry()
        self.field_listbox()
        self.submit()

    def main_label(self):
        """create student main label
        """
        label = tk.Label(
            self,
            text="Create Student",
            font=self.controller.title_font
        )
        label.grid(
            row=0,
            column=0,
            rowspan=1,
            columnspan=4,
            sticky="news",
            padx=5,
            pady=5
        )

    def return_button(self):
        """create return button
        """
        btn_return = tk.Button(
            self,
            text="return",
            command=lambda: self.return_refresh(),
            font=self.controller.normal_font,
        )
        btn_return.grid(
            row=16,
            column=0,
            rowspan=2,
            columnspan=2,
            sticky="news",
            padx=5,
            pady=5
        )

    def home_button(self):
        """create home button
        """
        btn_home = tk.Button(
            self,
            text="Home",
            command=lambda: self.home_refresh(),
            font=self.controller.normal_font,
        )
        btn_home.grid(
            row=16,
            column=2,
            rowspan=2,
            columnspan=2,
            sticky="news",
            padx=5,
            pady=5
        )

    def return_refresh(self):
        """func change page to StudentPage
        """
        self.refresh()
        self.controller.show_frame("StudentPage")

    def home_refresh(self):
        """func change page to StartPage
        """
        self.refresh()
        self.controller.show_frame("StartPage")

    def refresh(self):
        """clear all entries
        """
        self.e_name.delete(0, tk.END)
        self.e_lastname.delete(0, tk.END)
        self.e_email.delete(0, tk.END)
        self.e_sec_name.delete(0, tk.END)
        self.e_place.delete(0, tk.END)
        self.e_ssn.delete(0, tk.END)

    def name_entry(self):
        """create entry for name with label
        """
        l_name = tk.Label(
            master=self,
            text="name",
            font=self.controller.normal_font,
            anchor=tk.W,
            relief=tk.RAISED
        )
        l_name.grid(
            row=1,
            column=0,
            columnspan=4,
            sticky="nswe",
            pady=0,
            padx=5
        )

        self.e_name = tk.Entry(
            master=self,
            font=self.controller.entry_font
        )
        self.e_name.grid(
            row=2,
            column=0,
            columnspan=4,
            sticky="nswe",
            pady=0,
            padx=5
        )

    def sec_name_entry(self):
        """create entry for second name with label
        """
        l_sec_name = tk.Label(
            master=self,
            text="second name",
            font=self.controller.normal_font,
            anchor=tk.W,
            relief=tk.RAISED
        )
        l_sec_name.grid(
            row=3,
            column=0,
            columnspan=4,
            sticky="nswe",
            pady=0,
            padx=5
        )

        self.e_sec_name = tk.Entry(
            master=self,
            font=self.controller.entry_font
        )
        self.e_sec_name.grid(
            row=4,
            column=0,
            columnspan=4,
            sticky="nswe",
            pady=0,
            padx=5
        )

    def lastname_entry(self):
        """create entry for lastname with label
        """
        l_lastname = tk.Label(
            master=self,
            text="lastname",
            font=self.controller.normal_font,
            anchor=tk.W,
            relief=tk.RAISED
        )
        l_lastname.grid(
            row=5,
            column=0,
            columnspan=4,
            sticky="nswe",
            pady=0,
            padx=5
        )

        self.e_lastname = tk.Entry(
            master=self,
            font=self.controller.entry_font
        )
        self.e_lastname.grid(
            row=6,
            column=0,
            columnspan=4,
            sticky="nswe",
            pady=0,
            padx=5
        )

    def ssn_entry(self):
        """create entry for ssn with label
        """
        l_ssn = tk.Label(
            master=self,
            text="ssn",
            font=self.controller.normal_font,
            anchor=tk.W,
            relief=tk.RAISED
        )
        l_ssn.grid(
            row=7,
            column=0,
            columnspan=4,
            sticky="nswe",
            pady=0,
            padx=5
        )

        self.e_ssn = tk.Entry(
            master=self,
            font=self.controller.entry_font
        )
        self.e_ssn.grid(
            row=8,
            column=0,
            columnspan=4,
            sticky="nswe",
            pady=0,
            padx=5
        )

    def email_entry(self):
        """create entry for email with label
        """
        l_email = tk.Label(
            master=self,
            text="email",
            font=self.controller.normal_font,
            anchor=tk.W,
            relief=tk.RAISED
        )
        l_email.grid(
            row=9,
            column=0,
            columnspan=4,
            sticky="nswe",
            pady=0,
            padx=5
        )

        self.e_email = tk.Entry(
            master=self,
            font=self.controller.entry_font
        )
        self.e_email.grid(
            row=10,
            column=0,
            columnspan=4,
            sticky="nswe",
            pady=0,
            padx=5
        )

    def place_entry(self):
        """create entry for place of residence with label
        """
        l_place = tk.Label(
            master=self,
            text="place of residence",
            font=self.controller.normal_font,
            anchor=tk.W,
            relief=tk.RAISED
        )
        l_place.grid(
            row=11,
            column=0,
            columnspan=4,
            sticky="nswe",
            pady=0,
            padx=5
        )

        self.e_place = tk.Entry(
            master=self,
            font=self.controller.entry_font
        )
        self.e_place.grid(
            row=12,
            column=0,
            columnspan=4,
            sticky="nswe",
            pady=0,
            padx=5
        )

    def field_listbox(self):
        """create field of study listbox for Student Page
        """
        l_field = tk.Label(
            master=self,
            text="field of study",
            font=self.controller.normal_font,
            relief=tk.RAISED
        )
        l_field.grid(
            row=0,
            column=4,
            rowspan=1,
            columnspan=3,
            sticky="nswe",
            pady=5,
            padx=5
        )

        data = [
            ('field of study', 20),
            ('department', 20)
        ]

        self.list_field = MultiListBox(master=self, data=data)
        self.list_field.grid(
            row=1,
            column=4,
            rowspan=17,
            columnspan=3,
            sticky="nswe",
            pady=5,
            padx=5
        )
        self.refresh_field_listbox()

    def refresh_field_listbox(self):
        """refresh field of study listbox
        """
        self.list_field.delete(0, tk.END)
        for i, field in enumerate(self.controller.fields):
            try:
                dept = field.get_department().get_name()
            except AttributeError:
                dept = "NULL"

            output = (
                field.get_name(),
                dept
            )
            self.list_field.insert(i, output)

    def submit(self):
        """create submit button
        """
        sub_btn = tk.Button(
            master=self,
            text="submit",
            command=lambda: self.create_student(),
            font=self.controller.normal_font,
        )
        sub_btn.grid(
            row=14,
            column=0,
            rowspan=2,
            columnspan=4,
            sticky="nswe",
            pady=5,
            padx=5
        )

    def create_student(self):
        """func create new student and config other frames
        """
        try:
            idx = self.list_field.index(tk.ACTIVE)
            temp_field = self.controller.fields[idx]
        except IndexError:
            temp_field = None

        try:
            ssn = int(self.e_ssn.get())
        except ValueError:
            ssn = 'NULL'

        self.controller.students.append(Student(
            name=self.e_name.get(),
            sec_name=self.e_sec_name.get(),
            lastname=self.e_lastname.get(),
            ssn=ssn,
            email=self.e_email.get(),
            field_of_study=temp_field,
            place_of_residence=self.e_place.get()
        ))

        # insert to db
        self.controller.students[-1].insert(self.controller.db)
        self.controller.db.commit_conn()
        # refresh Groups frames
        self.controller.frames["LabStudentPage"].refresh_student_listbox()
        self.controller.frames["ExeStudentPage"].refresh_student_listbox()
        self.controller.frames["YearStudentPage"].refresh_student_listbox()
        # refresh self
        self.refresh()
        self.controller.frames["StudentPage"].restart()


class ChangeStudentPage(CreateStudentPage):
    """
    Page where we can update Student
    """
    def __init__(self, parent, controller):
        CreateStudentPage.__init__(self, parent, controller)
        if controller.students:
            self.student = controller.students[0]

    def main_label(self):
        """create update student main label
        """
        label = tk.Label(
            self,
            text="Change Student",
            font=self.controller.title_font
        )
        label.grid(
            row=0,
            column=0,
            rowspan=1,
            columnspan=4,
            sticky="news",
            padx=5,
            pady=5
        )

    def submit(self):
        """crate submit button
        """
        sub_btn = tk.Button(
            master=self,
            text="submit",
            command=lambda: self.update_student(),
            font=self.controller.normal_font,
        )
        sub_btn.grid(
            row=14,
            column=0,
            rowspan=2,
            columnspan=4,
            sticky="news",
            padx=5,
            pady=5
        )

    def fill_entry(self):
        """fill all entries with self attrs
        """
        self.e_name.insert(tk.END, str(self.student.get_name()))
        self.e_lastname.insert(tk.END, str(self.student.get_lastname()))
        self.e_email.insert(tk.END, str(self.student.get_email()))
        self.e_sec_name.insert(tk.END, str(self.student.get_sec_name()))
        self.e_place.insert(tk.END, str(self.student.get_place_of_residence()))
        self.e_ssn.insert(tk.END, str(self.student.get_ssn()))

    def set_student(self, student):
        """set student instance

        Args:
            student (Student): student which we want update
        """
        self.student = student

    def update_student(self):
        """func update student and config other frames
        """
        self.set_attr_student()
        self.student.update(self.controller.db)
        self.controller.db.commit_conn()

        # config after update
        self.controller.frames["LabStudentPage"].refresh_student_listbox()
        self.controller.frames["ExeStudentPage"].refresh_student_listbox()
        self.controller.frames["YearStudentPage"].refresh_student_listbox()
        self.refresh()
        self.controller.frames["StudentPage"].restart()

    def set_attr_student(self):
        """changes attrs of student
        """
        try:
            idx = self.list_field.index(tk.ACTIVE)
            field = self.controller.fields[idx]
            self.student.set_field_of_study(field)
        except IndexError:
            pass

        self.student.set_name(self.e_name.get())
        self.student.set_sec_name(self.e_sec_name.get())
        self.student.set_lastname(self.e_lastname.get())
        self.student.set_ssn(int(self.e_ssn.get()))
        self.student.set_email(self.e_email.get())
        self.student.set_place_of_residence(self.e_place.get())
