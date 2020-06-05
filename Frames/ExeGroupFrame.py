import tkinter as tk

from Tables.ExeGroup import ExeGroup

from tk_extension.multilistBox import MultiListBox


class ExeGroupPage(tk.Frame):
    """
    Main Exercise Group Page
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.columnconfigure([x for x in range(7)], minsize=245)
        self.rowconfigure([x for x in range(9)], minsize=100)
        self.controller = controller
        self.main_label()

        self.group_listbox()
        self.refresh_button()
        self.buttons()


    def main_label(self):
        """create exe group main label
        """
        label = tk.Label(
            self,
            text="Exercise Group Page",
            font=self.controller.title_font,
        )
        label.grid(row=0, column = 6, sticky="news", padx=5, pady=5)

    
    def buttons(self):
        """create exe group page buttons 
        """
        #Return Home Page
        btn_return = tk.Button(
            self,
            text="Home",
            command=lambda : self.controller.show_frame("StartPage"),
            font=self.controller.normal_font,
        )
        btn_return.grid(row=4, column=6, sticky="news", padx=5, pady=5)
        #Create Exercise Group Button
        btn_create = tk.Button(
            self,
            text="Create Group",
            command=lambda : self.create_group(),
            font=self.controller.normal_font,
        )
        btn_create.grid(row=1, column=6, sticky="news", padx=5, pady=5)
        #Delete Exercise Group Button
        btn_delete = tk.Button(
            self,
            text="Delete Group",
            command=lambda : self.delete_group(),
            font=self.controller.normal_font
        )
        btn_delete.grid(row=2, column=6, sticky="news", padx=5, pady=5)
        #Show Exercise Group Button
        btn_show = tk.Button(
            self,
            text="Show Group",
            command=lambda : self.show_group(),
            font=self.controller.normal_font,
        )
        btn_show.grid(row=3, column=6, sticky="news", padx=5, pady=5)


    def group_listbox(self):
        """create exe group listbox
        """
        data = [
            ('number',10),
            ('field of study', 20),
            ('department', 20),
            ('students', 10) #numbers of students
        ]

        self.list_groups = MultiListBox(master=self, data=data)
        self.refresh()
        self.list_groups.grid(row=0, column=0, columnspan=6, rowspan=9, sticky="news", padx=5, pady=5)


    def create_group(self):
        """func change page to CreateExeGroupPage
        """
        self.controller.show_frame("CreateExeGroupPage")


    def delete_group(self):
        """func delete exe group from listbox and config
        other frames
        """
        idx = self.list_groups.index(tk.ACTIVE)
        del_group = self.controller.exe_groups.pop(idx)

        try:
            del_group.delete(self.controller.db)
            self.controller.db.commit_conn()
        except AttributeError:
            pass

        del del_group
        # config
        self.controller.frames["ExeSubjectPage"].refresh()
        self.controller.frames["CreateExeSubjectPage"].refresh_exe_listbox()
        self.controller.frames["ExeAddStudentPage"].refresh_student_listbox()
        self.restart()


    def show_group(self):
        """func set exe group to show and change
        page to ExeStudentPage
        """
        idx = self.list_groups.index(tk.ACTIVE)
        group = self.controller.exe_groups[idx]

        self.controller.frames["ExeStudentPage"].set_group(group)
        self.controller.frames["ExeStudentPage"].refresh_student_listbox()
        self.controller.show_frame("ExeStudentPage")


    def restart(self):
        """func restart frame
        """
        self.refresh()
        self.controller.show_frame("ExeGroupPage")

    
    def refresh_button(self):
        """create refresh button
        """
        btn_refresh = tk.Button(
            master=self,
            text="refresh",
            command=lambda : self.restart(),
            font=self.controller.normal_font,
        )
        btn_refresh.grid(row=8, column=6, sticky="news", padx=5, pady=5)


    def refresh(self):
        """func refresh exe group listbox
        """
        self.list_groups.delete(0, tk.END)
        for i, group in enumerate(self.controller.exe_groups):
            try:
                field = group.get_field().get_name()
                try:
                    dept = group.get_field().get_department().get_name()
                except AttributeError:
                    dept = "NULL"
            except AttributeError:
                field = "NULL"
                dept = "NULL"

            output = (
                group.get_number(),
                field,
                dept,
                len(group.get_students())
            )

            self.list_groups.insert(i, output)



class CreateExeGroupPage(tk.Frame):
    """
    Page where we can create exe group
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.columnconfigure([x for x in range(9)], minsize=250)
        self.rowconfigure([x for x in range(18)], minsize=50)
        self.controller = controller
        self.main_label()
        self.return_button()
        self.home_button()
        self.number_entry()
        self.field_listbox()
        self.submit()


    def main_label(self):
        """create exe group main label
        """
        label = tk.Label(
            self,
            text="Create Group",
            font=self.controller.title_font
        )
        label.grid(row=0, column=0, rowspan=1, columnspan=4, sticky="news", padx=5, pady=5)


    def return_button(self):
        """create return button
        """
        btn_return = tk.Button(
            self,
            text="return",
            command=lambda : self.return_refresh(),
            font=self.controller.normal_font
        )
        btn_return.grid(row=16, column=0, rowspan=2, columnspan=2, sticky="news", padx=5, pady=5)


    def home_button(self):
        """create home button
        """
        btn_home = tk.Button(
            self,
            text="Home",
            command=lambda : self.home_refresh(),
            font=self.controller.normal_font,
        )
        btn_home.grid(row=16, column=2,rowspan=2, columnspan=2, sticky="news", padx=5, pady=5)


    def return_refresh(self):
        """func change page to ExeGroupPage
        """
        self.refresh()
        self.controller.show_frame("ExeGroupPage")


    def home_refresh(self):
        """func change page to StartPage
        """
        self.refresh()
        self.controller.show_frame("StartPage")


    def refresh(self):
        """clear all entries
        """
        self.e_number.delete(0, tk.END)


    def number_entry(self):
        """create entry for number with label
        """
        l_number = tk.Label(master=self, text="number",font=self.controller.normal_font, anchor=tk.W, relief=tk.RAISED)
        l_number.grid(row=1, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)

        self.e_number = tk.Entry(master=self, font=self.controller.entry_font)
        self.e_number.grid(row=2, column=0, columnspan=4, sticky="nswe", pady=0, padx=5)


    def field_listbox(self):
        """create field of study listbox for Exe Group Page
        """
        l_field = tk.Label(master=self, text="field of study", font=self.controller.normal_font, relief=tk.RAISED)
        l_field.grid(row=0, column=4, rowspan=1, columnspan=3, sticky="nswe", pady=5, padx=5)
        
        data = [
            ('field of study', 20),
            ('department', 20)
        ]

        self.list_fields = MultiListBox(master=self, data=data)
        self.list_fields.grid(row=1, column=4, rowspan=17, columnspan=3, sticky="nswe", pady=5, padx=5)
        self.refresh_field_listbox()


    def refresh_field_listbox(self):
        """refresh field of study listbox
        """
        self.list_fields.delete(0, tk.END)
        for i, field in enumerate(self.controller.fields):
            try:
                dept = field.get_department().get_name()
            except AttributeError:
                dept = "NULL"

            output = (
                field.get_name(),
                dept
            )

            self.list_fields.insert(i, output)


    def submit(self):
        """create submit button
        """
        sub_btn = tk.Button(
            master=self,
            text="submit",
            command=lambda : self.create_group(),
            font=self.controller.normal_font,
        )
        sub_btn.grid(row=14, column=0, rowspan=2, columnspan=4, sticky="nswe", pady=5, padx=5)


    def create_group(self):
        """func create new exe group and config other frames
        """
        try:
            idx = self.list_fields.index(tk.ACTIVE)
            field = self.controller.fields[idx]
        except IndexError:
            field = None

        self.controller.exe_groups.append(ExeGroup(
            number=self.e_number.get(),
            field=field,
            students={}
        ))

        # update Subject
        self.controller.frames["ExeSubjectPage"].refresh()
        self.controller.frames["CreateExeSubjectPage"].refresh_exe_listbox()
        # self config
        self.refresh()
        self.controller.db.commit_conn()
        self.controller.frames["ExeGroupPage"].restart()


class ExeStudentPage(tk.Frame):
    """
    Page where we can show all students in selected group
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.columnconfigure([x for x in range(7)], minsize=250)
        self.rowconfigure([x for x in range(9)], minsize=100)
        if controller.exe_groups:
            self.group = controller.exe_groups[0]

        self.controller = controller
        self.main_label()
        self.return_button()
        self.home_button()
        self.add_button()
        self.delete_button()
        self.student_listbox()


    def set_group(self, group):
        """set exe group instance

        Args:
            group (ExeGroup): exe group which we want show
        """
        self.group = group


    def main_label(self):
        """create show exe group main label
        """
        label = tk.Label(
            self,
            text="Exe Group",
            font=self.controller.title_font
        )
        label.grid(row=0, column = 6, sticky="news", padx=5, pady=5)


    def return_button(self):
        """create return button
        """
        btn_return = tk.Button(
            self,
            text="return",
            command=lambda : self.controller.show_frame("ExeGroupPage"),
            font=self.controller.normal_font
        )
        btn_return.grid(row=7, column=6, sticky="news", padx=5, pady=5)


    def home_button(self):
        """create home button
        """
        btn_home = tk.Button(
            self,
            text="Home",
            command=lambda : self.controller.show_frame("StartPage"),
            font=self.controller.normal_font,
        )
        btn_home.grid(row=8, column=6, sticky="news", padx=5, pady=5)


    def student_listbox(self):
        """create student listbox for Exe Student Group Page
        """
        data = [
            ('id', 10),
            ('name', 20),
            ('second name', 20),
            ('lastname', 20),
            ('ssn', 20),
            ('email', 20),
            ('field of study', 20),
            ('department', 20),
            ('place of residence', 30)
        ]

        self.list_students = MultiListBox(master=self, data=data)
        self.list_students.grid(row=0, column=0, columnspan=6, rowspan=9, sticky="news", padx=5, pady=5)
        self.refresh_student_listbox()


    def refresh_student_listbox(self):
        """refresh student listbox
        """
        self.list_students.delete(0, tk.END)
        try:
            for i, student in enumerate(self.group.get_students()):
                try:
                    field = student.get_field_of_study().get_name()
                    try:
                        department = student.get_field_of_study().get_department().get_name()
                    except AttributeError:
                        department = "NULL"
                except AttributeError:
                    field = "NULL"
                    department = "NULL"

                output = (
                    student.get_id(),
                    student.get_name(),
                    student.get_sec_name(),
                    student.get_lastname(),
                    student.get_ssn(),
                    student.get_email(),
                    field,
                    department,
                    student.get_place_of_residence()
                    )
                self.list_students.insert(i,output)
        except AttributeError:
            pass


    def add_button(self):
        """create add button
        """
        add_btn = tk.Button(
            master=self,
            text="add Student",
            command=lambda : self.add_student(),
            font=self.controller.normal_font
        )
        add_btn.grid(row=1, column=6, sticky="news", padx=5, pady=5)


    def delete_button(self):
        """create del button
        """
        delete_btn = tk.Button(
            master=self,
            text="del Student",
            command=lambda : self.del_student(),
            font=self.controller.normal_font,
        )
        delete_btn.grid(row=2, column=6, sticky="news", padx=5, pady=5)


    def add_student(self):
        """func set exe group to add student and change
        page to ExeAddStudentPage
        """
        self.controller.frames["ExeSubjectPage"].refresh()
        self.controller.frames["CreateExeSubjectPage"].refresh_exe_listbox()

        self.controller.frames["ExeAddStudentPage"].set_group(self.group)
        self.controller.frames["ExeAddStudentPage"].refresh_student_listbox()
        self.controller.show_frame("ExeAddStudentPage")


    def del_student(self):
        """func remove student from student listbox
        """
        idx = self.list_students.index(tk.ACTIVE)
        student = list(self.group.get_students())[idx]

        self.group.delete_student(student, self.controller.db)
        self.controller.db.commit_conn()

        self.controller.frames["ExeGroupPage"].refresh()
        self.refresh_student_listbox()


class ExeAddStudentPage(tk.Frame):
    """
    Page where we can add student to group
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.columnconfigure([x for x in range(7)], minsize=250)
        self.rowconfigure([x for x in range(9)], minsize=100)
        self.controller = controller

        if self.controller.exe_groups:
            self.group = self.controller.exe_groups[0]
        else:
            self.group = None

        self.main_label()
        self.return_button()
        self.student_listbox()
        self.submit()


    def set_group(self, group):
        """set exe group instance

        Args:
            group (ExeGroup): exe group which we want modify
        """
        self.group = group


    def main_label(self):
        """create add student to group main label
        """
        label = tk.Label(
            self,
            text="Add Student",
            font=self.controller.title_font
        )
        label.grid(row=0, column = 6, sticky="news", padx=5, pady=5)


    def student_listbox(self):
        """create student listbox for Add Student Exe Group Page
        """
        data = [
            ('id', 10),
            ('name', 20),
            ('second name', 20),
            ('lastname', 20),
            ('ssn', 20),
            ('email', 20),
            ('field of study', 20),
            ('department', 20),
            ('place of residence', 30)
        ]

        self.list_students = MultiListBox(master=self, data=data)
        self.list_students.grid(row=0, column=0, columnspan=6, rowspan=9, sticky="news", padx=5, pady=5)


    def return_button(self):
        """create return button
        """
        btn_return = tk.Button(
            self,
            text="return",
            command=lambda : self.controller.show_frame("ExeStudentPage"),
            font=self.controller.normal_font,
        )
        btn_return.grid(row=8, column=6, sticky="news", padx=5, pady=5)


    def refresh_student_listbox(self):
        """refresh student listbox
        """
        self.list_students.delete(0, tk.END)
        for i, student in enumerate(self.avi_students()):
                try:
                    field = student.get_field_of_study().get_name()
                    try:
                        department = student.get_field_of_study().get_department().get_name()
                    except AttributeError:
                        department = "NULL"
                except AttributeError:
                    field = "NULL"
                    department = "NULL"

                output = (
                    student.get_id(),
                    student.get_name(),
                    student.get_sec_name(),
                    student.get_lastname(),
                    student.get_ssn(),
                    student.get_email(),
                    field,
                    department,
                    student.get_place_of_residence()
                    )
                self.list_students.insert(i,output)


    def avi_students(self):
        """func calculate available student which
        we can add to group

        Returns:
            List: list of available students
        """
        if self.group is not None:
            return [student for student in self.controller.students if student not in ExeGroup.all_students and student.get_field_of_study() == self.group.get_field()]
        else:
            return []

    def submit(self):
        """create submit button
        """
        sub_btn = tk.Button(
            master=self,
            text="submit",
            command=lambda : self.add_student(),
            font=self.controller.normal_font
        )
        sub_btn.grid(row=1, column=6, sticky="news", padx=5, pady=5)


    def add_student(self):
        """func add student to group and config other frames
        """
        try:
            idx = self.list_students.index(tk.ACTIVE)
            student = self.avi_students()[idx]
            self.group.insert(student, self.controller.db)
            self.controller.db.commit_conn()

            self.controller.frames["ExeSubjectPage"].refresh()
            self.controller.frames["CreateExeSubjectPage"].refresh_exe_listbox()

            self.controller.frames["ExeStudentPage"].refresh_student_listbox()
            self.controller.frames["ExeGroupPage"].refresh()
            self.controller.show_frame("ExeStudentPage")
        except IndexError:
            self.controller.show_frame("ExeStudentPage")
