import tkinter as tk
from tkinter import font as tkfont

class LabGroupPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(
            self,
            text="Laboratory Group Page",
            font=controller.title_font
        )
        label.pack(side=tk.TOP, fill=tk.X, pady=10)

        #Return Home Button
        btn_1 = tk.Button(
            self,
            text="Return to Home Page",
            command=lambda:controller.show_frame("StartPage")
        )
        #Create Laboratory Group Button
        btn_2 = tk.Button(
            self,
            text="Create Laboratory Group",
            command=lambda:controller.show_frame("CreateLabGroupPage")
        )
        #Delete Laboratory Group Button
        btn_3 = tk.Button(
            self,
            text="Delete Laboratory Group",
            command=lambda:controller.show_frame("DeleteLabGroupPage")
        )
        #Change Laboratory Group Button
        btn_4 = tk.Button(
            self,
            text="Change Laboratory Group",
            command=lambda:controller.show_frame("ChangeLabGroupPage")
        )
        #Show All Laboratory Group Button
        btn_5 = tk.Button(
            self,
            text="Show Laboratory Groups",
            command=lambda:controller.show_frame("ShowLabGroupsPage")
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

class CreateLabGroupPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(
            self,
            text="Create Laboratory Group",
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
            command=lambda:controller.show_frame("LabGroupPage")
        )
        btn1.pack()
        btn2.pack()

class DeleteLabGroupPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(
            self,
            text="Delete Laboratory Group",
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
            command=lambda:controller.show_frame("LabGroupPage")
        )
        btn1.pack()
        btn2.pack()

class ShowLabGroupsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(
            self,
            text="Show Laboratory Groups",
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
            command=lambda:controller.show_frame("LabGroupPage")
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
            command=lambda:controller.show_frame("LabGroupPage")
        )
        btn1.pack()
        btn2.pack()

class ChangeLabGroupPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(
            self,
            text="Change Laboratory Group",
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
            command=lambda:controller.show_frame("LabGroupPage")
        )
        btn1.pack()
        btn2.pack()