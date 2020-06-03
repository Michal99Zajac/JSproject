import tkinter as tk

from Tables.Room import Room

from tk_extension.multilistBox import MultiListBox


class RoomPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.columnconfigure([x for x in range(7)], minsize=250)
        self.rowconfigure([x for x in range(9)], minsize=100)
        self.controller = controller
        self.main_label()

        self.room_listbox()
        self.refresh_button()
        self.buttons()


    def main_label(self):
        label = tk.Label(
            self,
            text="Room Page",
            font=self.controller.title_font
        )
        label.grid(row=0, column = 6, sticky="news", padx=5, pady=5)

    
    def buttons(self):
        #Return Home Page
        btn_return = tk.Button(
            self,
            text="Home",
            command=lambda: self.controller.show_frame("StartPage"),
            font=self.controller.normal_font,
        )
        btn_return.grid(row=4, column=6, sticky="news", padx=5, pady=5)
        #Create Room Button
        btn_create = tk.Button(
            self,
            text="Create Room",
            command=lambda : self.controller.show_frame("CreateRoomPage"),
            font=self.controller.normal_font,
        )
        btn_create.grid(row=1, column=6, sticky="news", padx=5, pady=5)
        #Delete Room Button
        btn_delete = tk.Button(
            self,
            text="Delete Room",
            command=lambda : self.delete_room(),
            font=self.controller.normal_font,
        )
        btn_delete.grid(row=2, column=6, sticky="news", padx=5, pady=5)
        #Change Room Button
        btn_update = tk.Button(
            self,
            text="Change Room",
            command=lambda : self.update_room(),
            font=self.controller.normal_font,
        )
        btn_update.grid(row=3, column=6, sticky="news", padx=5, pady=5)


    def room_listbox(self):
        data = [
            ('id', 10),
            ('building', 20),
            ('number', 10),
            ('is dean office', 10)
        ]

        self.list_rooms = MultiListBox(master=self, data=data)
        self.refresh()
        self.list_rooms.grid(row=0, column=0, columnspan=6, rowspan=9, sticky="news", padx=5, pady=5)


    def delete_room(self):
        idx = self.list_rooms.index(tk.ACTIVE)
        del_room = self.controller.rooms.pop(idx)

        del_room.delete(self.controller.db)
        self.controller.db.commit_conn()

        del del_room

        self.controller.frames["YearSubjectPage"].refresh()
        self.controller.frames["CreateYearSubjectPage"].refresh_room_listbox()
        self.controller.frames["ExeSubjectPage"].refresh()
        self.controller.frames["CreateExeSubjectPage"].refresh_room_listbox()
        self.controller.frames["LabSubjectPage"].refresh()
        self.controller.frames["CreateLabSubjectPage"].refresh_room_listbox()

        self.restart()


    def update_room(self):
        idx = self.list_rooms.index(tk.ACTIVE)
        room = self.controller.rooms[idx]

        self.controller.frames["ChangeRoomPage"].set_room(room)
        self.controller.frames["ChangeRoomPage"].fill_entry()
        self.controller.show_frame("ChangeRoomPage")


    def restart(self):
        self.refresh()
        self.controller.show_frame("RoomPage")


    def refresh_button(self):
        btn_refresh = tk.Button(
            master=self,
            text="refresh",
            command=lambda : self.restart(),
            font=self.controller.normal_font,
        )
        btn_refresh.grid(row=8, column=6, sticky="news", padx=5, pady=5)


    def refresh(self):
        self.list_rooms.delete(0, tk.END)
        for i, room in enumerate(self.controller.rooms):
            try:
                building = room.get_building().get_name()
            except AttributeError:
                building = "NULL"

            if room.get_is_dean() == 1:
                is_dean = "YES"
            else:
                is_dean = "NO"

            output = (
                room.get_id(),
                building,
                room.get_number(),
                is_dean
            )

            self.list_rooms.insert(i, output)


class CreateRoomPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.columnconfigure([x for x in range(9)], minsize=250)
        self.rowconfigure([x for x in range(18)], minsize=49)
        self.controller = controller

        self.main_label()
        self.return_button()
        self.home_button()

        self.number_entry()
        self.dean_off_listbox()
        self.building_listbox()
        self.submit()


    def main_label(self):
        label = tk.Label(
            self,
            text="Create Room",
            font=self.controller.title_font
        )
        label.grid(row=0, column=0, rowspan=1, columnspan=4, sticky="news", padx=5, pady=5)


    def return_button(self):
        btn_return = tk.Button(
            self,
            text="return",
            command=lambda : self.return_refresh(),
            font=self.controller.normal_font,
        )
        btn_return.grid(row=16, column=0, rowspan=2, columnspan=2, sticky="news", padx=5, pady=5)


    def home_button(self):
        btn_home = tk.Button(
            self,
            text="Home",
            command=lambda : self.home_refresh(),
            font=self.controller.normal_font,
        )
        btn_home.grid(row=16, column=2,rowspan=2, columnspan=2, sticky="news", padx=5, pady=5)


    def return_refresh(self):
        self.refresh()
        self.controller.show_frame("RoomPage")


    def home_refresh(self):
        self.refresh()
        self.controller.show_frame("StartPage")

    
    def refresh(self):
        self.e_number.delete(0, tk.END)

    
    def number_entry(self):
        l_number = tk.Label(master=self, text="number", font=self.controller.normal_font, anchor=tk.W, relief=tk.RAISED)
        l_number.grid(row=1, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)

        self.e_number = tk.Entry(master=self, font=self.controller.entry_font)
        self.e_number.grid(row=2, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)


    def dean_off_listbox(self):
        data = [
            ('is dean office?', 10),
        ]


        self.list_dean_off = MultiListBox(master=self, data=data)
        self.list_dean_off.insert(0, ("YES",))
        self.list_dean_off.insert(1, ("NO",))
        self.list_dean_off.grid(row=0, column=4, rowspan=4, columnspan=3, sticky="nswe", pady=5, padx=5)


    def building_listbox(self):
        l_building = tk.Label(master=self, text="building", font=self.controller.normal_font, relief=tk.RAISED)
        l_building.grid(row=4, column=4, rowspan=1, columnspan=3, sticky="nswe", pady=5, padx=5)

        data = [
            ('name', 10),
        ]

        self.list_building = MultiListBox(master=self, data=data)
        self.list_building.grid(row=5, column=4, rowspan=13, columnspan=3, sticky="nswe", pady=5, padx=5)
        self.refresh_building_listbox()


    def refresh_building_listbox(self):
        self.list_building.delete(0, tk.END)
        for i, building in enumerate(self.controller.buildings):
            output = (
                building.get_name(),
            )
            
            self.list_building.insert(i, output)


    def submit(self):
        sub_btn = tk.Button(
            master=self,
            text="submit",
            command=lambda : self.create_room(),
            font=self.controller.normal_font,
        )
        sub_btn.grid(row=14, column=0, rowspan=2, columnspan=4, sticky="nswe", pady=5, padx=5)


    def create_room(self):
        idx = self.list_building.index(tk.ACTIVE)
        temp_building = self.controller.buildings[idx]

        temp_is_dean = None
        if self.list_dean_off.index(tk.ACTIVE) == 0:
            temp_is_dean = 1
        else:
            temp_is_dean = 0

        self.controller.rooms.append(Room(
            building=temp_building,
            number=self.e_number.get(),
            is_dean=temp_is_dean
        ))

        #config after create
        self.controller.frames["YearSubjectPage"].refresh()
        self.controller.frames["CreateYearSubjectPage"].refresh_room_listbox()
        self.controller.frames["ExeSubjectPage"].refresh()
        self.controller.frames["CreateExeSubjectPage"].refresh_room_listbox()
        self.controller.frames["LabSubjectPage"].refresh()
        self.controller.frames["CreateLabSubjectPage"].refresh_room_listbox()

        self.controller.rooms[-1].insert(self.controller.db)
        self.controller.db.commit_conn()
        self.refresh()
        self.controller.frames["RoomPage"].restart()



class ChangeRoomPage(CreateRoomPage):
    def __init__(self, parent, controller):
        CreateRoomPage.__init__(self, parent, controller)
        if controller.rooms:
            self.room = controller.rooms[0]


    def main_label(self):
        label = tk.Label(
            self,
            text="Change Room",
            font=self.controller.title_font
        )
        label.grid(row=0, column=0, rowspan=1, columnspan=4, sticky="news", padx=5, pady=5)


    def submit(self):
        sub_btn = tk.Button(
            master=self,
            text="submit",
            command=lambda : self.update_room(),
            font=self.controller.normal_font,
        )
        sub_btn.grid(row=14, column=0, rowspan=2, columnspan=4, sticky="news", padx=5, pady=5)


    def fill_entry(self):
        self.e_number.insert(tk.END, str(self.room.get_number()))


    def set_room(self, room):
        self.room = room


    def update_room(self):
        self.set_attr_room()
        self.room.update(self.controller.db)
        self.controller.db.commit_conn()

        #config after update
        self.controller.frames["YearSubjectPage"].refresh()
        self.controller.frames["CreateYearSubjectPage"].refresh_room_listbox()
        self.controller.frames["ExeSubjectPage"].refresh()
        self.controller.frames["CreateExeSubjectPage"].refresh_room_listbox()
        self.controller.frames["LabSubjectPage"].refresh()
        self.controller.frames["CreateLabSubjectPage"].refresh_room_listbox()
        
        self.refresh()
        self.controller.frames["RoomPage"].restart()


    def set_attr_room(self):
        idx = self.list_building.index(tk.ACTIVE)
        temp_building = self.controller.buildings[idx]
        self.room.set_building(temp_building)

        if self.list_dean_off.get(tk.ACTIVE) == "YES":
            temp_is_dean = 1
        else:
            temp_is_dean = 0

        self.room.set_is_dean(temp_is_dean)
        self.room.set_number(self.e_number.get())
