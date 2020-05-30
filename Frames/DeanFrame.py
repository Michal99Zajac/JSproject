import tkinter as tk

from Tables.Dean import Dean

from tk_extension.multilistBox import MultiListBox

class DeanPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.main_label()

        self.dean_listbox()
        self.refresh_button()
        self.buttons()

    
    def main_label(self):
        label = tk.Label(
            self,
            text="Dean Page",
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
        #Create Dean Button
        btn_create = tk.Button(
            self,
            text="Create Dean",
            command=lambda : self.controller.show_frame("CreateDeanPage")
        )
        btn_create.pack()
        #Delete Dean Button
        btn_delete = tk.Button(
            self,
            text="Delete Dean",
            command=lambda : self.delete_dean()
        )
        btn_delete.pack()
        #Change Dean Button
        btn_update = tk.Button(
            self,
            text="Change Dean",
            command=lambda : self.update_dean()
        )
        btn_update.pack()

    
    def dean_listbox(self):
        f_dean = tk.Frame(master=self)
        f_dean.pack()
        l_dean = tk.Label(master=f_dean, text="select dean")
        l_dean.pack()

        data = [
            ('id', 10),
            ('name', 20),
            ('lastname',20),
            ('second name',20),
            ('ssn',20),
            ('email', 20),
            ('place of residence', 40)
        ]

        self.list_deans = MultiListBox(master=f_dean, data=data)
        self.refresh()
        self.list_deans.pack()


    def refresh(self):
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
        self.controller.show_frame("DeanPage")

    
    def delete_dean(self):
        idx = self.list_deans.index(tk.ACTIVE)
        del_dean = self.controller.deans.pop(idx)

        del_dean.delete(self.controller.db)
        self.update_department(del_dean)
        self.controller.db.commit_conn()

        del del_dean
        self.controller.frames["CreateDepartmentPage"].refresh_dean_listbox()
        self.controller.frames["ChangeDepartmentPage"].refresh_dean_listbox()
        self.controller.frames["DepartmentPage"].refresh()
        self.restart()


    def update_department(self, dean):
        for dept in self.controller.departments:
            if dept.get_dean() == dean:
                dept.set_dean(None)
                dept.update(self.controller.db)
                self.controller.db.commit_conn()
                break


    def update_dean(self):
        idx = self.list_deans.index(tk.ACTIVE)
        dean = self.controller.deans[idx]

        self.controller.frames["ChangeDeanPage"].set_dean(dean)
        self.controller.frames["ChangeDeanPage"].fill_entry()
        self.controller.show_frame("ChangeDeanPage")


class CreateDeanPage(tk.Frame):
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
        self.place_entry()
        self.submit()


    def main_label(self):
        label = tk.Label(
            self,
            text="Create Dean",
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
        self.controller.show_frame("DeanPage")


    def refresh(self):
        self.e_name.delete(0, tk.END)
        self.e_sec_name.delete(0, tk.END)
        self.e_lastname.delete(0, tk.END)
        self.e_ssn.delete(0, tk.END)
        self.e_email.delete(0, tk.END)
        self.e_place.delete(0, tk.END)


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

    def place_entry(self):
        f_place = tk.Frame(master=self)
        f_place.pack()

        l_place = tk.Label(master=f_place, text="place of residence")
        l_place.pack()

        self.e_place = tk.Entry(master=f_place)
        self.e_place.pack()


    def submit(self):
        sub_btn = tk.Button(
            master=self,
            text="submit",
            command=lambda : self.create_dean()
        )
        sub_btn.pack()


    def create_dean(self):
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
    def __init__(self, parent, controller):
        CreateDeanPage.__init__(self, parent, controller)
        if controller.deans:
            self.dean = controller.deans[0]


    def main_label(self):
        label = tk.Label(
            self,
            text="Change Dean",
            font=self.controller.title_font
        )
        label.pack(side=tk.TOP, fill=tk.X, pady=10)


    def submit(self):
        f_submit = tk.Frame(master=self)
        f_submit.pack()

        sub_btn = tk.Button(
            master=f_submit,
            text="submit",
            command=lambda : self.update_dean()
        )
        sub_btn.pack()


    def fill_entry(self):
        self.e_name.insert(tk.END, str(self.dean.get_name()))
        self.e_sec_name.insert(tk.END, str(self.dean.get_sec_name()))
        self.e_lastname.insert(tk.END, str(self.dean.get_lastname()))
        self.e_email.insert(tk.END, str(self.dean.get_email()))
        self.e_ssn.insert(tk.END, str(self.dean.get_ssn()))
        self.e_place.insert(tk.END, str(self.dean.get_place_of_residence()))


    def set_dean(self, dean):
        self.dean = dean


    def update_dean(self):
        self.set_attr_dean()
        self.dean.update(self.controller.db)
        self.controller.db.commit_conn()

        #config after update
        self.refresh()
        self.controller.frames["CreateDepartmentPage"].refresh_dean_listbox()
        self.controller.frames["ChangeDepartmentPage"].refresh_dean_listbox()
        self.controller.frames["DepartmentPage"].refresh()
        
        self.refresh()
        self.controller.frames["DeanPage"].restart()


    def set_attr_dean(self):
        self.dean.set_name(self.e_name.get())
        self.dean.set_sec_name(self.e_sec_name.get())
        self.dean.set_lastname(self.e_lastname.get())
        self.dean.set_email(self.e_email.get())
        self.dean.set_ssn(self.e_ssn.get())
        self.dean.set_place_of_residence(self.e_place.get())