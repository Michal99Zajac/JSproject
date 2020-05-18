import tkinter as tk
from tkinter import font as tkfont
from Tables.Student import Student

class StudentPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(
            self,
            text="Student Page",
            font=controller.title_font
        )
        label.pack(side=tk.TOP, fill=tk.X, pady=10)

        #Return Home Button
        btn_1 = tk.Button(
            self,
            text="Return to Home Page",
            command=lambda:controller.show_frame("StartPage")
        )
        #Create Student Button
        btn_2 = tk.Button(
            self,
            text="Create Student",
            command=lambda:controller.show_frame("CreateStudentPage")
        )
        #Delete Student Button
        btn_3 = tk.Button(
            self,
            text="Delete Student",
            command=lambda:controller.show_frame("DeleteStudentPage")
        )
        #Change Student Button
        btn_4 = tk.Button(
            self,
            text="Change Student",
            command=lambda:controller.show_frame("ChangeStudentPage")
        )
        #Show All Student Button
        btn_5 = tk.Button(
            self,
            text="Show Students",
            command=lambda:controller.show_frame("ShowStudentsPage")
        )
        btn_1.pack()
        btn_2.pack()
        btn_3.pack()
        btn_4.pack()
        btn_5.pack()

class DeleteStudentPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        label = tk.Label(
            self,
            text="Delete Student",
            font=controller.title_font
        )
        label.pack(side=tk.TOP, fill=tk.X, pady=10)
        btn1 = tk.Button(
            self,
            text="Return to Home Page",
            command=lambda:controller.show_frame("StartPage")
        )
        btn2 = tk.Button(
            self,
            text="return",
            command=lambda:controller.show_frame("StudentPage")
        )
        btn1.pack()
        btn2.pack()

class CreateStudentPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.returns_buttons()
        self.name_entry()
        self.sec_name_entry()
        self.lastname_entry()
        self.ssn_entry()
        self.email_entry()
        self.place_entry()
        self.field_listbox()
        self.submit()

    def returns_buttons(self):
        label = tk.Label(
            self,
            text="Create Student",
            font=self.controller.title_font
        )
        label.pack(side=tk.TOP, fill=tk.X, pady=10)
        btn1 = tk.Button(
            self,
            text="Return to Home Page",
            command=lambda:self.controller.show_frame("StartPage")
        )
        btn2 = tk.Button(
            self,
            text="return",
            command=lambda:self.controller.show_frame("StudentPage")
        )
        btn1.pack()
        btn2.pack()

    def name_entry(self):
        self.f_name = tk.Frame(master=self)
        self.l_name = tk.Label(master=self.f_name, text="name")
        self.l_name.pack()
        self.e_name = tk.Entry(master=self.f_name)
        self.e_name.pack()
        self.f_name.pack()

    def sec_name_entry(self):
        self.f_sec_name = tk.Frame(master=self)
        self.l_sec_name = tk.Label(master=self.f_sec_name, text="second name")
        self.l_sec_name.pack()
        self.e_sec_name = tk.Entry(master=self.f_sec_name)
        self.e_sec_name.pack()
        self.f_sec_name.pack()

    def lastname_entry(self):
        self.f_lastname = tk.Frame(master=self)
        self.l_lastname = tk.Label(master=self.f_lastname, text="lastname")
        self.l_lastname.pack()
        self.e_lastname = tk.Entry(master=self.f_lastname)
        self.e_lastname.pack()
        self.f_lastname.pack()

    def ssn_entry(self):
        self.f_ssn = tk.Frame(master=self)
        self.l_ssn = tk.Label(master=self.f_ssn, text="ssn")
        self.l_ssn.pack()
        self.e_ssn = tk.Entry(master=self.f_ssn)
        self.e_ssn.pack()
        self.f_ssn.pack()

    def email_entry(self):
        self.f_email = tk.Frame(master=self)
        self.l_email = tk.Label(master=self.f_email, text="email")
        self.l_email.pack()
        self.e_email = tk.Entry(master=self.f_email)
        self.e_email.pack()
        self.f_email.pack()

    def place_entry(self):
        self.f_place = tk.Frame(master=self)
        self.l_place = tk.Label(master=self.f_place, text="place of residence")
        self.l_place.pack()
        self.e_place = tk.Entry(master=self.f_place)
        self.e_place.pack()
        self.f_place.pack()

    def field_listbox(self):
        self.f_field = tk.Frame(master=self)
        self.l_field = tk.Label(master=self.f_field, text="field of study")
        self.l_field.pack()
        self.list_field = tk.Listbox(master=self.f_field)
        
        for i, field in enumerate(self.controller.fields):
            self.list_field.insert(i,field.get_name())
        
        self.list_field.pack()
        self.f_field.pack()

    def submit(self):
        self.f_submit = tk.Frame(master=self)
        self.sub_btn = tk.Button(
            master=self.f_submit,
            text="submit",
            command=lambda:self.create_student()
            )
        self.sub_btn.pack()
        self.f_submit.pack()

    def create_student(self):
        print(self.controller.students)
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
        ).insert(self.controller.db))
        
        self.controller.db.commit_conn()
        print(self.controller.students)


class ChangeStudentPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(
            self,
            text="Change Student",
            font=controller.title_font
        )
        label.pack(side=tk.TOP, fill=tk.X, pady=10)
        btn1 = tk.Button(
            self,
            text="Return to Home Page",
            command=lambda:controller.show_frame("StartPage")
        )
        btn2 = tk.Button(
            self,
            text="return",
            command=lambda:controller.show_frame("StudentPage")
        )
        btn1.pack()
        btn2.pack()

class ShowStudentsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(
            self,
            text="Show Students",
            font=controller.title_font
        )
        label.pack(side=tk.TOP, fill=tk.X, pady=10)
        btn1 = tk.Button(
            self,
            text="Return to Home Page",
            command=lambda:controller.show_frame("StartPage")
        )
        btn2 = tk.Button(
            self,
            text="return",
            command=lambda:controller.show_frame("StudentPage")
        )
        btn1.pack()
        btn2.pack()