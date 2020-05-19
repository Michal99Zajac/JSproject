import tkinter as tk
from tkinter import font as tkfont
import tkinter.ttk as ttk

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

        self.student_listbox()
        self.refresh_button()
        self.buttons()

    def buttons(self):
        #Return Home Button
        btn_return = tk.Button(
            self,
            text="Return to Home Page",
            command=lambda: self.controller.show_frame("StartPage")
        )
        #Create Student Button
        btn_create = tk.Button(
            self,
            text="Create Student",
            command=lambda: self.controller.show_frame("CreateStudentPage")
        )
        #Delete Student Button
        btn_delete = tk.Button(
            self,
            text="Delete Student",
            command=lambda: self.delete_student()
        )
        #Change Student Button
        btn_change = tk.Button(
            self,
            text="Change Student",
            command=lambda: self.update_student()
        )
        btn_return.pack()
        btn_create.pack()
        btn_delete.pack()
        btn_change.pack()

    def student_listbox(self):
        self.f_student = tk.Frame(master=self)
        self.l_student = tk.Label(master=self.f_student, text="select student")
        self.l_student.pack()
        self.list_students = MultiListBox(master=self.f_student)

        self.refresh()

        self.list_students.pack()
        self.f_student.pack()

    def delete_student(self):
        idx = self.list_students.index(tk.ACTIVE)
        del_student = self.controller.students.pop(idx)

        del_student.delete(self.controller.db)
        self.controller.db.commit_conn()

        del del_student
        self.restart()

    def update_student(self):
        idx = self.list_students.index(tk.ACTIVE)
        student = self.controller.students[idx]
        
        self.controller.frames["ChangeStudentPage"].set_student(student)
        self.controller.show_frame("ChangeStudentPage")

    def restart(self):
        self.refresh()
        self.controller.show_frame("StudentPage")

    def refresh_button(self):
        self.f_refresh = tk.Frame(master=self)
        self.b_refresh = tk.Button(master=self.f_refresh, text="refresh", command=lambda : self.restart())
        self.b_refresh.pack()
        self.f_refresh.pack()

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

        label = tk.Label(
            self,
            text="Create Student",
            font=self.controller.title_font
        )
        label.pack(side=tk.TOP, fill=tk.X, pady=10)

        self.return_buttons()
        self.name_entry()
        self.sec_name_entry()
        self.lastname_entry()
        self.ssn_entry()
        self.email_entry()
        self.place_entry()
        self.field_listbox()
        self.submit()

    def return_buttons(self):
        btn_home = tk.Button(
            self,
            text="Return to Home Page",
            command=lambda:self.controller.show_frame("StartPage")
        )
        btn_return = tk.Button(
            self,
            text="return",
            command=lambda:self.controller.show_frame("StudentPage")
        )
        btn_home.pack()
        btn_return.pack()

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
        self.controller.show_frame("StudentPage")
        self.controller.frames["StudentPage"].restart()

class ChangeStudentPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.student = controller.students[0]

        label = tk.Label(
            self,
            text="Change Student",
            font=self.controller.title_font
        )
        label.pack(side=tk.TOP, fill=tk.X, pady=10)

        self.return_buttons()
        self.name_entry()
        self.sec_name_entry()
        self.lastname_entry()
        self.ssn_entry()
        self.email_entry()
        self.place_entry()
        self.field_listbox()
        self.submit()

    def return_buttons(self):
        btn_home = tk.Button(
            self,
            text="Return to Home Page",
            command=lambda: self.controller.show_frame("StartPage")
        )
        btn_return = tk.Button(
            self,
            text="return",
            command=lambda: self.controller.show_frame("StudentPage")
        )
        btn_home.pack()
        btn_return.pack()

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
            command=lambda:self.update_student()
            )
        self.sub_btn.pack()
        self.f_submit.pack()

    def set_student(self, student):
        self.student = student

    def update_student(self):
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

        self.student.update(self.controller.db)
        self.controller.db.commit_conn()
        self.controller.show_frame("StudentPage")
        self.controller.frames["StudentPage"].restart()

class MultiListBox(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.data = (
            ('id', 10),
            ('name', 20),
            ('second name', 20),
            ('lastname', 20),
            ('ssn', 20),
            ('email', 20),
            ('field of study', 30),
            ('place of residence', 40)
        )
        self.lists = []
        self.l = {}

        for name, width in self.data:
            temp_frame = tk.Frame(self)
            temp_frame.pack(
                side=tk.LEFT,
                expand=tk.YES,
                fill=tk.BOTH
                )

            tk.Label(
                master=temp_frame,
                text=name,
                borderwidth=1,
                relief=tk.RAISED
            ).pack(fill=tk.X)

            lb = tk.Listbox(
                master=temp_frame,
                width=width,
                borderwidth=0,
                selectborderwidth=0,
                relief=tk.FLAT,
                exportselection=tk.FALSE
            )
            lb.pack(expand=tk.YES, fill=tk.BOTH)

            self.lists.append(lb)
            self.l[name] = lb

            lb.bind('<B1-Motion>',lambda e, s=self: s._select(e.y))
            lb.bind('<Button-1>',lambda e, s=self: s._select(e.y))

        frame = tk.Frame(self)
        frame.pack(side=tk.LEFT, fill=tk.Y)
        tk.Label(
            master=frame,
            borderwidth=1,
            relief=tk.RAISED
        ).pack(fill=tk.X)

    def _select(self, y):
        row = self.lists[0].nearest(y)
        self.selection_clear(0, tk.END)
        self.selection_set(row)
        return 'break'

    def selection_set(self, first, last=None):
        for l in self.lists:
            l.selection_set(first, last)

    def selection_clear(self, first, last=None):
        for l in self.lists:
            l.selection_clear(first, last)

    def insert(self, index, *elements):
        for e in elements:
            i = 0
            for name in self.lists:
                name.insert(index, e[i])
                i += 1

    def delete(self, first, last=None):
        for name in self.lists:
            name.delete(first, last)

    def index(self, index):
        return self.lists[0].index(index)