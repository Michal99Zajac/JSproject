import tkinter as tk

from Tables.Dean import Dean

from tk_extension.multilistBox import MultiListBox


class DeanPage(tk.Frame):
    """
    Main Dean Page
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.columnconfigure([x for x in range(7)], minsize=250)
        self.rowconfigure([x for x in range(9)], minsize=100)
        self.controller = controller
        self.main_label()

        self.dean_listbox()
        self.refresh_button()
        self.buttons()

    def main_label(self):
        """create dean main label
        """
        label = tk.Label(
            self,
            text="Dean Page",
            font=self.controller.title_font
        )
        label.grid(row=0, column=6, sticky="news", padx=5, pady=5)

    def buttons(self):
        """create dean buttons
        """
        # Return Home Button
        btn_return = tk.Button(
            self,
            text="Home",
            command=lambda: self.controller.show_frame("StartPage"),
            font=self.controller.normal_font
        )
        btn_return.grid(row=4, column=6, sticky="news", padx=5, pady=5)
        # Create Dean Button
        btn_create = tk.Button(
            self,
            text="Create Dean",
            command=lambda: self.controller.show_frame("CreateDeanPage"),
            font=self.controller.normal_font
        )
        btn_create.grid(row=1, column=6, sticky="news", padx=5, pady=5)
        # Delete Dean Button
        btn_delete = tk.Button(
            self,
            text="Delete Dean",
            command=lambda: self.delete_dean(),
            font=self.controller.normal_font
        )
        btn_delete.grid(row=2, column=6, sticky="news", padx=5, pady=5)
        # Change Dean Button
        btn_update = tk.Button(
            self,
            text="Change Dean",
            command=lambda: self.update_dean(),
            font=self.controller.normal_font
        )
        btn_update.grid(row=3, column=6, sticky="news", padx=5, pady=5)

    def dean_listbox(self):
        """create dean listbox
        """
        data = [
            ('id', 10),
            ('name', 20),
            ('lastname', 20),
            ('second name', 20),
            ('ssn', 20),
            ('email', 20),
            ('place of residence', 40)
        ]

        self.list_deans = MultiListBox(master=self, data=data)
        self.refresh()
        self.list_deans.grid(
            row=0,
            column=0,
            columnspan=6,
            rowspan=9,
            sticky="news",
            padx=5,
            pady=5
        )

    def refresh(self):
        """func refresh dean listbox
        """
        self.list_deans.delete(0, tk.END)
        for i, dean in enumerate(self.controller.deans):
            output = (
                dean.get_id(),
                dean.get_name(),
                dean.get_lastname(),
                dean.get_sec_name(),
                dean.get_ssn(),
                dean.get_email(),
                dean.get_place_of_residence()
            )
            self.list_deans.insert(i, output)

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
        self.controller.show_frame("DeanPage")

    def delete_dean(self):
        """func delete dean from listbox and config other frame
        """
        idx = self.list_deans.index(tk.ACTIVE)
        del_dean = self.controller.deans.pop(idx)

        del_dean.delete(self.controller.db)
        self.update_department(del_dean)
        self.controller.db.commit_conn()

        del del_dean
        # config
        self.controller.frames["CreateDepartmentPage"].refresh_dean_listbox()
        self.controller.frames["ChangeDepartmentPage"].refresh_dean_listbox()
        self.controller.frames["DepartmentPage"].refresh()
        self.restart()

    def update_dean(self):
        """func set dean to update and change page to ChangeDeanPage
        """
        idx = self.list_deans.index(tk.ACTIVE)
        dean = self.controller.deans[idx]

        self.controller.frames["ChangeDeanPage"].set_dean(dean)
        self.controller.frames["ChangeDeanPage"].fill_entry()
        self.controller.show_frame("ChangeDeanPage")


class CreateDeanPage(tk.Frame):
    """
    Page where we can create dean
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
        self.sec_name_entry()
        self.lastname_entry()
        self.ssn_entry()
        self.email_entry()
        self.place_entry()
        self.submit()

    def main_label(self):
        """create dean main label
        """
        label = tk.Label(
            self,
            text="Create Dean",
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
        """func change page to DeanPage
        """
        self.refresh()
        self.controller.show_frame("DeanPage")

    def refresh(self):
        """clear all entries
        """
        self.e_name.delete(0, tk.END)
        self.e_sec_name.delete(0, tk.END)
        self.e_lastname.delete(0, tk.END)
        self.e_ssn.delete(0, tk.END)
        self.e_email.delete(0, tk.END)
        self.e_place.delete(0, tk.END)

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

    def sec_name_entry(self):
        """create entry for second name with label
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
            sticky="news",
            pady=0,
            padx=5
        )

        self.e_sec_name = tk.Entry(
            master=self,
            font=self.controller.entry_font
        )
        self.e_sec_name.grid(
            row=4,
            column=0,
            columnspan=4,
            sticky="news",
            pady=0,
            padx=5
        )

    def lastname_entry(self):
        """create entry for lastname with label
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
            sticky="news",
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
            sticky="news",
            pady=0,
            padx=5
        )

    def ssn_entry(self):
        """create entry for ssn with label
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
            sticky="news",
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
            sticky="news",
            pady=0,
            padx=5
        )

    def email_entry(self):
        """create entry for email with label
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
            sticky="news",
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
            sticky="news",
            pady=0,
            padx=5
        )

    def place_entry(self):
        """create entry for place of residence with label
        """
        l_place = tk.Label(
            master=self,
            text="place of residence",
            font=self.controller.normal_font,
            anchor=tk.W,
            relief=tk.RAISED
        )
        l_place.grid(
            row=11,
            column=0,
            columnspan=4,
            sticky="news",
            pady=0,
            padx=5
        )

        self.e_place = tk.Entry(
            master=self,
            font=self.controller.entry_font
        )
        self.e_place.grid(
            row=12,
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
            command=lambda: self.create_dean(),
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

    def create_dean(self):
        """func create new dean and config other frames
        """
        self.controller.deans.append(Dean(
            name=self.e_name.get(),
            lastname=self.e_lastname.get(),
            sec_name=self.e_sec_name.get(),
            ssn=self.e_ssn.get(),
            email=self.e_email.get(),
            place_of_residence=self.e_place.get()
        ))

        self.controller.deans[-1].insert(self.controller.db)
        self.controller.db.commit_conn()

        self.controller.frames["CreateDepartmentPage"].refresh_dean_listbox()
        self.controller.frames["ChangeDepartmentPage"].refresh_dean_listbox()
        self.controller.frames["DepartmentPage"].refresh()

        self.refresh()
        self.controller.frames["DeanPage"].restart()


class ChangeDeanPage(CreateDeanPage):
    """
    Page where we can update dean
    """
    def __init__(self, parent, controller):
        CreateDeanPage.__init__(self, parent, controller)
        if controller.deans:
            self.dean = controller.deans[0]

    def main_label(self):
        """create update dean main label
        """
        label = tk.Label(
            self,
            text="Change Dean",
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
            command=lambda: self.update_dean(),
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
        self.e_name.insert(tk.END, str(self.dean.get_name()))
        self.e_sec_name.insert(tk.END, str(self.dean.get_sec_name()))
        self.e_lastname.insert(tk.END, str(self.dean.get_lastname()))
        self.e_email.insert(tk.END, str(self.dean.get_email()))
        self.e_ssn.insert(tk.END, str(self.dean.get_ssn()))
        self.e_place.insert(tk.END, str(self.dean.get_place_of_residence()))

    def set_dean(self, dean):
        """set dean instance

        Args:
            dean (Dean): dean which we want update
        """
        self.dean = dean

    def update_dean(self):
        """func update dean and config other frames
        """
        self.set_attr_dean()
        self.dean.update(self.controller.db)
        self.controller.db.commit_conn()

        # config after update
        self.controller.frames["CreateDepartmentPage"].refresh_dean_listbox()
        self.controller.frames["ChangeDepartmentPage"].refresh_dean_listbox()
        self.controller.frames["DepartmentPage"].refresh()
        self.refresh()
        self.controller.frames["DeanPage"].restart()

    def set_attr_dean(self):
        """change attrs of dean
        """
        self.dean.set_name(self.e_name.get())
        self.dean.set_sec_name(self.e_sec_name.get())
        self.dean.set_lastname(self.e_lastname.get())
        self.dean.set_email(self.e_email.get())
        self.dean.set_ssn(self.e_ssn.get())
        self.dean.set_place_of_residence(self.e_place.get())
