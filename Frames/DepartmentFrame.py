import tkinter as tk

from Tables.Department import Department

from Frames.extendTk import MultiListBox

class DepartmentPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.main_label()

        self.dept_listbox()
        self.refresh_button()
        self.buttons()

    
    def main_label(self):
        label = tk.Label(
            self,
            text="Department Page",
            font=self.controller.title_font
        )
        label.pack(side=tk.TOP, fill=tk.X, pady=10)


    def buttons(self):
        #Return Home Page
        btn_return = tk.Button(
            self,
            text="Return to Home Page",
            command=lambda: self.controller.show_frame("StartPage")
        )
        btn_return.pack()
        #Create Department Button
        btn_create = tk.Button(
            self,
            text="Create Department",
            command=lambda : self.controller.show_frame("CreateDepartmentPage")
        )
        btn_create.pack()
        #Delete Department Button
        btn_delete = tk.Button(
            self,
            text="Delete Department",
            command=lambda : self.delete_dept()
        )
        btn_delete.pack()
        #Change Department Button
        btn_change = tk.Button(
            self,
            text="Change Department",
            command=lambda : self.update_dept()
        )
        btn_change.pack()


    def dept_listbox(self):
        f_dept = tk.Frame(master=self)
        f_dept.pack()
        l_dept = tk.Label(master=f_dept, text="select department")
        l_dept.pack()

        data = [
            ('id', 10),
            ('building', 20),
            ('name', 20),
            ('office start', 10),
            ('office stop', 10),
            ('dean', 20)
        ]

        self.list_depts = MultiListBox(master=f_dept, data=data)
        self.refresh()
        self.list_depts.pack()


    def delete_dept(self):
        idx = self.list_depts.index(tk.ACTIVE)
        del_dept = self.controller.departments.pop(idx)

        del_dept.delete(self.controller.db)
        self.controller.db.commit_conn()

        del del_dept

        self.controller.frames["CreateFieldOfStudyPage"].refresh_dept_listbox()
        self.controller.frames["ChangeFieldOfStudyPage"].refresh_dept_listbox()
        self.controller.frames["FieldOfStudyPage"].refresh()
        self.controller.frames["CreateDeansEmpPage"].refresh_dept_listbox()
        self.controller.frames["ChangeDeansEmpPage"].refresh_dept_listbox()
        self.controller.frames["DeansEmpPage"].refresh()
        self.controller.frames["CreateTeacherPage"].refresh_dept_listbox()
        self.controller.frames["ChangeTeacherPage"].refresh_dept_listbox()
        self.controller.frames["TeacherPage"].refresh()
        self.restart()


    def update_dept(self):
        idx = self.list_depts.index(tk.ACTIVE)
        dept = self.controller.departments[idx]

        #self.controller.frames["ChangeDepartmentPage"].refresh_building_listbox()
        #self.controller.frames["ChangeDepartmentPage"].refresh_dean_listbox()
        self.controller.frames["ChangeDepartmentPage"].set_dept(dept)
        self.controller.frames["ChangeDepartmentPage"].fill_entry()
        self.controller.show_frame("ChangeDepartmentPage")


    def restart(self):
        self.refresh()
        self.controller.show_frame("DepartmentPage")


    def refresh_button(self):
        f_refresh = tk.Frame(master=self)
        f_refresh.pack()
        btn_refresh = tk.Button(
            master=f_refresh,
            text="refresh",
            command=lambda : self.restart()
        )
        btn_refresh.pack()

    def refresh(self):
        self.list_depts.delete(0, tk.END)
        for i, dept in enumerate(self.controller.departments):
            try:
                dean = dept.get_dean().get_name() + " " + dept.get_dean().get_lastname()
            except AttributeError:
                dean = "-----------"

            try:
                building = dept.get_building().get_name()
            except AttributeError:
                building = "-----------"

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
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
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
        label = tk.Label(
            self,
            text="Create Department",
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
        self.controller.show_frame("DepartmentPage")


    def home_refresh(self):
        self.refresh()
        self.controller.show_frame("StartPage")


    def refresh(self):
        self.e_name.delete(0, tk.END)
        self.e_off_start.delete(0, tk.END)
        self.e_off_stop.delete(0, tk.END)


    def name_entry(self):
        f_name = tk.Frame(master=self)
        f_name.pack()

        l_name = tk.Label(master=f_name, text="name")
        l_name.pack()

        self.e_name = tk.Entry(master=f_name)
        self.e_name.pack()


    def off_start_entry(self):
        f_off_start = tk.Frame(master=self)
        f_off_start.pack()

        l_off_start = tk.Label(master=f_off_start, text="office start")
        l_off_start.pack()

        self.e_off_start = tk.Entry(master=f_off_start)
        self.e_off_start.pack()


    def off_stop_entry(self):
        f_off_stop = tk.Frame(master=self)
        f_off_stop.pack()

        l_off_stop = tk.Label(master=f_off_stop, text="office stop")
        l_off_stop.pack()

        self.e_off_stop = tk.Entry(master=f_off_stop)
        self.e_off_stop.pack()


    def dean_listbox(self):
        f_dean = tk.Frame(master=self)
        f_dean.pack()

        l_dean = tk.Label(master=f_dean, text="dean")
        l_dean.pack()

        self.list_dean = tk.Listbox(master=f_dean)
        for i, dean in enumerate(self.controller.deans):
            full_name = dean.get_name() + " " + dean.get_lastname()
            if dean not in Department.deans:
                self.list_dean.insert(i, full_name)
        self.list_dean.pack()


    def refresh_dean_listbox(self):
        self.list_dean.delete(0, tk.END)
        for i, dean in enumerate(self.controller.deans):
            full_name = dean.get_name() + " " + dean.get_lastname()
            if dean not in Department.deans:
                self.list_dean.insert(i, full_name)

    
    def building_listbox(self):
        f_building = tk.Frame(master=self)
        f_building.pack()

        l_building = tk.Label(master=f_building, text="building")
        l_building.pack()

        self.list_building = tk.Listbox(master=f_building)
        for i, building in enumerate(self.controller.buildings):
            if building not in Department.buildings:
                self.list_building.insert(i, building.get_name())
        self.list_building.pack()

    
    def refresh_building_listbox(self):
        self.list_building.delete(0, tk.END)
        for i, building in enumerate(self.controller.buildings):
            if building not in Department.buildings:
                self.list_building.insert(i, building.get_name())


    def submit(self):
        f_submit = tk.Frame(master=self)
        f_submit.pack()

        sub_btn = tk.Button(
            master=f_submit,
            text="submit",
            command=lambda : self.create_dept()
        )
        sub_btn.pack()


    def create_dept(self):
        temp_dean = None
        for dean in self.controller.deans:
            full_name = dean.get_name() + " " + dean.get_lastname()
            if self.list_dean.get(tk.ACTIVE) == full_name:
                temp_dean = dean
                break


        temp_building = None
        for building in self.controller.buildings:
            if self.list_building.get(tk.ACTIVE) == building.get_name():
                temp_building = building
                break


        self.controller.departments.append(Department(
            building=temp_building,
            name=self.e_name.get(),
            off_start=self.e_off_start.get(),
            off_stop=self.e_off_stop.get(),
            dean=temp_dean
        ))

        self.controller.frames["CreateFieldOfStudyPage"].refresh_dept_listbox()
        self.controller.frames["ChangeFieldOfStudyPage"].refresh_dept_listbox()
        self.controller.frames["FieldOfStudyPage"].refresh()
        self.controller.frames["CreateDeansEmpPage"].refresh_dept_listbox()
        self.controller.frames["ChangeDeansEmpPage"].refresh_dept_listbox()
        self.controller.frames["DeansEmpPage"].refresh()
        self.controller.frames["CreateTeacherPage"].refresh_dept_listbox()
        self.controller.frames["ChangeTeacherPage"].refresh_dept_listbox()
        self.controller.frames["TeacherPage"].refresh()
        self.controller.departments[-1].insert(self.controller.db)
        self.controller.db.commit_conn()
        self.controller.frames["DepartmentPage"].restart()



class ChangeDepartmentPage(CreateDepartmentPage):
    def __init__(self, parent, controller):
        CreateDepartmentPage.__init__(self, parent, controller)
        if controller.departments:
            self.dept = controller.departments[0]


    def main_label(self):
        label = tk.Label(
            self,
            text="Change Department",
            font=self.controller.title_font
        )
        label.pack(side=tk.TOP, fill=tk.X, pady=10)


    def submit(self):
        f_submit = tk.Frame(master=self)
        f_submit.pack()

        sub_btn = tk.Button(
            master=f_submit,
            text="submit",
            command=lambda : self.update_dept()
        )
        sub_btn.pack()


    def fill_entry(self):
        self.e_name.insert(tk.END, str(self.dept.get_name()))
        self.e_off_start.insert(tk.END, str(self.dept.get_off_start()))
        self.e_off_stop.insert(tk.END, str(self.dept.get_off_stop()))


    def set_dept(self, dept):
        self.dept = dept

    
    def update_dept(self):
        self.set_attr_dept()
        self.dept.update(self.controller.db)
        self.controller.db.commit_conn()

        #config after update
        self.refresh()
        self.controller.frames["CreateFieldOfStudyPage"].refresh_dept_listbox()
        self.controller.frames["ChangeFieldOfStudyPage"].refresh_dept_listbox()
        self.controller.frames["FieldOfStudyPage"].refresh()

        self.controller.frames["CreateDeansEmpPage"].refresh_dept_listbox()
        self.controller.frames["ChangeDeansEmpPage"].refresh_dept_listbox()
        self.controller.frames["DeansEmpPage"].refresh()

        self.controller.frames["CreateTeacherPage"].refresh_dept_listbox()
        self.controller.frames["ChangeTeacherPage"].refresh_dept_listbox()
        self.controller.frames["TeacherPage"].refresh()

        self.controller.frames["DepartmentPage"].restart()


    def set_attr_dept(self):
        for dean in self.controller.deans:
            full_name = dean.get_name() + " " + dean.get_lastname()
            if self.list_dean.get(tk.ACTIVE) == full_name:
                self.dept.set_dean(dean)
                break

        for building in self.controller.buildings:
            if self.list_building.get(tk.ACTIVE) == building.get_name():
                self.dept.set_building(building)
                break
        
        self.dept.set_name(self.e_name.get())
        self.dept.set_off_start(self.e_off_start.get())
        self.dept.set_off_stop(self.e_off_stop.get())