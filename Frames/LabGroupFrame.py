import tkinter as tk

from Tables.LabGroup import LabGroup

from tk_extension.multilistBox import MultiListBox


class LabGroupPage(tk.Frame):
    """
    Main Laboratory Group Page
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.columnconfigure([x for x in range(7)], minsize=240)
        self.rowconfigure([x for x in range(9)], minsize=100)
        self.controller = controller
        self.main_label()

        self.group_listbox()
        self.refresh_button()
        self.buttons()

    def main_label(self):
        """create lab group main label
        """
        label = tk.Label(
            self,
            text="Laboratory Group Page",
            font=self.controller.title_font
        )
        label.grid(row=0, column=6, sticky="news", padx=5, pady=5)

    def buttons(self):
        """create lab group page buttons
        """
        # Return Home Page
        btn_return = tk.Button(
            self,
            text="Home",
            command=lambda: self.controller.show_frame("StartPage"),
            font=self.controller.normal_font,
        )
        btn_return.grid(row=4, column=6, sticky="news", padx=5, pady=5)
        # Create Laboratory Group Button
        btn_create = tk.Button(
            self,
            text="Create Group",
            command=lambda: self.create_group(),
            font=self.controller.normal_font,
        )
        btn_create.grid(row=1, column=6, sticky="news", padx=5, pady=5)
        # Delete Laboratory Group Button
        btn_delete = tk.Button(
            self,
            text="Delete Group",
            command=lambda: self.delete_group(),
            font=self.controller.normal_font,
        )
        btn_delete.grid(row=2, column=6, sticky="news", padx=5, pady=5)
        # Show Laboratory Group Button
        btn_show = tk.Button(
            self,
            text="Show Group",
            command=lambda: self.show_group(),
            font=self.controller.normal_font,
        )
        btn_show.grid(row=3, column=6, sticky="news", padx=5, pady=5)

    def group_listbox(self):
        """create lab group listbox
        """
        data = [
            ('number', 10),
            ('field of study', 20),
            ('department', 20),
            ('students', 10)  # numbers of students
        ]

        self.list_groups = MultiListBox(master=self, data=data)
        self.refresh()
        self.list_groups.grid(
            row=0,
            column=0,
            columnspan=6,
            rowspan=9,
            sticky="news",
            padx=5,
            pady=5
        )

    def create_group(self):
        """func change page to CreateLabGroupPage
        """
        self.controller.show_frame("CreateLabGroupPage")

    def delete_group(self):
        """func delete lab group from listbox and config
        other frames
        """
        idx = self.list_groups.index(tk.ACTIVE)
        del_group = self.controller.lab_groups.pop(idx)

        try:
            del_group.delete(self.controller.db)
            self.controller.db.commit_conn()
        except AttributeError:
            pass

        del del_group
        # config
        self.controller.frames["LabSubjectPage"].refresh()
        self.controller.frames["CreateLabSubjectPage"].refresh_lab_listbox()
        self.controller.frames["LabAddStudentPage"].refresh_student_listbox()
        self.restart()

    def show_group(self):
        """func set lab group to show and change
        page to LabStudentPage
        """
        idx = self.list_groups.index(tk.ACTIVE)
        group = self.controller.lab_groups[idx]

        self.controller.frames["LabStudentPage"].set_group(group)
        self.controller.frames["LabStudentPage"].refresh_student_listbox()
        self.controller.show_frame("LabStudentPage")

    def restart(self):
        """func restart frame
        """
        self.refresh()
        self.controller.show_frame("LabGroupPage")

    def refresh_button(self):
        """create refresh button
        """
        btn_refresh = tk.Button(
            master=self,
            text="refresh",
            command=lambda: self.restart(),
            font=self.controller.normal_font,
        )
        btn_refresh.grid(row=8, column=6, sticky="news", padx=5, pady=5)

    def refresh(self):
        """func refresh lab group listbox
        """
        self.list_groups.delete(0, tk.END)
        for i, group in enumerate(self.controller.lab_groups):
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


class CreateLabGroupPage(tk.Frame):
    """
    Page where we can create lab group
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
        """create lab group main label
        """
        label = tk.Label(
            self,
            text="Create Group",
            font=self.controller.title_font
        )
        label.grid(
            row=0,
            column=0,
            rowspan=1,
            columnspan=4,
            sticky="news",
            padx=5,
            pady=5
        )

    def return_button(self):
        """create return button
        """
        btn_return = tk.Button(
            self,
            text="return",
            command=lambda: self.return_refresh(),
            font=self.controller.normal_font,
        )
        btn_return.grid(
            row=16,
            column=0,
            rowspan=2,
            columnspan=2,
            sticky="news",
            padx=5,
            pady=5
        )

    def home_button(self):
        """create home button
        """
        btn_home = tk.Button(
            self,
            text="Home",
            command=lambda: self.home_refresh(),
            font=self.controller.normal_font,
        )
        btn_home.grid(
            row=16,
            column=2,
            rowspan=2,
            columnspan=2,
            sticky="news",
            padx=5,
            pady=5
        )

    def return_refresh(self):
        """func change page to LabGroupPage
        """
        self.refresh()
        self.controller.show_frame("LabGroupPage")

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
        l_number = tk.Label(
            master=self,
            text="number",
            font=self.controller.normal_font,
            anchor=tk.W,
            relief=tk.RAISED
        )
        l_number.grid(
            row=1,
            column=0,
            columnspan=4,
            sticky="nswe",
            pady=0,
            padx=5
        )

        self.e_number = tk.Entry(
            master=self,
            font=self.controller.entry_font
        )
        self.e_number.grid(
            row=2,
            column=0,
            columnspan=4,
            sticky="nswe",
            pady=0,
            padx=5
        )

    def field_listbox(self):
        """create field of study listbox for Lab Group Page
        """
        l_field = tk.Label(
            master=self,
            text="field of study",
            font=self.controller.normal_font,
            relief=tk.RAISED
        )
        l_field.grid(
            row=0,
            column=4,
            rowspan=1,
            columnspan=3,
            sticky="nswe",
            pady=5,
            padx=5
        )

        data = [
            ('field of study', 20),
            ('department', 20)
        ]

        self.list_fields = MultiListBox(master=self, data=data)
        self.list_fields.grid(
            row=1,
            column=4,
            rowspan=17,
            columnspan=3,
            sticky="nswe",
            pady=5,
            padx=5
        )
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
            command=lambda: self.create_group(),
            font=self.controller.normal_font,
        )
        sub_btn.grid(
            row=14,
            column=0,
            rowspan=2,
            columnspan=4,
            sticky="nswe",
            pady=5,
            padx=5
        )

    def create_group(self):
        """func create new lab group and config other frames
        """
        try:
            idx = self.list_fields.index(tk.ACTIVE)
            field = self.controller.fields[idx]
        except IndexError:
            field = None

        self.controller.lab_groups.append(LabGroup(
            number=self.e_number.get(),
            field=field,
            students={}
        ))

        # update Subject
        self.controller.frames["LabSubjectPage"].refresh()
        self.controller.frames["CreateLabSubjectPage"].refresh_lab_listbox()

        self.refresh()
        self.controller.db.commit_conn()
        self.controller.frames["LabGroupPage"].restart()


class LabStudentPage(tk.Frame):
    """
    Page where we can show all students in selected group
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.columnconfigure([x for x in range(7)], minsize=250)
        self.rowconfigure([x for x in range(9)], minsize=100)
        if controller.lab_groups:
            self.group = controller.lab_groups[0]

        self.controller = controller
        self.main_label()
        self.return_button()
        self.home_button()
        self.add_button()
        self.delete_button()
        self.student_listbox()

    def set_group(self, group):
        """set lab group instance

        Args:
            group (LabGroup): lab group which we want show
        """
        self.group = group

    def main_label(self):
        """create show lab group main label
        """
        label = tk.Label(
            self,
            text="Lab Group",
            font=self.controller.title_font
        )
        label.grid(row=0, column=6, sticky="news", padx=5, pady=5)

    def return_button(self):
        """create return button
        """
        btn_return = tk.Button(
            self,
            text="return",
            command=lambda: self.controller.show_frame("LabGroupPage"),
            font=self.controller.normal_font,
        )
        btn_return.grid(row=7, column=6, sticky="news", padx=5, pady=5)

    def home_button(self):
        """create home button
        """
        btn_home = tk.Button(
            self,
            text="Home",
            command=lambda: self.controller.show_frame("StartPage"),
            font=self.controller.normal_font,
        )
        btn_home.grid(row=8, column=6, sticky="news", padx=5, pady=5)

    def student_listbox(self):
        """create student listbox for Lab Student Group Page
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
        self.list_students.grid(
            row=0,
            column=0,
            columnspan=6,
            rowspan=9,
            sticky="news",
            padx=5,
            pady=5
        )
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
                    student.get_place_of_residence(),
                )
                self.list_students.insert(i, output)
        except AttributeError:
            pass

    def add_button(self):
        """create add button
        """
        add_btn = tk.Button(
            master=self,
            text="add Student",
            command=lambda: self.add_student(),
            font=self.controller.normal_font,
        )
        add_btn.grid(row=1, column=6, sticky="news", padx=5, pady=5)

    def delete_button(self):
        """create del button
        """
        delete_btn = tk.Button(
            master=self,
            text="del Student",
            command=lambda: self.del_student(),
            font=self.controller.normal_font,
        )
        delete_btn.grid(row=2, column=6, sticky="news", padx=5, pady=5)

    def add_student(self):
        """func set lab group and add student and change
        page to LabAddStudentPage
        """
        self.controller.frames["LabAddStudentPage"].set_group(self.group)
        self.controller.frames["LabAddStudentPage"].refresh_student_listbox()
        self.controller.show_frame("LabAddStudentPage")

    def del_student(self):
        """func remove student from student listbox
        """
        idx = self.list_students.index(tk.ACTIVE)
        student = list(self.group.get_students())[idx]

        self.group.delete_student(student, self.controller.db)
        self.controller.db.commit_conn()

        self.controller.frames["LabGroupPage"].refresh()
        self.refresh_student_listbox()


class LabAddStudentPage(tk.Frame):
    """
    Page where we can add student to group
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.columnconfigure([x for x in range(7)], minsize=250)
        self.rowconfigure([x for x in range(9)], minsize=100)
        self.controller = controller
        if self.controller.lab_groups:
            self.group = self.controller.lab_groups[0]
        else:
            self.group = None

        self.main_label()
        self.return_button()
        self.student_listbox()
        self.submit()

    def set_group(self, group):
        """set lab group instance

        Args:
            group (LabGroup): lab group which we want modify
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
        label.grid(row=0, column=6, sticky="news", padx=5, pady=5)

    def student_listbox(self):
        """create student listbox for Add Student Lab Group Page
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
        self.list_students.grid(
            row=0,
            column=0,
            columnspan=6,
            rowspan=9,
            sticky="news",
            padx=5,
            pady=5
        )

    def return_button(self):
        """create return button
        """
        btn_return = tk.Button(
            self,
            text="return",
            command=lambda: self.controller.show_frame("LabStudentPage"),
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
                student.get_place_of_residence(),
            )
            self.list_students.insert(i, output)

    def avi_students(self):
        """func calculate available student which
        we can add to group

        Returns:
            List: list of available students
        """
        if self.group is not None:
            return [student for student in self.controller.students if student not in LabGroup.all_students and student.get_field_of_study() == self.group.get_field()]
        else:
            return []

    def submit(self):
        """create submit button
        """
        sub_btn = tk.Button(
            master=self,
            text="submit",
            command=lambda: self.add_student(),
            font=self.controller.normal_font,
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

            self.controller.frames["LabSubjectPage"].refresh()

            self.controller.frames["LabStudentPage"].refresh_student_listbox()
            self.controller.frames["LabGroupPage"].refresh()
            self.controller.show_frame("LabStudentPage")
        except IndexError:
            self.controller.show_frame("LabStudentPage")
