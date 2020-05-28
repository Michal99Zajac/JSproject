import tkinter as tk

from Tables.DeansEmp import DeansEmp

from Frames.extendTk import MultiListBox


class DeansEmpPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.main_label()

        self.dean_emp_listbox()
        self.refresh_button()
        self.buttons()


    def main_label(self):
        label = tk.Label(
            self,
            text="Deans Employee Page",
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
        #Create Dean Emp Button
        btn_create = tk.Button(
            self,
            text="Create Dean Employee",
            command=lambda : self.controller.show_frame("CreateDeansEmpPage")
        )
        btn_create.pack()
        #Delete Dean Emp Button
        btn_delete = tk.Button(
            self,
            text="Delete Dean Employee",
            command=lambda : self.delete_emp()
        )
        btn_delete.pack()
        #Change Dean Emp Button
        btn_update = tk.Button(
            self,
            text="Change Dean Employee",
            command=lambda : self.update_emp()
        )
        btn_update.pack()


    def dean_emp_listbox(self):
        f_emp = tk.Frame(master=self)
        f_emp.pack()
        l_emp = tk.Label(master=f_emp, text="select dean employee")
        l_emp.pack()

        data = [
            ('id', 10),
            ('name', 20),
            ('second name', 20),
            ('lastname', 20),
            ('ssn',20),
            ('email',20),
            ('department', 20)
        ]

        self.list_emps = MultiListBox(master=f_emp, data=data)
        self.refresh()
        self.list_emps.pack()


    def refresh(self):
        self.list_emps.delete(0, tk.END)
        for i, emp in enumerate(self.controller.deans_emps):
            try:
                department = emp.get_department().get_name()
            except AttributeError:
                department = "-----------"

            output = (
                emp.get_id(),
                emp.get_name(),
                emp.get_sec_name(),
                emp.get_lastname(),
                emp.get_ssn(),
                emp.get_email(),
                department
            )
            self.list_emps.insert(i, output)


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
        self.controller.show_frame("DeansEmpPage")


    def delete_emp(self):
        idx = self.list_emps.index(tk.ACTIVE)
        del_emp = self.controller.deans_emps.pop(idx)

        del_emp.delete(self.controller.db)
        self.controller.db.commit_conn()

        del del_emp

        self.controller.frames["CreateFieldOfStudyPage"].refresh_leader_listbox()
        self.controller.frames["ChangeFieldOfStudyPage"].refresh_leader_listbox()
        self.controller.frames["FieldOfStudyPage"].refresh()
        self.restart()


    def update_emp(self):
        idx = self.list_emps.index(tk.ACTIVE)
        emp = self.controller.deans_emps[idx]

        self.controller.frames["ChangeDeansEmpPage"].set_emp(emp)
        self.controller.frames["ChangeDeansEmpPage"].fill_entry()
        self.controller.show_frame("ChangeDeansEmpPage")



class CreateDeansEmpPage(tk.Frame):
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
        self.dept_listbox()
        self.submit()


    def main_label(self):
        label = tk.Label(
            self,
            text="Create Dean Employee",
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
        self.controller.show_frame("DeansEmpPage")

    
    def refresh(self):
        self.e_name.delete(0, tk.END)
        self.e_sec_name.delete(0, tk.END)
        self.e_lastname.delete(0, tk.END)
        self.e_ssn.delete(0, tk.END)
        self.e_email.delete(0, tk.END)


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
            command=lambda : self.create_emp()
        )
        sub_btn.pack()

    
    def create_emp(self):
        temp_dept = None
        for dept in self.controller.fields:
            if self.dept_list.get(tk.ACTIVE) == dept.get_id():
                temp_dept = dept
                break

        self.controller.deans_emps.append(DeansEmp(
            name=self.e_name.get(),
            sec_name=self.e_sec_name.get(),
            lastname=self.e_lastname.get(),
            ssn=self.e_ssn.get(),
            email=self.e_email.get(),
            department=temp_dept
        ))

        self.controller.frames["CreateFieldOfStudyPage"].refresh_leader_listbox()
        self.controller.frames["ChangeFieldOfStudyPage"].refresh_leader_listbox()
        self.controller.frames["FieldOfStudyPage"].refresh()
        self.controller.deans_emps[-1].insert(self.controller.db)
        self.controller.db.commit_conn()
        self.controller.frames["DeansEmpPage"].restart()



class ChangeDeansEmpPage(CreateDeansEmpPage):
    def __init__(self, parent, controller):
        CreateDeansEmpPage.__init__(self,parent, controller)
        if controller.deans_emps:
            self.emp = controller.deans_emps[0]


    def main_label(self):
        label = tk.Label(
            self,
            text="Change Dean Employee",
            font=self.controller.title_font
        )
        label.pack(side=tk.TOP, fill=tk.X, pady=10)


    def submit(self):
        f_submit = tk.Frame(master=self)
        f_submit.pack()

        sub_btn = tk.Button(
            master=f_submit,
            text="submit",
            command=lambda : self.update_emp()
        )
        sub_btn.pack()


    def fill_entry(self):
        self.e_name.insert(tk.END, str(self.emp.get_name()))
        self.e_sec_name.insert(tk.END, str(self.emp.get_sec_name()))
        self.e_lastname.insert(tk.END, str(self.emp.get_lastname()))
        self.e_ssn.insert(tk.END, str(self.emp.get_ssn()))
        self.e_email.insert(tk.END, str(self.emp.get_email()))


    def set_emp(self, emp):
        self.emp = emp


    def update_emp(self):
        self.set_attr_emp()
        self.emp.update(self.controller.db)
        self.controller.commit_conn()

        #config after update
        self.controller.frames["CreateFieldOfStudyPage"].refresh_leader_listbox()
        self.controller.frames["ChangeFieldOfStudyPage"].refresh_leader_listbox()
        self.controller.frames["FieldOfStudyPage"].refresh()
        self.refresh()
        self.controller.frames["DeansEmpPage"].restart()


    def set_attr_emp(self):
        for dept in self.controller.departments:
            if self.dept_list.get(tk.ACTIVE) == dept.get_id():
                self.emp.set_department(dept)
                break


        self.emp.set_name(self.e_name.get())
        self.emp.set_sec_name(self.e_sec_name.get())
        self.emp.set_lastname(self.e_lastname.get())
        self.emp.set_ssn(self.e_ssn.get())
        self.emp.set_email(self.e_email.get())
