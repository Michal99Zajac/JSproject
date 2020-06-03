import tkinter as tk

from Tables.Teacher import Teacher

from tk_extension.multilistBox import MultiListBox

class TeacherPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.columnconfigure([x for x in range(7)], minsize=250)
        self.rowconfigure([x for x in range(9)], minsize=100)
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
        label.grid(row=0, column = 6, sticky="news", padx=5, pady=5)


    def buttons(self):
        #Return Home Button
        btn_return = tk.Button(
            self,
            text="Home",
            command=lambda:self.controller.show_frame("StartPage"),
            font=self.controller.normal_font,
        )
        btn_return.grid(row=4, column=6, sticky="news", padx=5, pady=5)
        #Create Teacher Button
        btn_create = tk.Button(
            self,
            text="Create Teacher",
            command=lambda:self.controller.show_frame("CreateTeacherPage"),
            font=self.controller.normal_font,
        )
        btn_create.grid(row=1, column=6, sticky="news", padx=5, pady=5)
        #Delete Teacher Button
        btn_delete = tk.Button(
            self,
            text="Delete Teacher",
            command=lambda:self.delete_teacher(),
            font=self.controller.normal_font,
        )
        btn_delete.grid(row=2, column=6, sticky="news", padx=5, pady=5)
        #Change Teacher Button
        btn_update = tk.Button(
            self,
            text="Change Teacher",
            command=lambda: self.update_teacher(),
            font=self.controller.normal_font,
        )
        btn_update.grid(row=3, column=6, sticky="news", padx=5, pady=5)


    def teacher_listbox(self):
        data = [
            ('id', 10),
            ('name', 20),
            ('second name', 20),
            ('lastname', 20),
            ('ssn', 20),
            ('email', 20),
            ('academic degree', 10),
            ('department name', 20),
            ('place of residence', 30)
        ]

        self.list_teachers = MultiListBox(master=self, data=data)
        self.refresh()
        self.list_teachers.grid(row=0, column=0, columnspan=6, rowspan=9, sticky="news", padx=5, pady=5)

    
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
        btn_refresh = tk.Button(
            master=self,
            text="refresh",
            command=lambda : self.restart(),
            font=self.controller.normal_font,
        )
        btn_refresh.grid(row=8, column=6, sticky="news", padx=5, pady=5)


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

        #config after delete
        self.controller.frames["YearSubjectPage"].refresh()
        self.controller.frames["CreateYearSubjectPage"].refresh_teacher_listbox()
        self.controller.frames["ExeSubjectPage"].refresh()
        self.controller.frames["CreateExeSubjectPage"].refresh_teacher_listbox()
        self.controller.frames["LabSubjectPage"].refresh()
        self.controller.frames["CreateLabSubjectPage"].refresh_teacher_listbox()

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
        self.columnconfigure([x for x in range(9)], minsize=250)
        self.rowconfigure([x for x in range(18)], minsize=49)
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
        label.grid(row=0, column=0, rowspan=1, columnspan=4, sticky="news", padx=5, pady=5)

    
    def home_button(self):
        btn_home = tk.Button(
            self,
            text="Home",
            command=lambda : self.home_refresh(),
            font=self.controller.normal_font,
        )
        btn_home.grid(row=16, column=2,rowspan=2, columnspan=2, sticky="news", padx=5, pady=5)

    
    def home_refresh(self):
        self.refresh()
        self.controller.show_frame("StartPage")

    
    def return_button(self):
        btn_return = tk.Button(
            self,
            text="return",
            command=lambda : self.return_refresh(),
            font=self.controller.normal_font,
        )
        btn_return.grid(row=16, column=0, rowspan=2, columnspan=2, sticky="news", padx=5, pady=5)


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
        l_name = tk.Label(master=self, text="name", font=self.controller.normal_font, anchor=tk.W, relief=tk.RAISED)
        l_name.grid(row=1, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)

        self.e_name = tk.Entry(master=self, font=self.controller.entry_font)
        self.e_name.grid(row=2, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)

    
    def sec_name_entry(self):
        l_sec_name = tk.Label(master=self, text="second name", font=self.controller.normal_font, anchor=tk.W, relief=tk.RAISED)
        l_sec_name.grid(row=3, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)

        self.e_sec_name = tk.Entry(master=self, font=self.controller.entry_font)
        self.e_sec_name.grid(row=4, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)


    def lastname_entry(self):
        l_lastname = tk.Label(master=self, text="lastname", font=self.controller.normal_font, anchor=tk.W, relief=tk.RAISED)
        l_lastname.grid(row=5, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)

        self.e_lastname = tk.Entry(master=self, font=self.controller.entry_font)
        self.e_lastname.grid(row=6, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)

    
    def ssn_entry(self):
        l_ssn = tk.Label(master=self, text="ssn", font=self.controller.normal_font, anchor=tk.W, relief=tk.RAISED)
        l_ssn.grid(row=7, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)

        self.e_ssn = tk.Entry(master=self, font=self.controller.entry_font)
        self.e_ssn.grid(row=8, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)


    def email_entry(self):
        l_email = tk.Label(master=self, text="email", font=self.controller.normal_font, anchor=tk.W, relief=tk.RAISED)
        l_email.grid(row=9, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)

        self.e_email = tk.Entry(master=self, font=self.controller.entry_font)
        self.e_email.grid(row=10, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)


    def acd_listbox(self):
        data = [
            ('academic degree', 10),
        ]

        self.e_acd = MultiListBox(master=self, data=data)
        for i, degree in enumerate(Teacher.acd_degrees):
            self.e_acd.insert(i, (degree,))
        self.e_acd.grid(row=0, column=4, rowspan=4, columnspan=3, sticky="nswe", pady=5, padx=5)

    
    def place_entry(self):
        l_place = tk.Label(master=self, text="place of residence", font=self.controller.normal_font, anchor=tk.W, relief=tk.RAISED)
        l_place.grid(row=11, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)

        self.e_place = tk.Entry(master=self, font=self.controller.entry_font)
        self.e_place.grid(row=12, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)

    
    def dept_listbox(self):
        l_dept = tk.Label(master=self, text="department", font=self.controller.normal_font, relief=tk.RAISED)
        l_dept.grid(row=4, column=4, rowspan=1, columnspan=3, sticky="nswe", pady=5, padx=5)

        data = [
            ('name', 10),
            ('dean', 10)
        ]

        self.list_dept = MultiListBox(master=self, data=data)
        self.list_dept.grid(row=5, column=4, rowspan=14, columnspan=3, sticky="nswe", pady=5, padx=5)
        self.refresh_dept_listbox()


    def refresh_dept_listbox(self):
        self.list_dept.delete(0, tk.END)
        for i, dept in enumerate(self.controller.departments):
            try:
                dean = dept.get_dean().get_name()
            except AttributeError:
                dean = "NULL"

            output = (
                dept.get_name(),
                dean
            )

            self.list_dept.insert(i, output)

    
    def submit(self):
        sub_btn = tk.Button(
            master=self,
            text="submit",
            command=lambda : self.create_teacher(),
            font=self.controller.normal_font,
        )
        sub_btn.grid(row=14, column=0, rowspan=2, columnspan=4, sticky="news", padx=5, pady=5)


    def create_teacher(self):
        try:
            idx = self.list_dept.index(tk.ACTIVE)
            temp_dept = self.controller.departments[idx]
        except IndexError:
            temp_dept = None

        idx = self.e_acd.index(tk.ACTIVE)
        temp_acd = list(Teacher.acd_degrees)[idx]

        self.controller.teachers.append(Teacher(
            name=self.e_name.get(),
            sec_name=self.e_sec_name.get(),
            lastname=self.e_lastname.get(),
            ssn=self.e_ssn.get(),
            email=self.e_email.get(),
            acd_degree=temp_acd,
            department=temp_dept,
            place_of_residence=self.e_place.get()
        ))

        #config after create
        self.controller.frames["YearSubjectPage"].refresh()
        self.controller.frames["CreateYearSubjectPage"].refresh_teacher_listbox()
        self.controller.frames["ExeSubjectPage"].refresh()
        self.controller.frames["CreateExeSubjectPage"].refresh_teacher_listbox()
        self.controller.frames["LabSubjectPage"].refresh()
        self.controller.frames["CreateLabSubjectPage"].refresh_teacher_listbox()

        self.controller.teachers[-1].insert(self.controller.db)
        self.controller.db.commit_conn()
        self.refresh()
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
        label.grid(row=0, column=0, rowspan=1, columnspan=4, sticky="news", padx=5, pady=5)


    def submit(self):
        sub_btn = tk.Button(
            master=self,
            text="submit",
            command=lambda : self.update_teacher(),
            font=self.controller.normal_font,
        )
        sub_btn.grid(row=14, column=0, rowspan=2, columnspan=4, sticky="nswe", pady=5, padx=5)


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
        self.controller.frames["YearSubjectPage"].refresh()
        self.controller.frames["CreateYearSubjectPage"].refresh_teacher_listbox()
        self.controller.frames["ExeSubjectPage"].refresh()
        self.controller.frames["CreateExeSubjectPage"].refresh_teacher_listbox()
        self.controller.frames["LabSubjectPage"].refresh()
        self.controller.frames["CreateLabSubjectPage"].refresh_teacher_listbox()
        
        self.refresh()
        self.controller.frames["TeacherPage"].restart()

    
    def set_attr_teacher(self):
        try:
            idx = self.list_dept.index(tk.ACTIVE)
            temp_dept = self.controller.departments[idx]
            self.teacher.set_department(temp_dept)
        except IndexError:
            pass

        try:
            idx = self.e_acd.index(tk.ACTIVE)
            temp_acd = list(Teacher.acd_degrees)[idx]
            self.teacher.set_acd_degree(temp_acd)
        except IndexError:
            pass

        self.teacher.set_name(self.e_name.get())
        self.teacher.set_sec_name(self.e_sec_name.get())
        self.teacher.set_lastname(self.e_lastname.get())
        self.teacher.set_ssn(self.e_ssn.get())
        self.teacher.set_email(self.e_email.get())
        self.teacher.set_place_od_residence(self.e_place.get())
