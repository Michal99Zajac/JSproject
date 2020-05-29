import tkinter as tk

from Tables.Teacher import Teacher

from Frames.extendTk import MultiListBox

class TeacherPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.main_label()

        self.teacher_listbox()
        self.refresh_button()
        self.buttons()

    def main_label(self):
        label = tk.Label(
            self,
            text="Teacher Page",
            font=self.controller.title_font
        )
        label.pack(side=tk.TOP, fill=tk.X, pady=10)


    def buttons(self):
        #Return Home Button
        btn_return = tk.Button(
            self,
            text="Return to Home Page",
            command=lambda:self.controller.show_frame("StartPage")
        )
        btn_return.pack()
        #Create Teacher Button
        btn_create = tk.Button(
            self,
            text="Create Teacher",
            command=lambda:self.controller.show_frame("CreateTeacherPage")
        )
        btn_create.pack()
        #Delete Teacher Button
        btn_delete = tk.Button(
            self,
            text="Delete Teacher",
            command=lambda:self.delete_teacher()
        )
        btn_delete.pack()
        #Change Teacher Button
        btn_update = tk.Button(
            self,
            text="Change Teacher",
            command=lambda: self.update_teacher()
        )
        btn_update.pack()


    def teacher_listbox(self):
        f_teacher = tk.Frame(master=self)
        f_teacher.pack()
        l_teacher = tk.Label(master=f_teacher, text="select teacher")
        l_teacher.pack()

        data = [
            ('id', 10),
            ('name', 20),
            ('second name', 20),
            ('lastname', 20),
            ('ssn', 20),
            ('email', 20),
            ('academic degree', 10),
            ('department name', 20),
            ('place of residence', 40)
        ]

        self.list_teachers = MultiListBox(master=f_teacher, data=data)
        self.refresh()
        self.list_teachers.pack()

    
    def refresh(self):
        self.list_teachers.delete(0, tk.END)
        for i, teacher in enumerate(self.controller.teachers):
            try:
                department = teacher.get_department().get_name()
            except AttributeError:
                department = "NULL"

            output = (
                teacher.get_id(),
                teacher.get_name(),
                teacher.get_sec_name(),
                teacher.get_lastname(),
                teacher.get_ssn(),
                teacher.get_email(),
                teacher.get_acd_degree(),
                department,
                teacher.get_place_of_residence()
            )
            self.list_teachers.insert(i, output)

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
        self.controller.show_frame("TeacherPage")


    def delete_teacher(self):
        idx = self.list_teachers.index(tk.ACTIVE)
        del_teacher = self.controller.teachers.pop(idx)

        del_teacher.delete(self.controller.db)
        self.delete_subject(del_teacher)
        self.controller.db.commit_conn()

        del del_teacher

        #update 'subject create room_listbox()'
        #update 'subject update room_listbox()'
        #subject.refresh()
        self.restart()


    def update_teacher(self):
        idx = self.list_teachers.index(tk.ACTIVE)
        teacher = self.controller.teachers[idx]

        self.controller.frames["ChangeTeacherPage"].set_teacher(teacher)
        self.controller.frames["ChangeTeacherPage"].fill_entry()
        self.controller.show_frame("ChangeTeacherPage")


    def delete_subject(self, teacher):
        idexes = []
        for i, subject in enumerate(self.controller.subjects):
            if subject.get_teacher() == teacher:
                subject.delete(self.controller.db)
                idexes.append(i)

        for i in idexes:
            self.controller.subjects.pop(i)
    


class CreateTeacherPage(tk.Frame):
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
        self.acd_listbox()
        self.dept_listbox()
        self.submit()

    def main_label(self):
        label = tk.Label(
            self,
            text="Create Teacher",
            font=self.controller.title_font
        )
        label.pack(side=tk.TOP, fill=tk.X, pady=10)

    
    def home_button(self):
        btn_home = tk.Button(
            self,
            text="Return to Home Page",
            command=lambda : self.home_refresh()
        )
        btn_home.pack()

    
    def home_refresh(self):
        self.refresh()
        self.controller.show_frame("StartPage")

    
    def return_button(self):
        btn_return = tk.Button(
            self,
            text="return",
            command=lambda : self.return_refresh()
        )
        btn_return.pack()


    def return_refresh(self):
        self.refresh()
        self.controller.show_frame("TeacherPage")


    def refresh(self):
        self.e_name.delete(0,tk.END)
        self.e_sec_name.delete(0, tk.END)
        self.e_lastname.delete(0, tk.END)
        self.e_ssn.delete(0, tk.END)
        self.e_email.delete(0, tk.END)
        self.e_place.delete(0, tk.END)


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


    def acd_listbox(self):
        f_acd = tk.Frame(master=self)
        f_acd.pack()

        l_acd = tk.Label(master=f_acd, text="academic degree")
        l_acd.pack()

        self.e_acd = tk.Listbox(master=f_acd)
        for i, degree in enumerate(Teacher.acd_degrees):
            self.e_acd.insert(i, degree)
        self.e_acd.pack()

    
    def place_entry(self):
        f_place = tk.Frame(master=self)
        f_place.pack()

        l_place = tk.Label(master=f_place, text="place of residence")
        l_place.pack()

        self.e_place = tk.Entry(master=self)
        self.e_place.pack()

    
    def dept_listbox(self):
        f_dept = tk.Frame(master=self)
        f_dept.pack()

        l_dept = tk.Label(master=f_dept, text="department")
        l_dept.pack()

        self.dept_list = tk.Listbox(master=f_dept)
        for i, dept in enumerate(self.controller.departments):
            self.dept_list.insert(i, dept.get_name())
        self.dept_list.pack()


    def refresh_dept_listbox(self):
        self.dept_list.delete(0, tk.END)
        for i, dept in enumerate(self.controller.departments):
            self.dept_list.insert(i, dept.get_name())

    
    def submit(self):
        sub_btn = tk.Button(
            master=self,
            text="submit",
            command=lambda : self.create_teacher()
        )
        sub_btn.pack()


    def create_teacher(self):
        temp_dept = None
        for dept in self.controller.departments:
            if self.dept_list.get(tk.ACTIVE) == dept.get_name():
                temp_dept = dept
                break

        self.controller.teachers.append(Teacher(
            name=self.e_name.get(),
            sec_name=self.e_sec_name.get(),
            lastname=self.e_lastname.get(),
            ssn=self.e_ssn.get(),
            email=self.e_email.get(),
            acd_degree=self.e_acd.get(tk.ACTIVE),
            department=temp_dept,
            place_of_residence=self.e_place.get()
        ))

        #update 'subject create room_listbox()'
        #update 'subject update room_listbox()'
        #subject.refresh()
        self.controller.teachers[-1].insert(self.controller.db)
        self.controller.db.commit_conn()
        self.controller.frames["TeacherPage"].restart()



class ChangeTeacherPage(CreateTeacherPage):
    def __init__(self, parent, controller):
        CreateTeacherPage.__init__(self, parent, controller)
        if controller.teachers:
            self.teacher = controller.teachers[0]


    def main_label(self):
        label = tk.Label(
            self,
            text="Change Teacher",
            font=self.controller.title_font
        )
        label.pack(side=tk.TOP, fill=tk.X, pady=10)


    def submit(self):
        f_submit = tk.Frame(master=self)
        f_submit.pack()

        sub_btn = tk.Button(
            master=f_submit,
            text="submit",
            command=lambda : self.update_teacher()
        )
        sub_btn.pack()


    def fill_entry(self):
        self.e_name.insert(tk.END, str(self.teacher.get_name()))
        self.e_lastname.insert(tk.END, str(self.teacher.get_lastname()))
        self.e_sec_name.insert(tk.END, str(self.teacher.get_sec_name()))
        self.e_email.insert(tk.END, str(self.teacher.get_email()))
        self.e_place.insert(tk.END, str(self.teacher.get_place_of_residence()))
        self.e_ssn.insert(tk.END, str(self.teacher.get_ssn()))


    def set_teacher(self, teacher):
        self.teacher = teacher


    def update_teacher(self):
        self.set_attr_teacher()
        self.teacher.update(self.controller.db)
        self.controller.db.commit_conn()

        #config after update
        #update 'subject create room_listbox()'
        #update 'subject update room_listbox()'
        #subject.refresh()
        self.refresh()
        self.controller.frames["TeacherPage"].restart()

    
    def set_attr_teacher(self):
        for dept in self.controller.departments:
            if self.dept_list.get(tk.ACTIVE) == dept.get_name():
                self.teacher.set_department(dept)
                break

        self.teacher.set_name(self.e_name.get())
        self.teacher.set_sec_name(self.e_sec_name.get())
        self.teacher.set_lastname(self.e_lastname.get())
        self.teacher.set_ssn(self.e_ssn.get())
        self.teacher.set_email(self.e_email.get())
        self.teacher.set_acd_degree(self.e_acd.get(tk.ACTIVE))
        self.teacher.set_place_od_residence(self.e_place.get())
