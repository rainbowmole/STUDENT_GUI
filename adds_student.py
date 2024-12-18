from tkinter import *
from student import StudentInfo
import tkinter.messagebox

class AddStudent:
    def __init__(self, student_data, constructor, filename="student_data.txt"):
        self.student_data = student_data
        self.filename = filename
        self.constructor = constructor
        self.students_id = []
        self.fetch_all_students()

    def fetch_all_students(self) -> list[object]:
         with open(self.filename, "r") as file:
            for line in file:
                student_data = line.strip().split(', ')
                #print(student_data)
                name, age, id, email, phone = student_data
                student = self.constructor(name, age, id, email, phone)
                self.students_id.append(student_data[2])
 

    def store_in_file(self, student):
        with open(self.filename, "a+") as file:
            file.write(student.to_file())

    def add_student(self, name, age, idnum, email, phone):
        student = StudentInfo()

        student.setName(name)
        student.setAge(age)
        student.setIdnum(idnum)
        student.setEmail(email)
        student.setPhone(phone)

        self.store_in_file(student)
        print(f'\nAdded student {name} to the list')
    
    def new_student(self):
        newstud = StudentInfo()

        print("\n===ADD NEW STUDENT===")
        name, age, idnum, email, phone = input("\nEnter Name: "), int(input("Enter Age: ")), input("Enter ID Number: "), input("Enter Email: "), input("Enter Phone Number: ")
        print("\n===NOTHING FOLLOWS===\n")

        newstud.setName(name)
        newstud.setAge(age)
        newstud.setIdnum(idnum)
        newstud.setEmail(email)
        newstud.setPhone(phone)

        self.store_in_file(newstud)
        print(f'\nAdded student {name} to the list')

    def reg_ui(self, reg_frame):
        self.lblError = Label(reg_frame, text="", font=('Century Gothic', 20), fg="red", bg="#0f0f0f")
        self.lblError.grid(row=1, column=0, columnspan=4)

        self.reg_lbl_txt = ["Name", "Age", "Student Id", "Email Address", "Phone Number"]
        self.reg_entry = []

        for i in range(len(self.reg_lbl_txt)):
            Label(reg_frame, text=self.reg_lbl_txt[i], font=("Courier", 16),bg="#0f0f0f", fg="#00ee00", anchor="w", width=14).grid(row=i+2, column=0)
            self.reg_entry.append(Entry(reg_frame, width=40, font=("Courier", 16), bg="#00ee00", fg="#0f0f0f", insertbackground="#0f0f0f", relief="flat"))
            self.reg_entry[i].grid(row=i+2, column=1)

        reg_btn = Button(reg_frame, width=25, text="Register Student", font=("Courier", 14), bg="#002f00", fg="#00ee00", relief="flat", command=self.check_entries)
        reg_btn.grid(row=8, columnspan=4)

    def reset_txts(self):
        for i in range(len(self.reg_entry)):
            self.reg_entry[i].delete(0, END)
    
    def reset_error(self):
        self.lblError.config(text="")
        self.reset_txts()
    
    def check_entries(self):
        errors = []

        for i in range(len(self.reg_entry)):
            if self.reg_entry[i].get() == "":
                errors.append(f"You forgot to add the {self.reg_lbl_txt[i]}\n")
        
        studentId = self.reg_entry[2].get()
        if self.reg_entry[2].get() in self.students_id:
            errors.append(f"The ID: {studentId} is already taken")

        if not errors:
            self.add_student(self.reg_entry[0].get(), 
                            self.reg_entry[1].get(), 
                            self.reg_entry[2].get(), 
                            self.reg_entry[3].get(), 
                            self.reg_entry[4].get(),)
            
            tkinter.messagebox.showinfo("New Student Registration Success", "Added student to the list!")
            self.reset_error()
        else:
            self.lblError.config(text=f"The following error(s) occured: \n{' '.join(errors)}")

    

