class SearchStud:
    def __init__(self, filename="student_data.txt"):
        self.filename = filename


    def searchstud(self, Idnum):
        with open(self.filename, "r") as file:
            for line in file:
                student_data = line.strip().split(', ')
                name = student_data[0]
                age = student_data[1]
                idnum = student_data[2]
                email = student_data[3]
                phone = student_data[4]

                if idnum == Idnum:
                    result = (f"\nStudent Found!\n\n"
                              f"Name: {name}\n"
                              f"Age: {age}\n"
                              f"ID Number: {idnum}\n"
                              f"Email: {email}\n"
                              f"Phone: {phone}\n")
                    return result
                
        return "Student not found..."    
    
    def printAllStudentInfo(self):
        all = []
        with open(self.filename, "r") as file:
            for line in file:
                student_data = line.strip().split(', ')

                name = student_data[0]
                age = student_data[1]
                idnum = student_data[2]
                email = student_data[3]
                phone = student_data[4]   
                
                all.append(
                    f"Name: {name}\n"
                    f"Age: {age}\n"
                    f"ID Number: {idnum}\n"
                    f"Email: {email}\n"
                    f"Phone: {phone}\n\n"
                    "--------------------------------------------------"
                )
            
        return "\n==== All Student's Information ====\n\n" + "\n\n".join(all)
                

