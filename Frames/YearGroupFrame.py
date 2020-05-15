import tkinter as tk
from tkinter import font as tkfont

class YearGroupPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(
            self,
            text="Year Group Page",
            font=controller.title_font
        )
        label.pack(side=tk.TOP, fill=tk.X, pady=10)

        #Return Home Button
        btn_1 = tk.Button(
            self,
            text="Return to Home Page",
            command=lambda:controller.show_frame("StartPage")
        )
        #Create Year Group Button
        btn_2 = tk.Button(
            self,
            text="Create Year Group",
            command=lambda:controller.show_frame("CreateYearGroupPage")
        )
        #Delete Year Group Button
        btn_3 = tk.Button(
            self,
            text="Delete Year Group",
            command=lambda:controller.show_frame("DeleteYearGroupPage")
        )
        #Change Year Group Button
        btn_4 = tk.Button(
            self,
            text="Change Year Group",
            command=lambda:controller.show_frame("ChangeYearGroupPage")
        )
        #Show All Year Group Button
        btn_5 = tk.Button(
            self,
            text="Show Year Groups",
            command=lambda:controller.show_frame("ShowYearGroupsPage")
        )
        #Add Student Button
        btn_6 = tk.Button(
            self,
            text="Add Student",
            command=lambda:controller.show_frame("AddStudentPage")
        )
        btn_1.pack()
        btn_2.pack()
        btn_3.pack()
        btn_4.pack()
        btn_5.pack()
        btn_6.pack()

class CreateYearGroupPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(
            self,
            text="Create Year Group",
            font=controller.title_font
        )
        label.pack(side=tk.TOP, fill=tk.X, pady=10)
        btn1 = tk.Button(
            self,
            text="Return to Home Page",
            command=lambda:controller.show_frame("StartPage")
        )
        btn2 = tk.Button(
            self,
            text="return",
            command=lambda:controller.show_frame("YearGroupPage")
        )
        btn1.pack()
        btn2.pack()

class DeleteYearGroupPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(
            self,
            text="Delete Year Group",
            font=controller.title_font
        )
        label.pack(side=tk.TOP, fill=tk.X, pady=10)
        btn1 = tk.Button(
            self,
            text="Return to Home Page",
            command=lambda:controller.show_frame("StartPage")
        )
        btn2 = tk.Button(
            self,
            text="return",
            command=lambda:controller.show_frame("YearGroupPage")
        )
        btn1.pack()
        btn2.pack()

class ShowYearGroupsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(
            self,
            text="Show Year Groups",
            font=controller.title_font
        )
        label.pack(side=tk.TOP, fill=tk.X, pady=10)
        btn1 = tk.Button(
            self,
            text="Return to Home Page",
            command=lambda:controller.show_frame("StartPage")
        )
        btn2 = tk.Button(
            self,
            text="return",
            command=lambda:controller.show_frame("YearGroupPage")
        )
        btn1.pack()
        btn2.pack()

class AddStudentPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(
            self,
            text="Add Student",
            font=controller.title_font
        )
        label.pack(side=tk.TOP, fill=tk.X, pady=10)
        btn1 = tk.Button(
            self,
            text="Return to Home Page",
            command=lambda:controller.show_frame("StartPage")
        )
        btn2 = tk.Button(
            self,
            text="return",
            command=lambda:controller.show_frame("YearGroupPage")
        )
        btn1.pack()
        btn2.pack()

class ChangeYearGroupPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(
            self,
            text="Change Year Group",
            font=controller.title_font
        )
        label.pack(side=tk.TOP, fill=tk.X, pady=10)
        btn1 = tk.Button(
            self,
            text="Return to Home Page",
            command=lambda:controller.show_frame("StartPage")
        )
        btn2 = tk.Button(
            self,
            text="return",
            command=lambda:controller.show_frame("YearGroupPage")
        )
        btn1.pack()
        btn2.pack()