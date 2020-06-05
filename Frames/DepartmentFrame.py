import tkinter as tk

from Tables.Department import Department

from tk_extension.multilistBox import MultiListBox


class DepartmentPage(tk.Frame):
    """
    Main Department Page
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.columnconfigure([x for x in range(7)], minsize=250)
        self.rowconfigure([x for x in range(9)], minsize=100)
        self.controller = controller
        self.main_label()

        self.dept_listbox()
        self.refresh_button()
        self.buttons()

    def main_label(self):
        """create department main label
        """
        label = tk.Label(
            self,
            text="Department Page",
            font=self.controller.title_font
        )
        label.grid(row=0, column=6, sticky="news", padx=5, pady=5)

    def buttons(self):
        """create department page buttons
        """
        # Return Home Page
        btn_return = tk.Button(
            self,
            text="Home",
            command=lambda: self.controller.show_frame("StartPage"),
            font=self.controller.normal_font
        )
        btn_return.grid(row=4, column=6, sticky="news", padx=5, pady=5)
        # Create Department Button
        btn_create = tk.Button(
            self,
            text="Create Department",
            command=lambda: self.create_dept(),
            font=self.controller.normal_font
        )
        btn_create.grid(row=1, column=6, sticky="news", padx=5, pady=5)
        # Delete Department Button
        btn_delete = tk.Button(
            self,
            text="Delete Department",
            command=lambda: self.delete_dept(),
            font=self.controller.normal_font
        )
        btn_delete.grid(row=2, column=6, sticky="news", padx=5, pady=5)
        # Change Department Button
        btn_change = tk.Button(
            self,
            text="Change Department",
            command=lambda: self.update_dept(),
            font=self.controller.normal_font
        )
        btn_change.grid(row=3, column=6, sticky="news", padx=5, pady=5)

    def dept_listbox(self):
        """create department listbox
        """
        data = [
            ('id', 10),
            ('building', 20),
            ('name', 20),
            ('office start', 10),
            ('office stop', 10),
            ('dean', 20)
        ]

        self.list_depts = MultiListBox(master=self, data=data)
        self.refresh()
        self.list_depts.grid(
            row=0,
            column=0,
            columnspan=6,
            rowspan=9,
            sticky="news",
            padx=5,
            pady=5
        )

    def delete_dept(self):
        """func delete departmeny from listbox and config other frame
        """
        idx = self.list_depts.index(tk.ACTIVE)
        del_dept = self.controller.departments.pop(idx)

        del_dept.delete(self.controller.db)
        self.controller.db.commit_conn()

        del del_dept
        # config
        # Field of Study
        self.controller.frames["CreateFieldOfStudyPage"].refresh_dept_listbox()
        self.controller.frames["ChangeFieldOfStudyPage"].refresh_dept_listbox()
        self.controller.frames["FieldOfStudyPage"].refresh()
        # Deans office employee
        self.controller.frames["CreateDeansEmpPage"].refresh_dept_listbox()
        self.controller.frames["ChangeDeansEmpPage"].refresh_dept_listbox()
        self.controller.frames["DeansEmpPage"].refresh()
        # Teacher
        self.controller.frames["CreateTeacherPage"].refresh_dept_listbox()
        self.controller.frames["ChangeTeacherPage"].refresh_dept_listbox()
        self.controller.frames["TeacherPage"].refresh()
        # self
        self.controller.frames["ChangeDepartmentPage"].refresh_building_listbox()
        self.controller.frames["ChangeDepartmentPage"].refresh_dean_listbox()
        self.restart()

    def update_dept(self):
        """func set department to update and change page to ChangeDepartmentPage
        """
        idx = self.list_depts.index(tk.ACTIVE)
        dept = self.controller.departments[idx]

        self.controller.frames["ChangeDepartmentPage"].refresh_building_listbox()
        self.controller.frames["ChangeDepartmentPage"].refresh_dean_listbox()

        self.controller.frames["ChangeDepartmentPage"].set_dept(dept)
        self.controller.frames["ChangeDepartmentPage"].fill_entry()
        self.controller.show_frame("ChangeDepartmentPage")

    def create_dept(self):
        """func change pagr to CreateDepartmentPage
        """
        self.controller.frames["CreateDepartmentPage"].refresh_building_listbox()
        self.controller.frames["CreateDepartmentPage"].refresh_dean_listbox()
        self.controller.show_frame("CreateDepartmentPage")

    def restart(self):
        """func restart frame
        """
        self.refresh()
        self.controller.show_frame("DepartmentPage")

    def refresh_button(self):
        """create refresh button
        """
        btn_refresh = tk.Button(
            master=self,
            text="refresh",
            command=lambda: self.restart(),
            font=self.controller.normal_font
        )
        btn_refresh.grid(row=8, column=6, sticky="news", padx=5, pady=5)

    def refresh(self):
        """func refresh department listbox
        """
        self.list_depts.delete(0, tk.END)
        for i, dept in enumerate(self.controller.departments):
            try:
                dean = dept.get_dean().get_name()
                + " " + dept.get_dean().get_lastname()
            except AttributeError:
                dean = "NULL"

            try:
                building = dept.get_building().get_name()
            except AttributeError:
                building = "NULL"

            output = (
                dept.get_id(),
                building,
                dept.get_name(),
                dept.get_off_start(),
                dept.get_off_stop(),
                dean
            )
            self.list_depts.insert(i, output)


class CreateDepartmentPage(tk.Frame):
    """
    Page where we can create department
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
        self.off_start_entry()
        self.off_stop_entry()
        self.dean_listbox()
        self.building_listbox()
        self.submit()

    def main_label(self):
        """create department main label
        """
        label = tk.Label(
            self,
            text="Create Department",
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

    def return_refresh(self):
        """func change page to DepartmentPage
        """
        self.refresh()
        self.controller.show_frame("DepartmentPage")

    def home_refresh(self):
        """func change page to StartPage
        """
        self.refresh()
        self.controller.show_frame("StartPage")

    def refresh(self):
        """clear all entries
        """
        self.e_name.delete(0, tk.END)
        self.e_off_start.delete(0, tk.END)
        self.e_off_stop.delete(0, tk.END)

    def name_entry(self):
        """create entry for name with label
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

        self.e_name = tk.Entry(master=self, font=self.controller.entry_font)
        self.e_name.grid(
            row=2,
            column=0,
            columnspan=4,
            sticky="nswe",
            pady=0,
            padx=5
        )

    def off_start_entry(self):
        """create entry for office start with label
        """
        l_off_start = tk.Label(
            master=self,
            text="office start",
            font=self.controller.normal_font,
            anchor=tk.W,
            relief=tk.RAISED
        )
        l_off_start.grid(
            row=3,
            column=0,
            columnspan=4,
            sticky="nswe",
            pady=0,
            padx=5
        )

        self.e_off_start = tk.Entry(
            master=self,
            font=self.controller.entry_font
        )
        self.e_off_start.grid(
            row=4,
            column=0,
            columnspan=4,
            sticky="nswe",
            pady=0,
            padx=5
        )

    def off_stop_entry(self):
        """create entry for office stop with label
        """
        l_off_stop = tk.Label(
            master=self,
            text="office stop",
            font=self.controller.normal_font,
            anchor=tk.W,
            relief=tk.RAISED
        )
        l_off_stop.grid(
            row=5,
            column=0,
            columnspan=4,
            sticky="nswe",
            pady=0,
            padx=5
        )

        self.e_off_stop = tk.Entry(
            master=self,
            font=self.controller.entry_font
        )
        self.e_off_stop.grid(
            row=6,
            column=0,
            columnspan=4,
            sticky="nswe",
            pady=0,
            padx=5
        )

    def dean_listbox(self):
        """create dean listbox for department page
        """
        l_dean = tk.Label(
            master=self,
            text="dean",
            font=self.controller.normal_font,
            relief=tk.RAISED
        )
        l_dean.grid(
            row=0,
            column=4,
            rowspan=1,
            columnspan=3,
            sticky="nswe",
            pady=5,
            padx=5
        )

        data = [
            ('name', 10),
            ('lastname', 20)
        ]

        self.list_dean = MultiListBox(master=self, data=data)
        self.list_dean.grid(
            row=1,
            column=4,
            rowspan=8,
            columnspan=3,
            sticky="nswe",
            pady=5,
            padx=5
        )
        self.refresh_dean_listbox()

    def refresh_dean_listbox(self):
        """refresh dean listbox
        """
        self.list_dean.delete(0, tk.END)
        for i, dean in enumerate(self.controller.deans):
            output = (
                dean.get_name(),
                dean.get_lastname()
            )

            self.list_dean.insert(i, output)

    def building_listbox(self):
        """create building listbox for department
        """
        l_building = tk.Label(
            master=self,
            text="building",
            font=self.controller.normal_font,
            relief=tk.RAISED
        )
        l_building.grid(
            row=9,
            column=4,
            rowspan=1,
            columnspan=3,
            sticky="nswe",
            pady=5,
            padx=5
        )

        data = [
            ('name', 20),
        ]

        self.list_building = MultiListBox(master=self, data=data)
        self.list_building.grid(
            row=10,
            column=4,
            rowspan=8,
            columnspan=3,
            sticky="nswe",
            pady=5,
            padx=5
        )
        self.refresh_building_listbox()

    def refresh_building_listbox(self):
        """refresh building listbox
        """
        self.list_building.delete(0, tk.END)
        for i, building in enumerate(self.controller.buildings):
            output = (
                building.get_name(),
            )

            self.list_building.insert(i, output)

    def submit(self):
        """create submit button
        """
        sub_btn = tk.Button(
            master=self,
            text="submit",
            command=lambda: self.create_dept(),
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

    def create_dept(self):
        """func create new department and config other frames
        """
        try:
            idx = self.list_dean.index(tk.ACTIVE)
            temp_dean = self.controller.deans[idx]
        except IndexError:
            temp_dean = None

        try:
            idx = self.list_building.index(tk.ACTIVE)
            temp_building = self.controller.buildings[idx]
        except IndexError:
            temp_building = None

        self.controller.departments.append(Department(
            building=temp_building,
            name=self.e_name.get(),
            off_start=self.e_off_start.get(),
            off_stop=self.e_off_stop.get(),
            dean=temp_dean
        ))

        # field of study page
        self.controller.frames["CreateFieldOfStudyPage"].refresh_dept_listbox()
        self.controller.frames["ChangeFieldOfStudyPage"].refresh_dept_listbox()
        self.controller.frames["FieldOfStudyPage"].refresh()
        # deans emp page
        self.controller.frames["CreateDeansEmpPage"].refresh_dept_listbox()
        self.controller.frames["ChangeDeansEmpPage"].refresh_dept_listbox()
        self.controller.frames["DeansEmpPage"].refresh()
        # teacher page
        self.controller.frames["CreateTeacherPage"].refresh_dept_listbox()
        self.controller.frames["ChangeTeacherPage"].refresh_dept_listbox()
        self.controller.frames["TeacherPage"].refresh()
        # insert to db
        self.controller.departments[-1].insert(self.controller.db)
        self.controller.db.commit_conn()
        # refresh self
        self.refresh()
        self.controller.frames["DepartmentPage"].restart()


class ChangeDepartmentPage(CreateDepartmentPage):
    """
    Page where we can update department
    """
    def __init__(self, parent, controller):
        CreateDepartmentPage.__init__(self, parent, controller)
        if controller.departments:
            self.dept = controller.departments[0]

    def main_label(self):
        """create update department main label
        """
        label = tk.Label(
            self,
            text="Change Department",
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

    def submit(self):
        """create submit button
        """
        sub_btn = tk.Button(
            master=self,
            text="submit",
            command=lambda: self.update_dept(),
            font=self.controller.normal_font
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
        self.e_name.insert(tk.END, str(self.dept.get_name()))
        self.e_off_start.insert(tk.END, str(self.dept.get_off_start()))
        self.e_off_stop.insert(tk.END, str(self.dept.get_off_stop()))

    def set_dept(self, dept):
        """set department instance

        Args:
            dept (Department): department which we want update
        """
        self.dept = dept

    def update_dept(self):
        """func update department and config other frames
        """
        self.set_attr_dept()
        self.dept.update(self.controller.db)
        self.controller.db.commit_conn()

        # config after update
        self.controller.frames["CreateFieldOfStudyPage"].refresh_dept_listbox()
        self.controller.frames["ChangeFieldOfStudyPage"].refresh_dept_listbox()
        self.controller.frames["FieldOfStudyPage"].refresh()

        self.controller.frames["CreateDeansEmpPage"].refresh_dept_listbox()
        self.controller.frames["ChangeDeansEmpPage"].refresh_dept_listbox()
        self.controller.frames["DeansEmpPage"].refresh()

        self.controller.frames["CreateTeacherPage"].refresh_dept_listbox()
        self.controller.frames["ChangeTeacherPage"].refresh_dept_listbox()
        self.controller.frames["TeacherPage"].refresh()

        self.refresh()
        self.controller.frames["DepartmentPage"].restart()

    def set_attr_dept(self):
        """change attrs of department
        """
        try:
            idx = self.list_dean.index(tk.ACTIVE)
            temp_dean = self.controller.deans[idx]
            self.dept.set_dean(temp_dean)
        except IndexError:
            pass

        try:
            idx = self.list_building.index(tk.ACTIVE)
            temp_building = self.controller.buildings[idx]
            self.dept.set_building(temp_building)
        except IndexError:
            pass

        self.dept.set_name(self.e_name.get())
        self.dept.set_off_start(self.e_off_start.get())
        self.dept.set_off_stop(self.e_off_stop.get())
