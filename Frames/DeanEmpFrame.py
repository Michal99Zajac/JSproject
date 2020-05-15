import tkinter as tk
from tkinter import font as tkfont

class DeansEmpPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(
            self,
            text="Deans Employee Page",
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
            text="Create Deans Employee",
            command=lambda:controller.show_frame("CreateDeansEmpPage")
        )
        #Delete Teacher Button
        btn_3 = tk.Button(
            self,
            text="Delete Deans Employee",
            command=lambda:controller.show_frame("DeleteDeansEmpPage")
        )
        #Change Teacher Button
        btn_4 = tk.Button(
            self,
            text="Change Deans Employee",
            command=lambda:controller.show_frame("ChangeDeansEmpPage")
        )
        #Show All Teacher Button
        btn_5 = tk.Button(
            self,
            text="Show Deans Employee",
            command=lambda:controller.show_frame("ShowDeansEmpsPage")
        )
        btn_1.pack()
        btn_2.pack()
        btn_3.pack()
        btn_4.pack()
        btn_5.pack()

class CreateDeansEmpPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(
            self,
            text="Create Deans Employee",
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
            command=lambda:controller.show_frame("DeansEmpPage")
        )
        btn1.pack()
        btn2.pack()

class DeleteDeansEmpPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(
            self,
            text="Delete Deans Employee",
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
            command=lambda:controller.show_frame("DeansEmpPage")
        )
        btn1.pack()
        btn2.pack()

class ChangeDeansEmpPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(
            self,
            text="Change Deans Employee",
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
            command=lambda:controller.show_frame("DeansEmpPage")
        )
        btn1.pack()
        btn2.pack()

class ShowDeansEmpsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(
            self,
            text="Show Deans Employees",
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
            command=lambda:controller.show_frame("DeansEmpPage")
        )
        btn1.pack()
        btn2.pack()