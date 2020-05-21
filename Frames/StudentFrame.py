import tkinter as tk

from Tables.Student import Student

from Frames.extendTk import MultiListBox

class StudentPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
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
        label.pack(side=tk.TOP, fill=tk.X, pady=10)

    def buttons(self):
        #Return Home Button
        btn_return = tk.Button(
            self,
            text="Return to Home Page",
            command=lambda: self.controller.show_frame("StartPage")
        )
        btn_return.pack()
        #Create Student Button
        btn_create = tk.Button(
            self,
            text="Create Student",
            command=lambda: self.controller.show_frame("CreateStudentPage")
        )
        btn_create.pack()
        #Delete Student Button
        btn_delete = tk.Button(
            self,
            text="Delete Student",
            command=lambda: self.delete_student()
        )
        btn_delete.pack()
        #Change Student Button
        btn_change = tk.Button(
            self,
            text="Change Student",
            command=lambda: self.update_student()
        )
        btn_change.pack()


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
            ('place of residence', 40)
        ]

        self.list_students = MultiListBox(master=f_student, data=data)
        self.refresh()
        self.list_students.pack()


    def delete_student(self):
        idx = self.list_students.index(tk.ACTIVE)
        del_student = self.controller.students.pop(idx)

        del_student.delete(self.controller.db)
        self.delete_from_groups(del_student)
        self.controller.db.commit_conn()

        del del_student
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
        f_refresh = tk.Frame(master=self)
        f_refresh.pack()
        btn_refresh = tk.Button(master=f_refresh, text="refresh", command=lambda : self.restart())
        btn_refresh.pack()


    def refresh(self):
        self.list_students.delete(0, tk.END)
        for i, student in enumerate(self.controller.students):
            output = (
                student.get_id(),
                student.get_name(),
                student.get_sec_name(),
                student.get_lastname(),
                student.get_ssn(),
                student.get_email(),
                student.get_field_of_study().get_name(),
                student.get_place_of_residence()
                )
            self.list_students.insert(i,output)
        


class CreateStudentPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
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
        label.pack(side=tk.TOP, fill=tk.X, pady=10)


    def return_button(self):
        btn_return = tk.Button(
            self,
            text="return",
            command=lambda: self.return_refresh()
        )
        btn_return.pack()


    def home_button(self):
        btn_home = tk.Button(
            self,
            text="Return to Home Page",
            command=lambda: self.home_refresh()
        )
        btn_home.pack()


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
        f_name = tk.Frame(master=self)
        f_name.pack()

        l_name = tk.Label(master=f_name, text="name")
        l_name.pack()

        self.e_name = tk.Entry(master=f_name)
        self.e_name.pack()
        

    def sec_name_entry(self):
        f_sec_name = tk.Frame(master=self)
        f_sec_name.pack()

        l_sec_name = tk.Label(master=f_sec_name, text="second name")
        l_sec_name.pack()

        self.e_sec_name = tk.Entry(master=f_sec_name)
        self.e_sec_name.pack()


    def lastname_entry(self):
        f_lastname = tk.Frame(master=self)
        f_lastname.pack()

        l_lastname = tk.Label(master=f_lastname, text="lastname")
        l_lastname.pack()

        self.e_lastname = tk.Entry(master=f_lastname)
        self.e_lastname.pack()


    def ssn_entry(self):
        f_ssn = tk.Frame(master=self)
        f_ssn.pack()

        l_ssn = tk.Label(master=f_ssn, text="ssn")
        l_ssn.pack()

        self.e_ssn = tk.Entry(master=f_ssn)
        self.e_ssn.pack()


    def email_entry(self):
        f_email = tk.Frame(master=self)
        f_email.pack()

        l_email = tk.Label(master=f_email, text="email")
        l_email.pack()

        self.e_email = tk.Entry(master=f_email)
        self.e_email.pack()


    def place_entry(self):
        f_place = tk.Frame(master=self)
        f_place.pack()

        l_place = tk.Label(master=f_place, text="place of residence")
        l_place.pack()

        self.e_place = tk.Entry(master=f_place)
        self.e_place.pack()


    def field_listbox(self):
        f_field = tk.Frame(master=self)
        f_field.pack()

        l_field = tk.Label(master=f_field, text="field of study")
        l_field.pack()

        self.list_field = tk.Listbox(master=f_field)  
        for i, field in enumerate(self.controller.fields):
            self.list_field.insert(i,field.get_name())
        self.list_field.pack()


    def submit(self):
        f_submit = tk.Frame(master=self)
        f_submit.pack()

        sub_btn = tk.Button(
            master=f_submit,
            text="submit",
            command=lambda : self.create_student()
            )
        sub_btn.pack()
        

    def create_student(self):
        temp_field = None
        for field in self.controller.fields:
            if self.list_field.get(tk.ACTIVE) == field.get_name():
                temp_field = field
                break
        
        self.controller.students.append(Student(
            name=self.e_name.get(),
            sec_name=self.e_sec_name.get(),
            lastname=self.e_lastname.get(),
            ssn=int(self.e_ssn.get()),
            email=self.e_email.get(),
            field_of_study=temp_field,
            place_of_residence=self.e_place.get()
        ))
        
        self.controller.students[-1].insert(self.controller.db)
        self.controller.db.commit_conn()
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
        label.pack(side=tk.TOP, fill=tk.X, pady=10)


    def submit(self):
        f_submit = tk.Frame(master=self)
        f_submit.pack()

        sub_btn = tk.Button(
            master=f_submit,
            text="submit",
            command=lambda:self.update_student()
            )
        sub_btn.pack()
        

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