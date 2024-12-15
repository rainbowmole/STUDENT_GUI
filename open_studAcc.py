from student import StudentInfo

class openAcc:
    def __init__(self, filename="student_data.txt"):
        self.filename = filename

    def open_studentAcc(self, idnum):
        with open(self.filename) as file:
            for line in file:
                student_data = line.strip().split(', ')

                name = student_data[0]
                age = student_data[1]
                id_number = student_data[2]
                email = student_data[3]
                phone = student_data[4]

                if id_number == idnum:
                    student = StudentInfo()
                    student.setName(name)
                    student.setAge(age)
                    student.setIdnum(id_number)    
                    student.setEmail(email)
                    student.setPhone(phone)

                    print(f"Welcome, {name}!")
                    return student
                
        print("ID not found..."); return False       
