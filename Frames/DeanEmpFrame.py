import tkinter as tk

from Tables.DeansEmp import DeansEmp

from tk_extension.multilistBox import MultiListBox


class DeansEmpPage(tk.Frame):
    """
    Main Deans Office Employee Page
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.columnconfigure([x for x in range(7)], minsize=241)
        self.rowconfigure([x for x in range(9)], minsize=100)
        self.controller = controller
        self.main_label()

        self.dean_emp_listbox()
        self.refresh_button()
        self.buttons()

    def main_label(self):
        """create deans office employee main label
        """
        label = tk.Label(
            self,
            text="Deans Employee Page",
            font=self.controller.title_font
        )
        label.grid(
            row=0,
            column=6,
            sticky="nsew",
            padx=5,
            pady=5
        )

    def buttons(self):
        """create deans office page buttons
        """
        # Return Home Button
        btn_return = tk.Button(
            self,
            text="Home",
            command=lambda: self.controller.show_frame("StartPage"),
            font=self.controller.normal_font
        )
        btn_return.grid(row=4, column=6, sticky="nsew", padx=5, pady=5)
        # Create Dean Emp Button
        btn_create = tk.Button(
            self,
            text="Create Dean Employee",
            command=lambda: self.controller.show_frame("CreateDeansEmpPage"),
            font=self.controller.normal_font
        )
        btn_create.grid(row=1, column=6, sticky="nsew", padx=5, pady=5)
        # Delete Dean Emp Button
        btn_delete = tk.Button(
            self,
            text="Delete Dean Employee",
            command=lambda: self.delete_emp(),
            font=self.controller.normal_font
        )
        btn_delete.grid(row=2, column=6, sticky="nsew", padx=5, pady=5)
        # Change Dean Emp Button
        btn_update = tk.Button(
            self,
            text="Change Dean Employee",
            command=lambda: self.update_emp(),
            font=self.controller.normal_font
        )
        btn_update.grid(row=3, column=6, sticky="nsew", padx=5, pady=5)

    def dean_emp_listbox(self):
        """create deans office employee listbox
        """
        data = [
            ('id', 10),
            ('name', 20),
            ('second name', 20),
            ('lastname', 20),
            ('ssn', 20),
            ('email', 20),
            ('department', 20)
        ]

        self.list_emps = MultiListBox(master=self, data=data)
        self.refresh()
        self.list_emps.grid(
            row=0,
            column=0,
            columnspan=6,
            rowspan=9,
            sticky="nswe",
            padx=5,
            pady=5
        )

    def refresh(self):
        """func refresh deans office listbox
        """
        self.list_emps.delete(0, tk.END)
        for i, emp in enumerate(self.controller.deans_emps):
            try:
                department = emp.get_department().get_name()
            except AttributeError:
                department = "NULL"

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
        """create refresh button
        """
        btn_refresh = tk.Button(
            master=self,
            text="refresh",
            command=lambda: self.restart(),
            font=self.controller.normal_font
        )
        btn_refresh.grid(row=8, column=6, sticky="nsew", padx=5, pady=5)

    def restart(self):
        """func restart frame
        """
        self.refresh()
        self.controller.show_frame("DeansEmpPage")

    def delete_emp(self):
        """func delete deans office employee from listbox and
        config other frames
        """
        idx = self.list_emps.index(tk.ACTIVE)
        del_emp = self.controller.deans_emps.pop(idx)

        del_emp.delete(self.controller.db)
        self.controller.db.commit_conn()

        del del_emp
        # config
        self.controller.frames["CreateFieldOfStudyPage"].refresh_leader_listbox()
        self.controller.frames["ChangeFieldOfStudyPage"].refresh_leader_listbox()
        self.controller.frames["FieldOfStudyPage"].refresh()
        self.restart()

    def update_emp(self):
        """func set deans office employee to update and change
        page to ChangeDeansEmpPage
        """
        idx = self.list_emps.index(tk.ACTIVE)
        emp = self.controller.deans_emps[idx]

        self.controller.frames["ChangeDeansEmpPage"].set_emp(emp)
        self.controller.frames["ChangeDeansEmpPage"].fill_entry()
        self.controller.show_frame("ChangeDeansEmpPage")


class CreateDeansEmpPage(tk.Frame):
    """
    Page where we can create deans office employee
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
        self.dept_listbox()
        self.submit()

    def main_label(self):
        """create deans office employee main label
        """
        label = tk.Label(
            self,
            text="Create Dean Employee",
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

    def home_button(self):
        """create home button
        """
        btn_home = tk.Button(
            self,
            text="Home",
            command=lambda: self.home_refresh(),
            font=self.controller.normal_font
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

    def home_refresh(self):
        """func change page to StartPage
        """
        self.refresh()
        self.controller.show_frame("StartPage")

    def return_button(self):
        """create return button
        """
        btn_return = tk.Button(
            self,
            text="return",
            command=lambda: self.return_refresh(),
            font=self.controller.normal_font
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

    def return_refresh(self):
        """func change page to DeansEmpPage
        """
        self.refresh()
        self.controller.show_frame("DeansEmpPage")

    def refresh(self):
        """clear all entries
        """
        self.e_name.delete(0, tk.END)
        self.e_sec_name.delete(0, tk.END)
        self.e_lastname.delete(0, tk.END)
        self.e_ssn.delete(0, tk.END)
        self.e_email.delete(0, tk.END)

    def name_entry(self):
        """create entry for name
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
        """create entry for second name
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
            padx=5,
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
        """create entry for lastname
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
        """create entry for ssn
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
        """create entry for email
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

    def dept_listbox(self):
        """create department listbox for Deans Office Employee Page
        """
        l_dept = tk.Label(
            master=self,
            text="department",
            font=self.controller.normal_font,
            relief=tk.RAISED
        )
        l_dept.grid(
            row=0,
            column=4,
            rowspan=1,
            columnspan=3,
            sticky="nswe",
            pady=5,
            padx=5
        )

        data = [
            ('department', 20)
        ]

        self.dept_list = MultiListBox(master=self, data=data)
        self.dept_list.grid(
            row=1,
            column=4,
            rowspan=18,
            columnspan=3,
            sticky="nswe",
            pady=5,
            padx=5
        )
        self.refresh_dept_listbox()

    def refresh_dept_listbox(self):
        """refresh department listbox
        """
        self.dept_list.delete(0, tk.END)
        for i, dept in enumerate(self.controller.departments):
            self.dept_list.insert(i, (dept.get_name(),))

    def submit(self):
        """create submit button
        """
        sub_btn = tk.Button(
            master=self,
            text="submit",
            command=lambda: self.create_emp(),
            font=self.controller.normal_font
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

    def create_emp(self):
        """func create new deans_office_employee and
        config other frames
        """
        try:
            idx = self.dept_list.index(tk.ACTIVE)
            temp_dept = self.controller.departments[idx]
        except IndexError:
            temp_dept = None

        self.controller.deans_emps.append(DeansEmp(
            name=self.e_name.get(),
            sec_name=self.e_sec_name.get(),
            lastname=self.e_lastname.get(),
            ssn=self.e_ssn.get(),
            email=self.e_email.get(),
            department=temp_dept
        ))

        # insert to db
        self.controller.deans_emps[-1].insert(self.controller.db)
        self.controller.db.commit_conn()
        # refresh Field of Study frames
        self.controller.frames["CreateFieldOfStudyPage"].refresh_leader_listbox()
        self.controller.frames["ChangeFieldOfStudyPage"].refresh_leader_listbox()
        self.controller.frames["FieldOfStudyPage"].refresh()
        # refresh self
        self.refresh()
        self.controller.frames["DeansEmpPage"].restart()


class ChangeDeansEmpPage(CreateDeansEmpPage):
    """
    Page where we can update deans office employee
    """
    def __init__(self, parent, controller):
        CreateDeansEmpPage.__init__(self, parent, controller)
        if controller.deans_emps:
            self.emp = controller.deans_emps[0]

    def main_label(self):
        """create update deans office employee main label
        """
        label = tk.Label(
            self,
            text="Change Dean Employee",
            font=self.controller.title_font,
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
        """create submit button
        """
        sub_btn = tk.Button(
            master=self,
            text="submit",
            command=lambda: self.update_emp(),
            font=self.controller.normal_font, relief=tk.RAISED
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
        self.e_name.insert(tk.END, str(self.emp.get_name()))
        self.e_sec_name.insert(tk.END, str(self.emp.get_sec_name()))
        self.e_lastname.insert(tk.END, str(self.emp.get_lastname()))
        self.e_ssn.insert(tk.END, str(self.emp.get_ssn()))
        self.e_email.insert(tk.END, str(self.emp.get_email()))

    def set_emp(self, emp):
        """set deans office employee instance

        Args:
            emp (DeansEmp): deans office emp which we want update
        """
        self.emp = emp

    def update_emp(self):
        """func update deans office employee and
        config other frames
        """
        self.set_attr_emp()
        self.emp.update(self.controller.db)
        self.controller.db.commit_conn()

        # config after update
        self.controller.frames["CreateFieldOfStudyPage"].refresh_leader_listbox()
        self.controller.frames["ChangeFieldOfStudyPage"].refresh_leader_listbox()
        self.controller.frames["FieldOfStudyPage"].refresh()
        self.refresh()
        self.controller.frames["DeansEmpPage"].restart()

    def set_attr_emp(self):
        """change attrs of deans office employee
        """
        try:
            idx = self.dept_list.index(tk.ACTIVE)
            dept = self.controller.departments[idx]
            self.emp.set_department(dept)
        except IndexError:
            pass

        self.emp.set_name(self.e_name.get())
        self.emp.set_sec_name(self.e_sec_name.get())
        self.emp.set_lastname(self.e_lastname.get())
        self.emp.set_ssn(self.e_ssn.get())
        self.emp.set_email(self.e_email.get())
