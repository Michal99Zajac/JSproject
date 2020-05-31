import tkinter as tk

from Tables.Student import Student

from tk_extension.multilistBox import MultiListBox

class StudentPage(tk.Frame):
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
        label = tk.Label(
            self,
            text="Student Page",
            font=self.controller.title_font
        )
        label.grid(row = 0, column = 6, sticky="nsew", padx=5, pady=5)

    def buttons(self):
        #Return Home Button
        btn_return = tk.Button(
            self,
            text="Return to Home Page",
            command=lambda: self.controller.show_frame("StartPage")
        )
        btn_return.grid(row=4, column=6, sticky="nsew", padx=5, pady=5)
        #Create Student Button
        btn_create = tk.Button(
            self,
            text="Create Student",
            command=lambda: self.controller.show_frame("CreateStudentPage")
        )
        btn_create.grid(row=1, column=6, sticky="nsew", padx=5, pady=5)
        #Delete Student Button
        btn_delete = tk.Button(
            self,
            text="Delete Student",
            command=lambda: self.delete_student()
        )
        btn_delete.grid(row=2, column=6, sticky="nsew", padx=5, pady=5)
        #Change Student Button
        btn_change = tk.Button(
            self,
            text="Change Student",
            command=lambda: self.update_student()
        )
        btn_change.grid(row=3, column=6, sticky="nsew", padx=5, pady=5)


    def student_listbox(self):
        #f_student = tk.Frame(master=self)
        #f_student.grid(row=0, column=0, sticky=tk.NW, padx=5, pady=5)
        #l_student = tk.Label(master=f_student, text="select student")
        #l_student.pack()

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
        self.list_students.grid(row=0, column=0, columnspan=6, rowspan=9, sticky="nswe", padx=5, pady=5)


    def delete_student(self):
        idx = self.list_students.index(tk.ACTIVE)
        del_student = self.controller.students.pop(idx)

        del_student.delete(self.controller.db)
        self.delete_from_groups(del_student)
        self.controller.db.commit_conn()

        del del_student

        self.controller.frames["LabAddStudentPage"].refresh_student_listbox()
        self.controller.frames["LabStudentPage"].refresh_student_listbox()
        self.controller.frames["ExeAddStudentPage"].refresh_student_listbox()
        self.controller.frames["ExeStudentPage"].refresh_student_listbox()
        self.controller.frames["YearAddStudentPage"].refresh_student_listbox()
        self.controller.frames["YearStudentPage"].refresh_student_listbox()
        self.restart()


    def delete_from_groups(self, student):
        #exe group
        for exe_group in self.controller.exe_groups:
            if student in exe_group.get_students():
                exe_group.delete_student(student, self.controller.db)

        #lab group
        for lab_group in self.controller.lab_groups:
            if student in lab_group.get_students():
                lab_group.delete_student(student, self.controller.db)

        #year group
        for year_group in self.controller.year_groups:
            if student in year_group.get_students():
                year_group.delete_student(student, self.controller.db)


    def update_student(self):
        idx = self.list_students.index(tk.ACTIVE)
        student = self.controller.students[idx]
       
        self.controller.frames["ChangeStudentPage"].set_student(student)
        self.controller.frames["ChangeStudentPage"].fill_entry()
        self.controller.show_frame("ChangeStudentPage")


    def restart(self):
        self.refresh()
        self.controller.show_frame("StudentPage")


    def refresh_button(self):
        btn_refresh = tk.Button(master=self, text="refresh", command=lambda : self.restart())
        btn_refresh.grid(row=8, column=6, sticky="nsew", padx=5, pady=5)


    def refresh(self):
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
        


class CreateStudentPage(tk.Frame):
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
        label = tk.Label(
            self,
            text="Create Student",
            font=self.controller.title_font
        )
        label.grid(row=0, column=0, rowspan=1, columnspan=4, sticky="news", padx=5, pady=5)


    def return_button(self):
        btn_return = tk.Button(
            self,
            text="return",
            command=lambda: self.return_refresh()
        )
        btn_return.grid(row=15, column=0, rowspan=2, columnspan=2, sticky="news", padx=5, pady=5)


    def home_button(self):
        btn_home = tk.Button(
            self,
            text="Home Page",
            command=lambda: self.home_refresh()
        )
        btn_home.grid(row=15, column=2,rowspan=2, columnspan=2, sticky="news", padx=5, pady=5)


    def return_refresh(self):
        self.refresh()
        self.controller.show_frame("StudentPage")


    def home_refresh(self):
        self.refresh()
        self.controller.show_frame("StartPage")

    
    def refresh(self):
        self.e_name.delete(0, tk.END)
        self.e_lastname.delete(0, tk.END)
        self.e_email.delete(0, tk.END)
        self.e_sec_name.delete(0, tk.END)
        self.e_place.delete(0, tk.END)
        self.e_ssn.delete(0, tk.END)


    def name_entry(self):
        # f_name = tk.Frame(master=self)
        # f_name.rowconfigure([0,1], minsize=50)
        # f_name.columnconfigure([x for x in range(4)], minsize=200)
        # f_name.grid(row=1, column=0, columnspan=4, sticky="news", padx=5, pady=5)

        l_name = tk.Label(master=self, text="name")
        l_name.grid(row=1, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)

        self.e_name = tk.Entry(master=self)
        self.e_name.grid(row=2, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)
        

    def sec_name_entry(self):
        #f_sec_name = tk.Frame(master=self)
        #f_sec_name.pack()

        l_sec_name = tk.Label(master=self, text="second name")
        l_sec_name.grid(row=3, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)

        self.e_sec_name = tk.Entry(master=self)
        self.e_sec_name.grid(row=4, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)


    def lastname_entry(self):
        #f_lastname = tk.Frame(master=self)
        #f_lastname.pack()

        l_lastname = tk.Label(master=self, text="lastname")
        l_lastname.grid(row=5, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)

        self.e_lastname = tk.Entry(master=self)
        self.e_lastname.grid(row=6, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)


    def ssn_entry(self):
        #f_ssn = tk.Frame(master=self)
        #f_ssn.pack()

        l_ssn = tk.Label(master=self, text="ssn")
        l_ssn.grid(row=7, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)

        self.e_ssn = tk.Entry(master=self)
        self.e_ssn.grid(row=8, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)


    def email_entry(self):
        #f_email = tk.Frame(master=self)
        #f_email.pack()

        l_email = tk.Label(master=self, text="email")
        l_email.grid(row=9, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)

        self.e_email = tk.Entry(master=self)
        self.e_email.grid(row=10, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)


    def place_entry(self):
        #f_place = tk.Frame(master=self)
        #f_place.pack()

        l_place = tk.Label(master=self, text="place of residence")
        l_place.grid(row=11, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)

        self.e_place = tk.Entry(master=self)
        self.e_place.grid(row=12, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)


    def field_listbox(self):
        #f_field = tk.Frame(master=self)
        #f_field.pack()

        l_field = tk.Label(master=self, text="field of study")
        l_field.grid(row=0, column=4, rowspan=1, columnspan=3, sticky="nswe", pady=5, padx=5)

        data = [
            ('field of study', 20),
            ('department', 20)
        ]

        self.list_field = MultiListBox(master=self, data=data)
        self.list_field.grid(row=1, column=4, rowspan=16, columnspan=3, sticky="nswe", pady=5, padx=5)
        self.refresh_field_listbox()


    def refresh_field_listbox(self):
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
        #f_submit = tk.Frame(master=self)
        #f_submit.pack()

        sub_btn = tk.Button(
            master=self,
            text="submit",
            command=lambda : self.create_student()
            )
        sub_btn.grid(row=13, column=0, rowspan=2, columnspan=4, sticky="nswe", pady=5, padx=5)
        

    def create_student(self):
        idx = self.list_field.index(tk.ACTIVE)
        temp_field = self.controller.fields[idx]

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
        
        self.controller.students[-1].insert(self.controller.db)
        self.controller.db.commit_conn()
        self.controller.frames["LabStudentPage"].refresh_student_listbox()
        self.controller.frames["ExeStudentPage"].refresh_student_listbox()
        self.controller.frames["YearStudentPage"].refresh_student_listbox()
        self.refresh()
        self.controller.frames["StudentPage"].restart()


class ChangeStudentPage(CreateStudentPage):
    def __init__(self, parent, controller):
        CreateStudentPage.__init__(self, parent, controller)
        if controller.students:
            self.student = controller.students[0]


    def main_label(self):
        label = tk.Label(
            self,
            text="Change Student",
            font=self.controller.title_font
        )
        #label.pack(side=tk.TOP, fill=tk.X, pady=10)


    def submit(self):
        f_submit = tk.Frame(master=self)
        #f_submit.pack()

        sub_btn = tk.Button(
            master=f_submit,
            text="submit",
            command=lambda:self.update_student()
            )
        #sub_btn.pack()
        

    def fill_entry(self):
        self.e_name.insert(tk.END, str(self.student.get_name()))
        self.e_lastname.insert(tk.END, str(self.student.get_lastname()))
        self.e_email.insert(tk.END, str(self.student.get_email()))
        self.e_sec_name.insert(tk.END, str(self.student.get_sec_name()))
        self.e_place.insert(tk.END, str(self.student.get_place_of_residence()))
        self.e_ssn.insert(tk.END, str(self.student.get_ssn()))


    def set_student(self, student):
        self.student = student


    def update_student(self):
        self.set_attr_student()
        self.student.update(self.controller.db)
        self.controller.db.commit_conn()

        #config after update
        self.controller.frames["LabStudentPage"].refresh_student_listbox()
        self.controller.frames["ExeStudentPage"].refresh_student_listbox()
        self.controller.frames["YearStudentPage"].refresh_student_listbox()
        self.refresh()
        self.controller.frames["StudentPage"].restart()

    def set_attr_student(self):
        for field in self.controller.fields:
            if self.list_field.get(tk.ACTIVE) == field.get_name():
                self.student.set_field_of_study(field)
                break

        self.student.set_name(self.e_name.get())
        self.student.set_sec_name(self.e_sec_name.get())
        self.student.set_lastname(self.e_lastname.get())
        self.student.set_ssn(int(self.e_ssn.get()))
        self.student.set_email(self.e_email.get())
        self.student.set_place_of_residence(self.e_place.get())