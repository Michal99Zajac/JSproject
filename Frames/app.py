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

        #table setting
        self.db = TableDatabase("databases/data.db")
        self.buildings = self.db.fetch_buildings()
        self.deans = self.db.fetch_deans()
        self.departments = self.db.fetch_departments(self.buildings, self.deans)
        self.deans_emps = self.db.fetch_deans_emps(self.departments)
        self.fields = self.db.fetch_fields_of_study(self.departments, self.deans)
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

        self.geometry("1600x900")

        self.title_font = tkfont.Font(family="Helvetica", size=20, weight="bold", slant="italic")

        mainframe = tk.Frame(self)
        mainframe.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
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
            BuildingFrame.DeleteBuildingPage,
            BuildingFrame.ShowBuildingsPage,
            #Dean Employee pages
            DeanEmpFrame.DeansEmpPage,
            DeanEmpFrame.ChangeDeansEmpPage,
            DeanEmpFrame.CreateDeansEmpPage,
            DeanEmpFrame.DeleteDeansEmpPage,
            DeanEmpFrame.ShowDeansEmpsPage,
            #Dean pages
            DeanFrame.DeanPage,
            DeanFrame.ChangeDeanPage,
            DeanFrame.CreateDeanPage,
            #Department pages
            DepartmentFrame.DepartmentPage,
            DepartmentFrame.ChangeDepartmentPage,
            DepartmentFrame.CreateDepartmentPage,
            DepartmentFrame.DeleteDepartmentPage,
            DepartmentFrame.ShowDepartmentsPage,
            #Exercise pages
            ExeGroupFrame.ExeGroupPage,
            ExeGroupFrame.AddStudentPage,
            ExeGroupFrame.ChangeExeGroupPage,
            ExeGroupFrame.CreateExeGroupPage,
            ExeGroupFrame.DeleteExeGroupPage,
            ExeGroupFrame.ShowExeGroupsPage,
            #Field of Study pages
            FieldOfStudyFrame.FieldOfStudyPage,
            FieldOfStudyFrame.ChangeFieldOfStudyPage,
            FieldOfStudyFrame.CreateFieldOfStudyPage,
            FieldOfStudyFrame.DeleteFieldOfStudyPage,
            FieldOfStudyFrame.ShowFieldsOfStudyPage,
            #Laboratory pages
            LabGroupFrame.LabGroupPage,
            LabGroupFrame.AddStudentPage,
            LabGroupFrame.ChangeLabGroupPage,
            LabGroupFrame.CreateLabGroupPage,
            LabGroupFrame.DeleteLabGroupPage,
            LabGroupFrame.ShowLabGroupsPage,
            #Room pages
            RoomFrame.RoomPage,
            RoomFrame.ChangeRoomPage,
            RoomFrame.CreateRoomPage,
            RoomFrame.DeleteRoomPage,
            RoomFrame.ShowRoomsPage,
            #Subject pages
            SubjectFrame.SubjectPage,
            SubjectFrame.ChangeSubjectPage,
            SubjectFrame.CreateSubjectPage,
            SubjectFrame.DeleteSubjectPage,
            SubjectFrame.ShowSubjectsPage,
            #Year pages
            YearGroupFrame.YearGroupPage,
            YearGroupFrame.AddStudentPage,
            YearGroupFrame.ChangeYearGroupPage,
            YearGroupFrame.CreateYearGroupPage,
            YearGroupFrame.DeleteYearGroupPage,
            YearGroupFrame.ShowYearGroupsPage,
        }

        for F in pages:
            page_name = F.__name__
            frame = F(parent=mainframe, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        #zrobienie refrash
        frame = self.frames[page_name]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(
            self, text="START",
            font=controller.title_font,
        )
        label.pack(side="top", fill=tk.X, pady=10)

        btns = []
        #Teacher Page Button
        btn_1 = tk.Button(
                self,
                text="Teacher Page",
                command=lambda: controller.show_frame("TeacherPage"),
                height=2,
            )
        btns.append(btn_1)

        #Building Page Button
        btn_2 = tk.Button(
                self,
                text="Building Page",
                command=lambda: controller.show_frame("BuildingPage"),
                height=2,
            )
        btns.append(btn_2)

        #Deans Employee Page Button
        btn_3 = tk.Button(
                self,
                text="Deans Employee Page",
                command=lambda: controller.show_frame("DeansEmpPage"),
                height=2,
            )
        btns.append(btn_3)

        #Dean Page Button
        btn_4 = tk.Button(
                self,
                text="Dean Page",
                command=lambda: controller.show_frame("DeanPage"),
                height=2,
            )
        btns.append(btn_4)

        #Department Page Button
        btn_5 = tk.Button(
                self,
                text="Department Page",
                command=lambda: controller.show_frame("DepartmentPage"),
                height=2,
            )
        btns.append(btn_5)

        #Exercise Group Page Button
        btn_6 = tk.Button(
                self,
                text="Exercise Group Page",
                command=lambda: controller.show_frame("ExeGroupPage"),
                height=2,
            )
        btns.append(btn_6)

        #Field Of Study Page
        btn_7 = tk.Button(
                self,
                text="Field of Study Page",
                command=lambda: controller.show_frame("FieldOfStudyPage"),
                height=2,
            )
        btns.append(btn_7)

        #Laboratory Group Page Button
        btn_8 = tk.Button(
                self,
                text="Laboratory Group Page",
                command=lambda: controller.show_frame("LabGroupPage"),
                height=2,
            )
        btns.append(btn_8)

        #Room Page Button
        btn_9 = tk.Button(
                self,
                text="Room Page",
                command=lambda: controller.show_frame("RoomPage"),
                height=2,
            )
        btns.append(btn_9)

        #Subject Page Button
        btn_10 = tk.Button(
                self,
                text="Subject Page",
                command=lambda: controller.show_frame("SubjectPage"),
                height=2,
            )
        btns.append(btn_10)

        #Year Group Page Button
        btn_11 = tk.Button(
                self,
                text="Year Group Page",
                command=lambda: controller.show_frame("YearGroupPage"),
                height=2,
            )
        btns.append(btn_11)

        #Student Page Button
        btn_12 = tk.Button(
                self,
                text="Student Page",
                command=lambda: controller.show_frame("StudentPage"),
                height=2,
            )
        btns.append(btn_12)
        
        for btn in btns:
            btn.pack(fill=tk.BOTH, pady=0.5)
