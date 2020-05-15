import tkinter as tk
from tkinter import font as tkfont

class TeacherPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(
            self,
            text="Teacher Page",
            font=controller.title_font
        )
        label.pack(side=tk.TOP, fill=tk.X, pady=10)
        
        #Return Home Button
        btn_1 = tk.Button(
            self,
            text="Return to Home Page",
            command=lambda:controller.show_frame("StartPage")
        )
        #Create Teacher Button
        btn_2 = tk.Button(
            self,
            text="Create Teacher",
            command=lambda:controller.show_frame("CreateTeacherPage")
        )
        #Delete Teacher Button
        btn_3 = tk.Button(
            self,
            text="Delete Teacher",
            command=lambda:controller.show_frame("DeleteTeacherPage")
        )
        #Change Teacher Button
        btn_4 = tk.Button(
            self,
            text="Change Teacher",
            command=lambda:controller.show_frame("ChangeTeacherPage")
        )
        #Show All Teacher Button
        btn_5 = tk.Button(
            self,
            text="Show Teachers",
            command=lambda:controller.show_frame("ShowTeachersPage")
        )
        btn_1.pack()
        btn_2.pack()
        btn_3.pack()
        btn_4.pack()
        btn_5.pack()

class CreateTeacherPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(
            self,
            text="Create Teacher",
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
            command=lambda:controller.show_frame("TeacherPage")
        )
        btn1.pack()
        btn2.pack()

class DeleteTeacherPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(
            self,
            text="Delete Teacher",
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
            command=lambda:controller.show_frame("TeacherPage")
        )
        btn1.pack()
        btn2.pack()

class ChangeTeacherPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(
            self,
            text="Change Teacher",
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
            command=lambda:controller.show_frame("TeacherPage")
        )
        btn1.pack()
        btn2.pack()

class ShowTeachersPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(
            self,
            text="Show Teachers",
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
            command=lambda:controller.show_frame("TeacherPage")
        )
        btn1.pack()
        btn2.pack()
