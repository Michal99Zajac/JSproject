import tkinter as tk

from Tables.Room import Room

from tk_extension.multilistBox import MultiListBox


class RoomPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
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
        label.pack(side=tk.TOP, fill=tk.X, pady=10)

    
    def buttons(self):
        #Return Home Page
        btn_return = tk.Button(
            self,
            text="Return to Home Page",
            command=lambda: self.controller.show_frame("StartPage")
        )
        btn_return.pack()
        #Create Room Button
        btn_create = tk.Button(
            self,
            text="Create Room",
            command=lambda : self.controller.show_frame("CreateRoomPage")
        )
        btn_create.pack()
        #Delete Room Button
        btn_delete = tk.Button(
            self,
            text="Delete Room",
            command=lambda : self.delete_room()
        )
        btn_delete.pack()
        #Change Room Button
        btn_update = tk.Button(
            self,
            text="Change Room",
            command=lambda : self.update_room()
        )
        btn_update.pack()


    def room_listbox(self):
        f_room = tk.Frame(master=self)
        f_room.pack()
        l_room = tk.Label(master=f_room, text="select room")
        l_room.pack()

        data = [
            ('id', 10),
            ('building', 20),
            ('number', 10),
            ('is dean office', 10)
        ]

        self.list_rooms = MultiListBox(master=f_room, data=data)
        self.refresh()
        self.list_rooms.pack()


    def delete_room(self):
        idx = self.list_rooms.index(tk.ACTIVE)
        del_room = self.controller.rooms.pop(idx)

        del_room.delete(self.controller.db)
        self.controller.db.commit_conn()

        del del_room

        #update 'create subject.listbox()'
        #update 'update subject.listbox()'
        #subject.refresh()
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
        f_refresh = tk.Frame(master=self)
        f_refresh.pack()
        btn_refresh = tk.Button(
            master=f_refresh,
            text="refresh",
            command=lambda : self.restart()
        )
        btn_refresh.pack()


    def refresh(self):
        self.list_rooms.delete(0, tk.END)
        for i, room in enumerate(self.controller.rooms):
            try:
                building = room.get_building().get_name()
            except AttributeError:
                building = "NULL"

            if room.get_is_dean():
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
        label.pack(side=tk.TOP, fill=tk.X, pady=10)


    def return_button(self):
        btn_return = tk.Button(
            self,
            text="return",
            command=lambda : self.return_refresh()
        )
        btn_return.pack()


    def home_button(self):
        btn_home = tk.Button(
            self,
            text="Return to Home Page",
            command=lambda : self.home_refresh()
        )
        btn_home.pack()


    def return_refresh(self):
        self.refresh()
        self.controller.show_frame("RoomPage")


    def home_refresh(self):
        self.refresh()
        self.controller.show_frame("StartPage")

    
    def refresh(self):
        self.e_number.delete(0, tk.END)

    
    def number_entry(self):
        f_number = tk.Frame(master=self)
        f_number.pack()

        l_number = tk.Label(master=f_number, text="number")
        l_number.pack()

        self.e_number = tk.Entry(master=f_number)
        self.e_number.pack()


    def dean_off_listbox(self):
        f_dean_off = tk.Frame(master=self)
        f_dean_off.pack()

        l_dean_off = tk.Label(master=f_dean_off, text="is dean office?")
        l_dean_off.pack()

        self.list_dean_off = tk.Listbox(master=f_dean_off)
        self.list_dean_off.insert(0, "YES")
        self.list_dean_off.insert(1, "NO")
        self.list_dean_off.pack()


    def building_listbox(self):
        f_building = tk.Frame(master=self)
        f_building.pack()

        l_building = tk.Label(master=f_building, text="building")
        l_building.pack()

        self.list_building = tk.Listbox(master=f_building)
        for i, building in enumerate(self.controller.buildings):
            self.list_building.insert(i, building.get_name())
        self.list_building.pack()


    def refresh_building_listbox(self):
        self.list_building.delete(0, tk.END)
        for i, building in enumerate(self.controller.buildings):
            self.list_building.insert(i, building.get_name())


    def submit(self):
        f_submit = tk.Frame(master=self)
        f_submit.pack()

        sub_btn = tk.Button(
            master=f_submit,
            text="submit",
            command=lambda : self.create_room()
        )
        sub_btn.pack()


    def create_room(self):
        temp_building = None
        for building in self.controller.buildings:
            if self.list_building.get(tk.ACTIVE) == building.get_name():
                temp_building = building
                break

        temp_is_dean = None
        if self.list_dean_off.get(tk.ACTIVE) == "YES":
            temp_is_dean = 1
        else:
            temp_is_dean = 0

        self.controller.rooms.append(Room(
            building=temp_building,
            number=self.e_number.get(),
            is_dean=temp_is_dean
        ))

        #update 'subject create room_listbox()'
        #update 'subject update room_listbox()'
        #subject.refresh()
        self.controller.rooms[-1].insert(self.controller.db)
        self.controller.db.commit_conn()
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
        label.pack(side=tk.TOP, fill=tk.X, pady=10)


    def submit(self):
        f_submit = tk.Frame(master=self)
        f_submit.pack()

        sub_btn = tk.Button(
            master=f_submit,
            text="submit",
            command=lambda : self.update_room()
        )
        sub_btn.pack()


    def fill_entry(self):
        self.e_number.insert(tk.END, str(self.room.get_number()))


    def set_room(self, room):
        self.room = room


    def update_room(self):
        self.set_attr_room()
        self.room.update(self.controller.db)
        self.controller.db.commit_conn()

        #config after update
        self.refresh()
        #update 'subject create room_listbox()'
        #update 'subject update room_listbox()'
        #subject.refresh()
        self.controller.frames["RoomPage"].restart()


    def set_attr_room(self):
        for building in self.controller.buildings:
            if self.list_building.get(tk.ACTIVE) == building.get_name():
                self.room.set_building(building)
                break

        if self.list_dean_off.get(tk.ACTIVE) == "YES":
            temp_is_dean = 1
        else:
            temp_is_dean = 0

        self.room.set_is_dean(temp_is_dean)
        self.room.set_number(self.e_number.get())
