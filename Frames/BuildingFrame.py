import tkinter as tk

from Tables.Building import Building

from Frames.extendTk import MultiListBox


class BuildingPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.main_label()

        self.building_listbox()
        self.refresh_button()
        self.buttons()


    def main_label(self):
        label = tk.Label(
            self,
            text="Building Page",
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
        #Create Building Button
        btn_create = tk.Button(
            self,
            text="Create Building",
            command=lambda : self.controller.show_frame("CreateBuildingPage")
        )
        btn_create.pack()
        #Delete Building Button
        btn_delete = tk.Button(
            self,
            text="Delete Building",
            command=lambda : self.delete_building()
        )
        btn_delete.pack()
        #Change Building Button
        btn_update = tk.Button(
            self,
            text="Change Building",
            command=lambda : self.update_building()
        )
        btn_update.pack()


    def building_listbox(self):
        f_building = tk.Frame(master=self)
        f_building.pack()
        l_building = tk.Label(master=f_building, text="select building")
        l_building.pack()

        data = [
            ('id', 10),
            ('street', 20),
            ('name', 20),
            ('number', 10)
        ]

        self.list_buildings = MultiListBox(master=f_building, data=data)
        self.refresh()
        self.list_buildings.pack()


    def refresh(self):
        self.list_buildings.delete(0, tk.END)
        for i, building in enumerate(self.controller.buildings):
            output = (
                building.get_id(),
                building.get_street_name(),
                building.get_name(),
                building.get_number()
            )
            self.list_buildings.insert(i, output)


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
        self.controller.show_frame("BuildingPage")


    def delete_building(self):
        idx = self.list_buildings.index(tk.ACTIVE)
        del_building = self.controller.buildings.pop(idx)

        del_building.delete(self.controller.db)
        self.update_department(del_building)
        self.controller.db.commit_conn()

        del del_building
        self.controller.frames["CreateDepartmentPage"].refresh_building_listbox()
        self.controller.frames["ChangeDepartmentPage"].refresh_building_listbox()
        self.controller.frames["DepartmentPage"].refresh()
        self.refresh()


    def update_department(self, building):
        for dept in self.controller.departments:
            if dept.get_building() == building:
                dept.set_building(None)
                dept.update(self.controller.db)
                self.controller.db.commit_conn()
                break

    
    def update_building(self):
        idx = self.list_buildings.index(tk.ACTIVE)
        building = self.controller.buildings[idx]

        self.controller.frames["ChangeBuildingPage"].set_building(building)
        self.controller.frames["ChangeBuildingPage"].fill_entry()
        self.controller.show_frame("ChangeBuildingPage")



class CreateBuildingPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        self.main_label()
        self.return_button()
        self.home_button()
        self.name_entry()
        self.street_name_entry()
        self.number_entry()
        self.submit()


    def main_label(self):
        label = tk.Label(
            self,
            text="Create Building",
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


    def refresh(self):
        self.e_name.delete(0, tk.END)
        self.e_street.delete(0, tk.END)
        self.e_number.delete(0, tk.END)


    def return_refresh(self):
        self.refresh()
        self.controller.show_frame("BuildingPage")


    def name_entry(self):
        f_name = tk.Frame(master=self)
        f_name.pack()

        l_name = tk.Label(master=f_name, text="name")
        l_name.pack()

        self.e_name = tk.Entry(master=f_name)
        self.e_name.pack()


    def street_name_entry(self):
        f_street = tk.Frame(master=self)
        f_street.pack()

        l_street = tk.Label(master=f_street, text="street name")
        l_street.pack()

        self.e_street = tk.Entry(master=f_street)
        self.e_street.pack()


    def number_entry(self):
        f_number = tk.Frame(master=self)
        f_number.pack()

        l_number = tk.Label(master=f_number, text="number")
        l_number.pack()

        self.e_number = tk.Entry(master=f_number)
        self.e_number.pack()


    def submit(self):
        sub_btn = tk.Button(
            master=self,
            text="submit",
            command=lambda : self.create_building()
        )
        sub_btn.pack()


    def create_building(self):
        self.controller.buildings.append(Building(
            street_name=self.e_street.get(),
            name=self.e_name.get(),
            number=self.e_number.get()
        ))

        self.controller.buildings[-1].insert(self.controller.db)
        self.controller.db.commit_conn()

        self.controller.frames["CreateDepartmentPage"].refresh_building_listbox()
        self.controller.frames["ChangeDepartmentPage"].refresh_building_listbox()
        self.controller.frames["DepartmentPage"].refresh()

        self.controller.frames["BuildingPage"].restart()
        


class ChangeBuildingPage(CreateBuildingPage):
    def __init__(self, parent, controller):
        CreateBuildingPage.__init__(self, parent, controller)
        if controller.buildings:
            self.building = controller.buildings[0]

    
    def main_label(self):
        label = tk.Label(
            self,
            text="Change Building",
            font=self.controller.title_font
        )
        label.pack(side=tk.TOP, fill=tk.X, pady=10)


    def submit(self):
        f_submit = tk.Frame(master=self)
        f_submit.pack()

        sub_btn = tk.Button(
            master=f_submit,
            text="submit",
            command=lambda : self.update_building()
        )
        sub_btn.pack()


    def fill_entry(self):
        self.e_name.insert(tk.END, str(self.building.get_name()))
        self.e_street.insert(tk.END, str(self.building.get_street_name()))
        self.e_number.insert(tk.END, str(self.building.get_number()))


    def set_building(self, building):
        self.building = building


    def update_building(self):
        self.set_attr_building()
        self.building.update(self.controller.db)

        #config after update
        self.refresh()
        self.controller.db.commit_conn()
        self.controller.frames["CreateDepartmentPage"].refresh_building_listbox()
        self.controller.frames["ChangeDepartmentPage"].refresh_building_listbox()
        self.controller.frames["DepartmentPage"].refresh()

        self.controller.frames["BuildingPage"].restart()


    def set_attr_building(self):
        self.building.set_name(self.e_name.get())
        self.building.set_street_name(self.e_street.get())
        self.building.set_number(self.e_number.get())
