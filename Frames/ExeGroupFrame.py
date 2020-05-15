import tkinter as tk
from tkinter import font as tkfont

class ExeGroupPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(
            self,
            text="Exercise Group Page",
            font=controller.title_font
        )
        label.pack(side=tk.TOP, fill=tk.X, pady=10)

        #Return Home Button
        btn_1 = tk.Button(
            self,
            text="Return to Home Page",
            command=lambda:controller.show_frame("StartPage")
        )
        #Create Exercise Group Button
        btn_2 = tk.Button(
            self,
            text="Create Exercise Group",
            command=lambda:controller.show_frame("CreateExeGroupPage")
        )
        #Delete Exercise Group Button
        btn_3 = tk.Button(
            self,
            text="Delete Exercise Group",
            command=lambda:controller.show_frame("DeleteExeGroupPage")
        )
        #Change Exercise Group Button
        btn_4 = tk.Button(
            self,
            text="Change Exercise Group",
            command=lambda:controller.show_frame("ChangeExeGroupPage")
        )
        #Show All Exercise Group Button
        btn_5 = tk.Button(
            self,
            text="Show Exercise Groups",
            command=lambda:controller.show_frame("ShowExeGroupsPage")
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

class CreateExeGroupPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(
            self,
            text="Create Exercise Group",
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
            command=lambda:controller.show_frame("ExeGroupPage")
        )
        btn1.pack()
        btn2.pack()

class DeleteExeGroupPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(
            self,
            text="Delete Exercise Group",
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
            command=lambda:controller.show_frame("ExeGroupPage")
        )
        btn1.pack()
        btn2.pack()

class ShowExeGroupsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(
            self,
            text="Show Exercise Groups",
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
            command=lambda:controller.show_frame("ExeGroupPage")
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
            command=lambda:controller.show_frame("ExeGroupPage")
        )
        btn1.pack()
        btn2.pack()

class ChangeExeGroupPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(
            self,
            text="Change Exercise Group",
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
            command=lambda:controller.show_frame("ExeGroupPage")
        )
        btn1.pack()
        btn2.pack()