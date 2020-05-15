import tkinter as tk
from tkinter import font as tkfont

class FieldOfStudyPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(
            self,
            text="Field Of Study Page",
            font=controller.title_font
        )
        label.pack(side=tk.TOP, fill=tk.X, pady=10)
        
        #Return Home Button
        btn_1 = tk.Button(
            self,
            text="Return to Home Page",
            command=lambda:controller.show_frame("StartPage")
        )
        #Create Field Of Study Button
        btn_2 = tk.Button(
            self,
            text="Create Field Of Study",
            command=lambda:controller.show_frame("CreateFieldOfStudyPage")
        )
        #Delete Field Of Study Button
        btn_3 = tk.Button(
            self,
            text="Delete Field Of Study",
            command=lambda:controller.show_frame("DeleteFieldOfStudyPage")
        )
        #Change Field Of Study Button
        btn_4 = tk.Button(
            self,
            text="Change Field Of Study",
            command=lambda:controller.show_frame("ChangeFieldOfStudyPage")
        )
        #Show All Field Of Study Button
        btn_5 = tk.Button(
            self,
            text="Show Fields Of Study",
            command=lambda:controller.show_frame("ShowFieldsOfStudyPage")
        )
        btn_1.pack()
        btn_2.pack()
        btn_3.pack()
        btn_4.pack()
        btn_5.pack()

class CreateFieldOfStudyPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(
            self,
            text="Create Field Of Study",
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
            command=lambda:controller.show_frame("FieldOfStudyPage")
        )
        btn1.pack()
        btn2.pack()

class DeleteFieldOfStudyPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(
            self,
            text="Delete Field Of Study",
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
            command=lambda:controller.show_frame("FieldOfStudyPage")
        )
        btn1.pack()
        btn2.pack()

class ChangeFieldOfStudyPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(
            self,
            text="Change Field Of Study",
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
            command=lambda:controller.show_frame("FieldOfStudyPage")
        )
        btn1.pack()
        btn2.pack()

class ShowFieldsOfStudyPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(
            self,
            text="Show Fields Of Study",
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
            command=lambda:controller.show_frame("FieldOfStudyPage")
        )
        btn1.pack()
        btn2.pack()