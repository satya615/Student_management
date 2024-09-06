from functools import partial
from tkinter import *
from tkinter import messagebox
import pymysql

class Management:
    def __init__(self, root):
        self.window = root
        self.window.title("Student Management System")
        self.window.geometry("780x480")
        self.window.config(bg="white")

        # Customization - Replace with your own customizations or use defaults
        self.color_1 = "#dfe3ee"  # Light color
        self.color_2 = "#3b5998"  # Dark color
        self.color_3 = "white"  # Text color
        self.color_4 = "gray"  # Entry background
        self.font_1 = "Arial"
        self.font_2 = "Helvetica"

        # Database connection credentials (Replace with your actual credentials)
        self.host = "localhost"
        self.user = "root"
        self.password = "satya"
        self.database = "student_management"

        # Left Frame
        self.frame_1 = Frame(self.window, bg=self.color_1)
        self.frame_1.place(x=0, y=0, width=540, relheight=1)

        # Right Frame
        self.frame_2 = Frame(self.window, bg=self.color_2)
        self.frame_2.place(x=540, y=0, relwidth=1, relheight=1)

        # Buttons
        Button(self.frame_2, text='Add New', font=(self.font_1, 12), bd=2, command=self.AddStudent, cursor="hand2", bg=self.color_2, fg=self.color_3).place(x=68, y=40, width=100)
        Button(self.frame_2, text='View Details', font=(self.font_1, 12), bd=2, command=self.GetContact_View, cursor="hand2", bg=self.color_2, fg=self.color_3).place(x=68, y=100, width=100)
        Button(self.frame_2, text='Update', font=(self.font_1, 12), bd=2, command=self.GetContact_Update, cursor="hand2", bg=self.color_2, fg=self.color_3).place(x=68, y=160, width=100)
        Button(self.frame_2, text='Delete', font=(self.font_1, 12), bd=2, command=self.GetContact_Delete, cursor="hand2", bg=self.color_2, fg=self.color_3).place(x=68, y=220, width=100)
        Button(self.frame_2, text='Clear', font=(self.font_1, 12), bd=2, command=self.ClearScreen, cursor="hand2", bg=self.color_2, fg=self.color_3).place(x=68, y=280, width=100)
        Button(self.frame_2, text='Exit', font=(self.font_1, 12), bd=2, command=self.Exit, cursor="hand2", bg=self.color_2, fg=self.color_3).place(x=68, y=340, width=100)

    def AddStudent(self):
        self.ClearScreen()
        
        Label(self.frame_1, text="First Name", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40, y=30)
        self.name_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.name_entry.place(x=40, y=60, width=200)

        Label(self.frame_1, text="Last Name", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300, y=30)
        self.surname_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.surname_entry.place(x=300, y=60, width=200)

        Label(self.frame_1, text="Course", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40, y=100)
        self.course_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.course_entry.place(x=40, y=130, width=200)

        Label(self.frame_1, text="Subject", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300, y=100)
        self.subject_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.subject_entry.place(x=300, y=130, width=200)

        Label(self.frame_1, text="Year", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40, y=170)
        self.year_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.year_entry.place(x=40, y=200, width=200)

        Label(self.frame_1, text="Age", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300, y=170)
        self.age_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.age_entry.place(x=300, y=200, width=200)

        Label(self.frame_1, text="Gender", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40, y=240)
        self.gender_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.gender_entry.place(x=40, y=270, width=200)

        Label(self.frame_1, text="Birthday", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300, y=240)
        self.birth_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.birth_entry.place(x=300, y=270, width=200)

        Label(self.frame_1, text="Contact", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40, y=310)
        self.contact_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.contact_entry.place(x=40, y=340, width=200)

        Label(self.frame_1, text="Email", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300, y=310)
        self.email_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.email_entry.place(x=300, y=340, width=200)

        Button(self.frame_1, text='Submit', font=(self.font_1, 12), bd=2, command=self.Submit, cursor="hand2", bg=self.color_2, fg=self.color_3).place(x=200, y=389, width=100)

    def Submit(self):
        # Collect data and insert into the database
        if self.name_entry.get() == "" or self.surname_entry.get() == "":
            messagebox.showerror("Error!", "All fields are required", parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
                curs = connection.cursor()
                curs.execute("INSERT INTO student_register (name, surname, course, subject, year, age, gender, birthday, contact, email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                            (self.name_entry.get(), self.surname_entry.get(), self.course_entry.get(), self.subject_entry.get(), self.year_entry.get(), 
                            self.age_entry.get(), self.gender_entry.get(), self.birth_entry.get(), self.contact_entry.get(), self.email_entry.get()))
                connection.commit()
                connection.close()
                messagebox.showinfo('Done!', "Data inserted successfully")
                self.ClearScreen()
            except Exception as e:
                messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

    def ClearScreen(self):
        for widget in self.frame_1.winfo_children():
            widget.destroy()

    def GetContact_View(self):
        self.ClearScreen()
        Label(self.frame_1, text="Enter Phone Number", font=(self.font_2, 18, "bold"), bg=self.color_1).place(x=140, y=70)
        self.getInfo_entry = Entry(self.frame_1, font=(self.font_1, 12), bg=self.color_4, fg=self.color_3)
        self.getInfo_entry.place(x=163, y=110, width=200, height=30)
        Button(self.frame_1, text='Submit', font=(self.font_1, 10), bd=2, command=self.CheckContact_View, cursor="hand2", bg=self.color_2, fg=self.color_3).place(x=220, y=150, width=80)

    def CheckContact_View(self):
        if self.getInfo_entry.get() == "":
            messagebox.showerror("Error!", "Please enter the phone number", parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
                curs = connection.cursor()
                curs.execute("SELECT * FROM student_register WHERE contact=%s", self.getInfo_entry.get())
                row = curs.fetchone()
                connection.close()

                if row is None:
                    messagebox.showerror("Error!", "No record found", parent=self.window)
                else:
                    self.ViewDetails(row)
            except Exception as e:
                messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

    def ViewDetails(self, row):
        self.ClearScreen()
        Label(self.frame_1, text="First Name", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40, y=30)
        Label(self.frame_1, text=row[1], font=(self.font_1, 12), bg=self.color_1).place(x=40, y=60)

        Label(self.frame_1, text="Last Name", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300, y=30)
        Label(self.frame_1, text=row[2], font=(self.font_1, 12), bg=self.color_1).place(x=300, y=60)

        Label(self.frame_1, text="Course", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40, y=100)
        Label(self.frame_1, text=row[3], font=(self.font_1, 12), bg=self.color_1).place(x=40, y=130)

        Label(self.frame_1, text="Subject", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300, y=100)
        Label(self.frame_1, text=row[4], font=(self.font_1, 12), bg=self.color_1).place(x=300, y=130)

        Label(self.frame_1, text="Year", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40, y=170)
        Label(self.frame_1, text=row[5], font=(self.font_1, 12), bg=self.color_1).place(x=40, y=200)

        Label(self.frame_1, text="Age", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300, y=170)
        Label(self.frame_1, text=row[6], font=(self.font_1, 12), bg=self.color_1).place(x=300, y=200)

        Label(self.frame_1, text="Gender", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40, y=240)
        Label(self.frame_1, text=row[7], font=(self.font_1, 12), bg=self.color_1).place(x=40, y=270)

        Label(self.frame_1, text="Birthday", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300, y=240)
        Label(self.frame_1, text=row[8], font=(self.font_1, 12), bg=self.color_1).place(x=300, y=270)

        Label(self.frame_1, text="Contact", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40, y=310)
        Label(self.frame_1, text=row[9], font=(self.font_1, 12), bg=self.color_1).place(x=40, y=340)

        Label(self.frame_1, text="Email", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300, y=310)
        Label(self.frame_1, text=row[10], font=(self.font_1, 12), bg=self.color_1).place(x=300, y=340)

    def GetContact_Update(self):
        self.GetContact_View()
        Button(self.frame_1, text='Update', font=(self.font_1, 10), bd=2, command=partial(self.UpdateDetails, self.row), cursor="hand2", bg=self.color_2, fg=self.color_3).place(x=220, y=400, width=80)

    def UpdateDetails(self, row):
        if self.name_entry.get() == "" or self.surname_entry.get() == "" or self.course_entry.get() == "" or self.subject_entry.get() == "" or self.year_entry.get() == "" or self.age_entry.get() == "" or self.gender_entry.get() == "" or self.birth_entry.get() == "" or self.email_entry.get() == "":
            messagebox.showerror("Error!", "All fields are required", parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
                curs = connection.cursor()
                curs.execute(
                    "UPDATE student_register SET first_name=%s, last_name=%s, course=%s, subject=%s, year=%s, age=%s, gender=%s, birthday=%s, email=%s WHERE contact=%s",
                    (
                        self.name_entry.get(),
                        self.surname_entry.get(),
                        self.course_entry.get(),
                        self.subject_entry.get(),
                        self.year_entry.get(),
                        self.age_entry.get(),
                        self.gender_entry.get(),
                        self.birth_entry.get(),
                        self.email_entry.get(),
                        row[8]  # Assuming contact as identifier
                    )
                )
                connection.commit()
                messagebox.showinfo("Success", "Student details updated successfully", parent=self.window)
                connection.close()
                self.ClearScreen()
            except Exception as e:
                messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

    def GetContact_Delete(self):
        self.GetContact_View()
        Button(self.frame_1, text='Delete', font=(self.font_1, 10), bd=2, command=partial(self.DeleteRecord, self.row), cursor="hand2", bg=self.color_2, fg=self.color_3).place(x=220, y=400, width=80)

    def DeleteRecord(self, row):
        try:
            connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            curs = connection.cursor()
            curs.execute("DELETE FROM student_register WHERE contact=%s", (row[9],))
            connection.commit()
            connection.close()
            messagebox.showinfo('Done!', "Record deleted successfully", parent=self.window)
            self.ClearScreen()
        except Exception as e:
            messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

    def Exit(self):
        self.window.quit()

# Driver Code
if __name__ == "__main__":
    root = Tk()
    obj = Management(root)
    root.mainloop()
