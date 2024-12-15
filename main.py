import os
from student import StudentInfo
from adds_student import AddStudent
from open_studAcc import openAcc
from student_search import SearchStud

filename = "student_data.txt" 
if not os.path.exists(filename): #this is just to create a file if there's none existing
    with open(filename, "w") as file:
        pass 

stu = StudentInfo()
studAcc = openAcc("student_data.txt")
addstud = AddStudent(stu)
search = SearchStud("student_data.txt")

#undo the comment if it's running on a new pc| addstud.add_student("Admin Camacho", "20", "2023-2-02449", "nat@gmail.com", "09560252200") 

def main():
    student = None
    for a in range(4):
        os.system("cls")
        idnum = input("\n\nWelcome to student portal!\nEnter student ID number: ")
        student = studAcc.open_studentAcc(idnum)
        if student:
            studportal(student)
            break
    else: print("Exiting")
        
def studportal(student):
    os.system("cls")
    while True:
        print(f"Welcome, {student.getName()}!\n")
        choice = input("Please choose from the following options\n1. View your Information\n2. View other student's information\n3. Register new student\'s info\n4. View all students in the list\n5. Exit\nEnter choice: ")

        if choice == '1': print(search.searchstud(student.getIdnum())) #your info
        
        elif choice == '2': #ibang info
            otherid = input("\nEnter the student\'s id number: ")
            print(search.searchstud(otherid))

        elif choice == '3': addstud.new_student() #registration

        elif choice == "4": print(search.printAllStudentInfo()) #view all

        elif choice == '5': #exit na
            print("\nThank you for using.")
            quit()

        else: print("Invalid input, please try again."); studportal(stu.getIdnum())

        again = input("\nContinue? [y/n]\nChoice: ").lower()
        if again == 'y': os.system("cls")
        else:
            print("\nThank you for using.")
            break
main()