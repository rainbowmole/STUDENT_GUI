class StudentInfo:
    def __init__(self, name="", age=0, idnum="", email="", phone=""):
        self.name = ""
        self.age = 0
        self.idnum = ""
        self.email = ""
        self.phone = ""
    
    def setName(self, name):
        self.name = name
    
    def setAge(self, age):
        self.age = age
    
    def setIdnum(self, idnum):
        self.idnum = idnum
    
    def setEmail(self, email):
        self.email = email
    
    def setPhone(self, phone):
        self.phone = phone
    
    def getName(self):
        return self.name

    def getAge(self):
        return self.age
    
    def getIdnum(self):
        return self.idnum
    
    def getEmail(self):
        return self.email

    def getPhone(self):
        return self.phone
    
    def to_file(self):
        return f"{self.name}, {self.age}, {self.idnum}, {self.email}, {self.phone}\n"