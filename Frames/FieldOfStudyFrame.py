import tkinter as tk

from Tables.FieldOfStudy import FieldOfStudy

from tk_extension.multilistBox import MultiListBox

class FieldOfStudyPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
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
        label.pack(side=tk.TOP, fill=tk.X, pady=10)


    def buttons(self):
        #Return Home Button
        btn_return = tk.Button(
            self,
            text="Return to Home Page",
            command=lambda : self.controller.show_frame("StartPage")
        )
        btn_return.pack()
        #Create Field of Study Button
        btn_create = tk.Button(
            self,
            text="Create Field of Study",
            command=lambda : self.controller.show_frame("CreateFieldOfStudyPage")
        )
        btn_create.pack()
        #Delete Field of Study Button
        btn_delete = tk.Button(
            self,
            text="Delete Field of Study",
            command=lambda : self.delete_field()
        )
        btn_delete.pack()
        #Update Field of Study
        btn_update = tk.Button(
            self,
            text="Update Field of Study",
            command=lambda : self.update_field()
        )
        btn_update.pack()


    def field_listbox(self):
        f_field = tk.Frame(master=self)
        f_field.pack()
        l_field = tk.Label(master=f_field, text="select field of study")
        l_field.pack()

        data = [
            ('id', 10),
            ('name', 20),
            ('department', 20),
            ('leader of field', 20)
        ]

        self.list_fields = MultiListBox(master=f_field, data=data)
        self.refresh()
        self.list_fields.pack()


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
        f_refresh = tk.Frame(master=self)
        f_refresh.pack()
        btn_refresh = tk.Button(
            master=f_refresh,
            text="refresh",
            command=lambda : self.restart()
        )
        btn_refresh.pack()


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
        label.pack(side=tk.TOP, fill=tk.X, pady=10)


    def return_button(self):
        btn_return = tk.Button(
            self,
            text="Return",
            command=lambda : self.return_refresh()
        )
        btn_return.pack()

    
    def return_refresh(self):
        self.refresh()
        self.controller.show_frame("FieldOfStudyPage")


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


    def refresh(self):
        self.e_name.delete(0, tk.END)


    def name_entry(self):
        f_name = tk.Frame(master=self)
        f_name.pack()

        l_name = tk.Label(master=f_name, text="name")
        l_name.pack()

        self.e_name = tk.Entry(master=f_name)
        self.e_name.pack()


    def dept_listbox(self):
        f_dept = tk.Frame(master=self)
        f_dept.pack()

        l_dept = tk.Label(master=f_dept, text="department")
        l_dept.pack()

        self.list_dept = tk.Listbox(master=f_dept)
        for i, dept in enumerate(self.controller.departments):
            self.list_dept.insert(i, dept.get_name())
        self.list_dept.pack()


    def refresh_dept_listbox(self):
        self.list_dept.delete(0, tk.END)
        for i, dept in enumerate(self.controller.departments):
            self.list_dept.insert(i, dept.get_name())


    def leader_listbox(self):
        f_leader = tk.Frame(master=self)
        f_leader.pack()

        l_leader = tk.Label(master=f_leader, text="deans office employees")
        l_leader.pack()

        self.list_leader = tk.Listbox(master=f_leader)
        for i, emp in enumerate(self.controller.deans_emps):
            leader = emp.get_name() + " " + emp.get_lastname()
            self.list_leader.insert(i, leader)
        self.list_leader.pack()


    def refresh_leader_listbox(self):
        self.list_leader.delete(0, tk.END)
        for i, emp in enumerate(self.controller.deans_emps):
            leader = emp.get_name() + " " + emp.get_lastname()
            self.list_leader.insert(i, leader)


    def submit(self):
        f_submit = tk.Frame(master=self)
        f_submit.pack()

        sub_btn = tk.Button(
            master=f_submit,
            text="submit",
            command=lambda : self.create_field()
        )
        sub_btn.pack()


    def create_field(self):
        temp_dept = None
        for dept in self.controller.departments:
            if self.list_dept.get(tk.ACTIVE) == dept.get_name():
                temp_dept = dept
                break

        temp_leader = None
        for leader in self.controller.deans_emps:
            full_leader = leader.get_name() + " " + leader.get_lastname()
            if self.list_leader.get(tk.ACTIVE) == full_leader:
                temp_leader = leader
                break

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
        label.pack(side=tk.TOP, fill=tk.X, pady=10)


    def submit(self):
        f_submit = tk.Frame(master=self)
        f_submit.pack()

        sub_btn = tk.Button(
            master=f_submit,
            text="submit",
            command=lambda : self.update_field()
        )
        sub_btn.pack()


    def fill_entry(self):
        self.e_name.insert(tk.END, str(self.field.get_name()))

    
    def set_field(self, field):
        self.field = field


    def set_attr_field(self):
        for dept in self.controller.departments:
            if self.list_dept.get(tk.ACTIVE) == dept.get_name():
                self.field.set_department(dept)
                break

        for emp in self.controller.deans_emps:
            full_emp = emp.get_name() + " " + emp.get_lastname()
            if self.list_leader.get(tk.ACTIVE) == full_emp:
                self.field.set_leader(emp)
                break

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
