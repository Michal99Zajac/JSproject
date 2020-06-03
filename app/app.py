import tkinter as tk
from tkinter import font as tkfont

from Frames import StudentFrame
from Frames import BuildingFrame
from Frames import DeanEmpFrame
from Frames import DeanFrame
from Frames import DepartmentFrame
from Frames import ExeGroupFrame
from Frames import FieldOfStudyFrame
from Frames import LabGroupFrame
from Frames import RoomFrame
from Frames import SubjectFrame
from Frames import TeacherFrame
from Frames import YearGroupFrame

from Tables.TableDatabase import TableDatabase

class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.resizable(False, False)
        self.db = TableDatabase("data.db")

        #table setting
        self.buildings = self.db.fetch_buildings()
        self.deans = self.db.fetch_deans()
        self.departments = self.db.fetch_departments(self.buildings, self.deans)
        self.deans_emps = self.db.fetch_deans_emps(self.departments)
        self.fields = self.db.fetch_fields_of_study(self.departments, self.deans_emps)
        self.students = self.db.fetch_students(self.fields)
        self.exe_groups = self.db.fetch_exe_groups(self.students, self.fields)
        self.lab_groups = self.db.fetch_lab_groups(self.students, self.fields)
        self.year_groups = self.db.fetch_year_groups(self.students, self.fields)
        self.rooms = self.db.fetch_rooms(self.buildings)
        self.teachers = self.db.fetch_teachers(self.departments)
        self.subjects = self.db.fetch_subjects(
            self.teachers,
            self.lab_groups,
            self.exe_groups,
            self.year_groups,
            self.rooms,
            self.fields
            )

        self.geometry("1750x900")

        self.title_font = tkfont.Font(family="Helvetica", size=20, weight="bold", slant="italic")
        self.normal_font = tkfont.Font(family="Helvetica", size=15, weight=tkfont.BOLD)
        self.entry_font = tkfont.Font(family="Helvetica", size=20)

        mainframe = tk.Frame(self)
        mainframe.grid()
        mainframe.grid_rowconfigure(0, weight=1)
        mainframe.grid_columnconfigure(0, weight=1)

        self.frames = {}
        pages = {
            StartPage,
            #Student pages
            StudentFrame.StudentPage,
            StudentFrame.CreateStudentPage,
            StudentFrame.ChangeStudentPage,
            #Teacher pages
            TeacherFrame.TeacherPage,
            TeacherFrame.ChangeTeacherPage,
            TeacherFrame.CreateTeacherPage,
            #Building pages
            BuildingFrame.BuildingPage,
            BuildingFrame.ChangeBuildingPage,
            BuildingFrame.CreateBuildingPage,
            #Dean Employee pages
            DeanEmpFrame.DeansEmpPage,
            DeanEmpFrame.ChangeDeansEmpPage,
            DeanEmpFrame.CreateDeansEmpPage,
            #Dean pages
            DeanFrame.DeanPage,
            DeanFrame.ChangeDeanPage,
            DeanFrame.CreateDeanPage,
            #Department pages
            DepartmentFrame.DepartmentPage,
            DepartmentFrame.ChangeDepartmentPage,
            DepartmentFrame.CreateDepartmentPage,
            #Exercise pages
            ExeGroupFrame.ExeGroupPage,
            ExeGroupFrame.CreateExeGroupPage,
            ExeGroupFrame.ExeAddStudentPage,
            ExeGroupFrame.ExeStudentPage,
            #Field of Study pages
            FieldOfStudyFrame.FieldOfStudyPage,
            FieldOfStudyFrame.ChangeFieldOfStudyPage,
            FieldOfStudyFrame.CreateFieldOfStudyPage,
            #Laboratory pages
            LabGroupFrame.LabGroupPage,
            LabGroupFrame.CreateLabGroupPage,
            LabGroupFrame.LabAddStudentPage,
            LabGroupFrame.LabStudentPage,
            #Room pages
            RoomFrame.RoomPage,
            RoomFrame.ChangeRoomPage,
            RoomFrame.CreateRoomPage,
            #Subject pages
            SubjectFrame.SubjectPage,
            SubjectFrame.YearSubjectPage,
            SubjectFrame.ExeSubjectPage,
            SubjectFrame.LabSubjectPage,
            SubjectFrame.CreateYearSubjectPage,
            SubjectFrame.CreateExeSubjectPage,
            SubjectFrame.CreateLabSubjectPage,
            #Year pages
            YearGroupFrame.YearGroupPage,
            YearGroupFrame.CreateYearGroupPage,
            YearGroupFrame.YearAddStudentPage,
            YearGroupFrame.YearStudentPage,
        }

        for F in pages:
            page_name = F.__name__
            frame = F(parent=mainframe, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.columnconfigure([x for x in range(2)], minsize=875)
        self.rowconfigure([x for x in range(7)], minsize=128)

        font = tkfont.Font(family="Helvetica", size=20, weight=tkfont.BOLD)
        title_font = tkfont.Font(family="Helvetica", size=36, weight=tkfont.BOLD)

        label = tk.Label(
            self, text="MENU",
            font=title_font,
        )
        label.grid(row=0, column=0, columnspan=2, sticky="nswe", padx=5, pady=5)

        #btns = []
        #Teacher Page Button
        btn_teacher = tk.Button(
                self,
                text="Teacher Page",
                command=lambda: controller.show_frame("TeacherPage"),
                height=2,
                font=font
            )
        btn_teacher.grid(row=2, column=1, sticky="nswe", padx=5, pady=5)

        #Building Page Button
        btn_building = tk.Button(
                self,
                text="Building Page",
                command=lambda: controller.show_frame("BuildingPage"),
                height=2,
                font=font
            )
        btn_building.grid(row=5, column=1, sticky="nswe", padx=5, pady=5)

        #Deans Employee Page Button
        btn_deans_emp = tk.Button(
                self,
                text="Deans Employee Page",
                command=lambda: controller.show_frame("DeansEmpPage"),
                height=2,
                font=font
            )
        btn_deans_emp.grid(row=4, column=1, sticky="nswe", padx=5, pady=5)

        #Dean Page Button
        btn_dean = tk.Button(
                self,
                text="Dean Page",
                command=lambda: controller.show_frame("DeanPage"),
                height=2,
                font=font
            )
        btn_dean.grid(row=3, column=1, sticky="nswe", padx=5, pady=5)

        #Department Page Button
        btn_dept = tk.Button(
                self,
                text="Department Page",
                command=lambda: controller.show_frame("DepartmentPage"),
                height=2,
                font=font
            )
        btn_dept.grid(row=1, column=0, sticky="nswe", padx=5, pady=5)

        #Exercise Group Page Button
        btn_exe = tk.Button(
                self,
                text="Exercise Group Page",
                command=lambda: controller.show_frame("ExeGroupPage"),
                height=2,
                font=font
            )
        btn_exe.grid(row=5, column=0, sticky="nswe", padx=5, pady=5)

        #Field Of Study Page
        btn_field = tk.Button(
                self,
                text="Field of Study Page",
                command=lambda: controller.show_frame("FieldOfStudyPage"),
                height=2,
                font=font
            )
        btn_field.grid(row=2, column=0, sticky="nswe", padx=5, pady=5)

        #Laboratory Group Page Button
        btn_lab = tk.Button(
                self,
                text="Laboratory Group Page",
                command=lambda: controller.show_frame("LabGroupPage"),
                height=2,
                font=font
            )
        btn_lab.grid(row=6, column=0, sticky="nswe", padx=5, pady=5)

        #Room Page Button
        btn_room = tk.Button(
                self,
                text="Room Page",
                command=lambda: controller.show_frame("RoomPage"),
                height=2,
                font=font
            )
        btn_room.grid(row=6, column=1, sticky="nswe", padx=5, pady=5)

        #Subject Page Button
        btn_subject = tk.Button(
                self,
                text="Subject Page",
                command=lambda: controller.show_frame("SubjectPage"),
                height=2,
                font=font
            )
        btn_subject.grid(row=3, column=0, sticky="nswe", padx=5, pady=5)

        #Year Group Page Button
        btn_year = tk.Button(
                self,
                text="Year Group Page",
                command=lambda: controller.show_frame("YearGroupPage"),
                height=2,
                font=font
            )
        btn_year.grid(row=4, column=0, sticky="nswe", padx=5, pady=5)

        #Student Page Button
        btn_student = tk.Button(
                self,
                text="Student Page",
                command=lambda: controller.show_frame("StudentPage"),
                height=2,
                font=font
            )
        btn_student.grid(row=1, column=1, sticky="nswe", padx=5, pady=5)
