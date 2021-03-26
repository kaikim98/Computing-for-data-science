class Member:
    def __init__(self, name: str, adress:str, email:str, DoB:str, affiliation:str) -> None:
        self.name = name
        self.adress = adress
        self.email = email
        self.DoB = DoB
        self.affiliation = affiliation
        self.infoList = [self.name, self.adress, self.email, self.DoB, self.affiliation]
        
    def printinfo(self):
        print(self.infoList)
        
    def switch_affiliation(self, new_affiliation:str):
        print('member', self.name, 'changes affiliation from', self.affiliation, 'to', new.affiliation)
        self.affiliation = new.affiliation

class Student(Member):
    def __init__(self, name:str, address: str, email:str, DoB: str, affiliation: str, student_num:str):
        #reuse parent's init function
        super().__init__(name, address, email, DoB, affiliation)
        #student-specific init
        self.student_num = student_num
        self.advisor = ''
        self.courses_taken = []
        self.courses_taking = []
        self.GPA = []
        self.infoList += [self.student_num, self.advisor, self.courses_taken, self.courses_taking, self.GPA]

    #printing method is inherited
    #switch_affiliatoin is inherited but [polymorphism] works here
    def switch_affiliation(self, new_affiliation:str):
        print('student', self.name, 'changes affiliation from', self.affiliation, 'to', new.affiliation)
        self.affiliation = new.affiliation

class Faculty(Member):
    def __init__(self, name:str, address:str, email:str, DoB:str, affiliation:str, faculty_num=str):
        #reuse parent's init function
        super().__init__(name, address, email, DoB, affiliation)
        #Faculty-specific init
        self.faculty_num = faculty_num
        self.advisees = []
        self.courses_teaching = []
        self.infoList +=[self.faculty_num, self.advisees, self.courses_teaching]

    def switch_affiliation(self, new_affiliation:str):
        print('faculty', self.name, 'changes affiliation from', self.affiliation, 'to', new.affiliation)
        self.affiliation = new.affiliation

    
a = Member('Donghyun Kim', 'SNU-Gis/LBS', 'kaikim98@snu.ac.kr', '0926', 'Civil engineering')
print(type(a))
a.printinfo()
print(a)
b = Student('Keondo Park', 'SNU-GSDS', 'asdf@snu.ac.kr', '0101', 'GSDS', '2020-11111')
print(type(b))
b.printinfo()
c = Faculty('HyungSin Kim')