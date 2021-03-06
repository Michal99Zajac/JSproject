import tkinter as tk

from Tables.Building import Building

from tk_extension.multilistBox import MultiListBox


class BuildingPage(tk.Frame):
    """
    First building page
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.columnconfigure([x for x in range(7)], minsize=250)
        self.rowconfigure([x for x in range(9)], minsize=100)
        self.controller = controller
        self.main_label()

        self.building_listbox()
        self.refresh_button()
        self.buttons()

    def main_label(self):
        """create building main label
        """
        label = tk.Label(
            self,
            text="Building Page",
            font=self.controller.title_font
        )
        label.grid(row=0, column=6, sticky="news", padx=5, pady=5)

    def buttons(self):
        """create building page buttons
        """
        # Return Home Button
        btn_return = tk.Button(
            self,
            text="Home",
            command=lambda: self.controller.show_frame("StartPage"),
            font=self.controller.normal_font
        )
        btn_return.grid(row=4, column=6, sticky="news", padx=5, pady=5)
        # Create Building Button
        btn_create = tk.Button(
            self,
            text="Create Building",
            command=lambda: self.controller.show_frame("CreateBuildingPage"),
            font=self.controller.normal_font
        )
        btn_create.grid(row=1, column=6, sticky="news", padx=5, pady=5)
        # Delete Building Button
        btn_delete = tk.Button(
            self,
            text="Delete Building",
            command=lambda: self.delete_building(),
            font=self.controller.normal_font
        )
        btn_delete.grid(row=2, column=6, sticky="news", padx=5, pady=5)
        # Change Building Button
        btn_update = tk.Button(
            self,
            text="Change Building",
            command=lambda: self.update_building(),
            font=self.controller.normal_font
        )
        btn_update.grid(row=3, column=6, sticky="news", padx=5, pady=5)

    def building_listbox(self):
        """create buliding listbox
        """
        data = [
            ('id', 10),
            ('street', 20),
            ('name', 20),
            ('number', 10)
        ]

        self.list_buildings = MultiListBox(master=self, data=data)
        self.refresh()
        self.list_buildings.grid(
            row=0,
            column=0,
            columnspan=6,
            rowspan=9,
            sticky="news",
            padx=5,
            pady=5
        )

    def refresh(self):
        """func refresh building listbox
        """
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
        """create refresh button
        """
        btn_refresh = tk.Button(
            master=self,
            text="refresh",
            command=lambda: self.restart(),
            font=self.controller.normal_font
        )
        btn_refresh.grid(row=8, column=6, sticky="news", padx=5, pady=5)

    def restart(self):
        """func restart frame
        """
        self.refresh()
        self.controller.show_frame("BuildingPage")

    def delete_building(self):
        """func delete building from listbox and config other frames
        """
        idx = self.list_buildings.index(tk.ACTIVE)
        del_building = self.controller.buildings.pop(idx)

        del_building.delete(self.controller.db)
        self.update_department(del_building)
        self.controller.db.commit_conn()

        del del_building
        # config
        self.controller.frames["CreateDepartmentPage"].refresh_building_listbox()
        self.controller.frames["ChangeDepartmentPage"].refresh_building_listbox()
        self.controller.frames["DepartmentPage"].refresh()
        self.controller.frames["CreateRoomPage"].refresh_building_listbox()
        self.controller.frames["ChangeRoomPage"].refresh_building_listbox()
        self.controller.frames["RoomPage"].refresh()
        self.refresh()

    def update_building(self):
        """func set building and change page to ChangeBuildingPage
        """
        idx = self.list_buildings.index(tk.ACTIVE)
        building = self.controller.buildings[idx]

        self.controller.frames["ChangeBuildingPage"].set_building(building)
        self.controller.frames["ChangeBuildingPage"].fill_entry()
        self.controller.show_frame("ChangeBuildingPage")


class CreateBuildingPage(tk.Frame):
    """
    Page where we can create building
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.columnconfigure([x for x in range(9)], minsize=250)
        self.rowconfigure([x for x in range(18)], minsize=50)
        self.controller = controller
        self.main_label()
        self.empty_space()
        self.return_button()
        self.home_button()
        self.name_entry()
        self.street_name_entry()
        self.number_entry()
        self.submit()

    def main_label(self):
        """create building main label
        """
        label = tk.Label(
            self,
            text="Create Building",
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

    def refresh(self):
        """clear all entries
        """
        self.e_name.delete(0, tk.END)
        self.e_street.delete(0, tk.END)
        self.e_number.delete(0, tk.END)

    def return_refresh(self):
        """func change page to BuildingPage
        """
        self.refresh()
        self.controller.show_frame("BuildingPage")

    def empty_space(self):
        """create grey block on the left
        """
        frame = tk.Frame(
            master=self,
            relief=tk.SUNKEN,
            borderwidth=5,
            bg="gray"
        )
        frame.grid(
            row=0,
            column=4,
            rowspan=18,
            columnspan=3,
            sticky="news",
            pady=5,
            padx=5
        )

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
            sticky="news",
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
            sticky="news",
            pady=0,
            padx=5
        )

    def street_name_entry(self):
        """create entry for street_name
        """
        l_street = tk.Label(
            master=self,
            text="street name",
            font=self.controller.normal_font,
            anchor=tk.W,
            relief=tk.RAISED
        )
        l_street.grid(
            row=3,
            column=0,
            columnspan=4,
            sticky="news",
            pady=0,
            padx=5
        )

        self.e_street = tk.Entry(
            master=self,
            font=self.controller.entry_font
        )
        self.e_street.grid(
            row=4,
            column=0,
            columnspan=4,
            sticky="news",
            pady=0,
            padx=5
        )

    def number_entry(self):
        """create entry for number
        """
        l_number = tk.Label(
            master=self,
            text="number",
            font=self.controller.normal_font,
            anchor=tk.W,
            relief=tk.RAISED
        )
        l_number.grid(
            row=5,
            column=0,
            columnspan=4,
            sticky="news",
            pady=0,
            padx=5
        )

        self.e_number = tk.Entry(
            master=self,
            font=self.controller.entry_font
        )
        self.e_number.grid(
            row=6,
            column=0,
            columnspan=4,
            sticky="news",
            pady=0,
            padx=5
        )

    def submit(self):
        """create submit button
        """
        sub_btn = tk.Button(
            master=self,
            text="submit",
            command=lambda: self.create_building(),
            font=self.controller.normal_font
        )
        sub_btn.grid(
            row=14,
            column=0,
            rowspan=2,
            columnspan=4,
            sticky="news",
            pady=5,
            padx=5
        )

    def create_building(self):
        """func create new building and config other frames
        """
        self.controller.buildings.append(Building(
            street_name=self.e_street.get(),
            name=self.e_name.get(),
            number=self.e_number.get()
        ))

        # insert to db
        self.controller.buildings[-1].insert(self.controller.db)
        self.controller.db.commit_conn()
        # refresh department frames
        self.controller.frames["CreateDepartmentPage"].refresh_building_listbox()
        self.controller.frames["ChangeDepartmentPage"].refresh_building_listbox()
        self.controller.frames["DepartmentPage"].refresh()
        # refresh room frames
        self.controller.frames["CreateRoomPage"].refresh_building_listbox()
        self.controller.frames["ChangeRoomPage"].refresh_building_listbox()
        self.controller.frames["RoomPage"].refresh()
        # refresh self
        self.refresh()
        self.controller.frames["BuildingPage"].restart()


class ChangeBuildingPage(CreateBuildingPage):
    """
    Page where we can update building
    """
    def __init__(self, parent, controller):
        CreateBuildingPage.__init__(self, parent, controller)
        if controller.buildings:
            self.building = controller.buildings[0]

    def main_label(self):
        """update building main label
        """
        label = tk.Label(
            self,
            text="Change Building",
            font=self.controller.title_font
        )
        label.grid(
            row=0,
            column=0,
            rowspan=1,
            columnspan=4,
            sticky="news",
            pady=5,
            padx=5
        )

    def submit(self):
        """create submit button
        """
        sub_btn = tk.Button(
            master=self,
            text="submit",
            command=lambda: self.update_building(),
            font=self.controller.normal_font
        )
        sub_btn.grid(
            row=14,
            column=0,
            rowspan=2,
            columnspan=4,
            sticky="news",
            pady=5,
            padx=5
        )

    def fill_entry(self):
        """fill all entries with self attrs
        """
        self.e_name.insert(tk.END, str(self.building.get_name()))
        self.e_street.insert(tk.END, str(self.building.get_street_name()))
        self.e_number.insert(tk.END, str(self.building.get_number()))

    def set_building(self, building):
        """set building instance

        Args:
            building (Building): building which we want update
        """
        self.building = building

    def update_building(self):
        """func update building and config other frames
        """
        self.set_attr_building()
        self.building.update(self.controller.db)
        self.controller.db.commit_conn()

        # config after update
        # refresh department frames
        self.controller.frames["CreateDepartmentPage"].refresh_building_listbox()
        self.controller.frames["ChangeDepartmentPage"].refresh_building_listbox()
        self.controller.frames["DepartmentPage"].refresh()
        # refresh room frames
        self.controller.frames["CreateRoomPage"].refresh_building_listbox()
        self.controller.frames["ChangeRoomPage"].refresh_building_listbox()
        self.controller.frames["RoomPage"].refresh()
        # refresh self
        self.refresh()
        self.controller.frames["BuildingPage"].restart()

    def set_attr_building(self):
        """change attrs of building
        """
        self.building.set_name(self.e_name.get())
        self.building.set_street_name(self.e_street.get())
        self.building.set_number(self.e_number.get())
