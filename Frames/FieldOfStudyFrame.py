import tkinter as tk

from Tables.FieldOfStudy import FieldOfStudy

from tk_extension.multilistBox import MultiListBox

class FieldOfStudyPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.columnconfigure([x for x in range(7)], minsize=248)
        self.rowconfigure([x for x in range(9)], minsize=100)
        self.controller = controller
        self.main_label()

        self.field_listbox()
        self.refresh_button()
        self.buttons()


    def main_label(self):
        label = tk.Label(
            self,
            text="Field of Study Page",
            font=self.controller.title_font
        )
        label.grid(row = 0, column = 6, sticky="nsew", padx=5, pady=5)


    def buttons(self):
        #Return Home Button
        btn_return = tk.Button(
            self,
            text="Home",
            font=self.controller.normal_font,
            command=lambda : self.controller.show_frame("StartPage")
        )
        btn_return.grid(row=4, column=6, sticky="nsew", padx=5, pady=5)
        #Create Field of Study Button
        btn_create = tk.Button(
            self,
            text="Create",
            command=lambda : self.controller.show_frame("CreateFieldOfStudyPage"),
            font=self.controller.normal_font,
        )
        btn_create.grid(row=1, column=6, sticky="nsew", padx=5, pady=5)
        #Delete Field of Study Button
        btn_delete = tk.Button(
            self,
            text="Delete",
            command=lambda : self.delete_field(),
            font=self.controller.normal_font,
        )
        btn_delete.grid(row=2, column=6, sticky="nsew", padx=5, pady=5)
        #Update Field of Study
        btn_update = tk.Button(
            self,
            text="Update",
            command=lambda : self.update_field(),
            font=self.controller.normal_font,
        )
        btn_update.grid(row=3, column=6, sticky="nsew", padx=5, pady=5)


    def field_listbox(self):
        data = [
            ('id', 10),
            ('name', 20),
            ('department', 20),
            ('leader of field', 20)
        ]

        self.list_fields = MultiListBox(master=self, data=data)
        self.refresh()
        self.list_fields.grid(row=0, column=0, columnspan=6, rowspan=9, sticky="nswe", padx=5, pady=5)


    def refresh(self):
        self.list_fields.delete(0, tk.END)
        for i, field in enumerate(self.controller.fields):
            try:
                department = field.get_department().get_name()
            except AttributeError:
                department = "NULL"

            try:
                leader = field.get_leader().get_name() + " " + field.get_leader().get_lastname()
            except AttributeError:
                leader = "NULL"

            output = (
                field.get_id(),
                field.get_name(),
                department,
                leader
            )

            self.list_fields.insert(i, output)


    def restart(self):
        self.refresh()
        self.controller.show_frame("FieldOfStudyPage")


    def refresh_button(self):
        btn_refresh = tk.Button(
            master=self,
            text="refresh",
            command=lambda : self.restart(),
            font=self.controller.normal_font,
        )
        btn_refresh.grid(row=8, column=6, sticky="nsew", padx=5, pady=5)


    def delete_field(self):
        idx = self.list_fields.index(tk.ACTIVE)
        del_field = self.controller.fields.pop(idx)

        del_field.delete(self.controller.db)
        self.update_student(del_field)
        self.controller.db.commit_conn()

        del del_field
        #students restart
        self.controller.frames["CreateStudentPage"].refresh_field_listbox()
        self.controller.frames["ChangeStudentPage"].refresh_field_listbox()
        self.controller.frames["StudentPage"].refresh()
        #lab group restart
        self.controller.frames["CreateLabGroupPage"].refresh_field_listbox()
        self.controller.frames["LabGroupPage"].refresh()
        #exe group restart
        self.controller.frames["CreateExeGroupPage"].refresh_field_listbox()
        self.controller.frames["ExeGroupPage"].refresh()
        #year group restart
        self.controller.frames["CreateYearGroupPage"].refresh_field_listbox()
        self.controller.frames["YearGroupPage"].refresh()
        #subject restarts
        self.controller.frames["YearSubjectPage"].refresh()
        self.controller.frames["CreateYearSubjectPage"].refresh_field_listbox()
        self.controller.frames["ExeSubjectPage"].refresh()
        self.controller.frames["CreateExeSubjectPage"].refresh_field_listbox()
        self.controller.frames["LabSubjectPage"].refresh()
        self.controller.frames["CreateLabSubjectPage"].refresh_field_listbox()
        
        self.restart()


    def update_student(self, field):
        for student in self.controller.students:
            try:
                if student.get_field() == field:
                    student.set_field(None)
                    student.update(self.controller.db)
                    self.controller.db.commit_conn()
            except AttributeError:
                pass


    def update_field(self):
        idx = self.list_fields.index(tk.ACTIVE)
        field = self.controller.fields[idx]

        self.controller.frames["ChangeFieldOfStudyPage"].set_field(field)
        self.controller.frames["ChangeFieldOfStudyPage"].fill_entry()
        self.controller.show_frame("ChangeFieldOfStudyPage")
        

class CreateFieldOfStudyPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.columnconfigure([x for x in range(9)], minsize=250)
        self.rowconfigure([x for x in range(18)], minsize=50)
        self.controller = controller
        
        self.main_label()
        self.return_button()
        self.home_button()
        self.name_entry()
        self.dept_listbox()
        self.leader_listbox()
        self.submit()


    def main_label(self):
        label = tk.Label(
            self,
            text="Create Field of Study",
            font=self.controller.title_font
        )
        label.grid(row=0, column=0, rowspan=1, columnspan=4, sticky="news", padx=5, pady=5)


    def return_button(self):
        btn_return = tk.Button(
            self,
            text="Return",
            command=lambda : self.return_refresh(),
            font=self.controller.normal_font,
        )
        btn_return.grid(row=16, column=0, rowspan=2, columnspan=2, sticky="news", padx=5, pady=5)

    
    def return_refresh(self):
        self.refresh()
        self.controller.show_frame("FieldOfStudyPage")


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


    def refresh(self):
        self.e_name.delete(0, tk.END)


    def name_entry(self):
        l_name = tk.Label(master=self, text="name", font=self.controller.normal_font, anchor=tk.W, relief=tk.RAISED)
        l_name.grid(row=1, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)

        self.e_name = tk.Entry(master=self, font=self.controller.entry_font)
        self.e_name.grid(row=2, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)


    def dept_listbox(self):
        l_dept = tk.Label(master=self, text="department", font=self.controller.normal_font, relief=tk.RAISED)
        l_dept.grid(row=0, column=4, rowspan=1, columnspan=3, sticky="nswe", pady=5, padx=5)

        data = [
            ('name', 10),
            ('dean', 10)
        ]

        self.list_dept = MultiListBox(master=self, data=data)
        self.list_dept.grid(row=1, column=4, rowspan=8, columnspan=3, sticky="nswe", pady=5, padx=5)
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


    def leader_listbox(self):
        l_leader = tk.Label(master=self, text="deans office employees", font=self.controller.normal_font, relief=tk.RAISED)
        l_leader.grid(row=9, column=4, rowspan=1, columnspan=3, sticky="nswe", pady=5, padx=5)

        data = [
            ('name', 20),
            ('lastname', 20)
        ]

        self.list_leader = MultiListBox(master=self, data=data)
        self.list_leader.grid(row=10, column=4, rowspan=8, columnspan=3, sticky="nswe", pady=5, padx=5)
        self.refresh_leader_listbox()


    def refresh_leader_listbox(self):
        self.list_leader.delete(0, tk.END)
        for i, emp in enumerate(self.controller.deans_emps):
            output = (
                emp.get_name(),
                emp.get_lastname()
            )

            self.list_leader.insert(i, output)


    def submit(self):
        sub_btn = tk.Button(
            master=self,
            text="submit",
            command=lambda : self.create_field(),
            font=self.controller.normal_font,
        )
        sub_btn.grid(row=14, column=0, rowspan=2, columnspan=4, sticky="nswe", pady=5, padx=5)


    def create_field(self):
        idx = self.list_dept.index(tk.ACTIVE)
        temp_dept = self.controller.departments[idx]

        idx = self.list_leader.index(tk.ACTIVE)
        temp_leader = self.controller.deans_emps[idx]

        self.controller.fields.append(FieldOfStudy(
            name=self.e_name.get(),
            department=temp_dept,
            do_emp=temp_leader
        ))

        #lab group restart
        self.controller.frames["CreateLabGroupPage"].refresh_field_listbox()
        self.controller.frames["LabGroupPage"].refresh()
        #exe group restart
        self.controller.frames["CreateExeGroupPage"].refresh_field_listbox()
        self.controller.frames["ExeGroupPage"].refresh()
        #year group restart
        self.controller.frames["CreateYearGroupPage"].refresh_field_listbox()
        self.controller.frames["YearGroupPage"].refresh()
        #student page restart
        self.controller.frames["StudentPage"].refresh()

        self.controller.frames["YearSubjectPage"].refresh()
        self.controller.frames["CreateYearSubjectPage"].refresh_field_listbox()
        self.controller.frames["ExeSubjectPage"].refresh()
        self.controller.frames["CreateExeSubjectPage"].refresh_field_listbox()
        self.controller.frames["LabSubjectPage"].refresh()
        self.controller.frames["CreateLabSubjectPage"].refresh_field_listbox()

        self.refresh()
        self.controller.fields[-1].insert(self.controller.db)
        self.controller.db.commit_conn()
        self.controller.frames["FieldOfStudyPage"].restart()



class ChangeFieldOfStudyPage(CreateFieldOfStudyPage):
    def __init__(self, parent, controller):
        CreateFieldOfStudyPage.__init__(self, parent, controller)
        if controller.fields:
            self.field = controller.fields[0]


    def main_label(self):
        label = tk.Label(
            self,
            text="Change Field of Study",
            font=self.controller.title_font
        )
        label.grid(row=0, column=0, rowspan=1, columnspan=4, sticky="news", padx=5, pady=5)


    def submit(self):
        sub_btn = tk.Button(
            master=self,
            text="submit",
            command=lambda : self.update_field(),
            font=self.controller.normal_font,
        )
        sub_btn.grid(row=14, column=0, rowspan=2, columnspan=4, sticky="news", padx=5, pady=5)


    def fill_entry(self):
        self.e_name.insert(tk.END, str(self.field.get_name()))

    
    def set_field(self, field):
        self.field = field


    def set_attr_field(self):
        idx = self.list_dept.index(tk.ACTIVE)
        temp_dept = self.controller.departments[idx]
        self.field.set_department(temp_dept)

        idx = self.list_leader.index(tk.ACTIVE)
        temp_emp = self.controller.deans_emps[idx]
        self.field.set_leader(temp_emp)

        self.field.set_name(self.e_name.get())


    def update_field(self):
        self.set_attr_field()
        self.field.update(self.controller.db)
        self.controller.db.commit_conn()

        #config after update
        #student page refresh
        self.controller.frames["CreateStudentPage"].refresh_field_listbox()
        self.controller.frames["ChangeStudentPage"].refresh_field_listbox()
        self.controller.frames["StudentPage"].refresh()
        #lab group restart
        self.controller.frames["CreateLabGroupPage"].refresh_field_listbox()
        self.controller.frames["LabGroupPage"].refresh()
        #exe group restart
        self.controller.frames["CreateExeGroupPage"].refresh_field_listbox()
        self.controller.frames["ExeGroupPage"].refresh()
        #year group restart
        self.controller.frames["CreateYearGroupPage"].refresh_field_listbox()
        self.controller.frames["YearGroupPage"].refresh()
        #subjects restarts
        self.controller.frames["YearSubjectPage"].refresh()
        self.controller.frames["CreateYearSubjectPage"].refresh_field_listbox()
        self.controller.frames["ExeSubjectPage"].refresh()
        self.controller.frames["CreateExeSubjectPage"].refresh_field_listbox()
        self.controller.frames["LabSubjectPage"].refresh()
        self.controller.frames["CreateLabSubjectPage"].refresh_field_listbox()

        self.refresh()
        self.controller.frames["FieldOfStudyPage"].restart()
