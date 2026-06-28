class Student:
    def msg(self):
        print("this is class program")
    def student_info(self):
        print(self.name,self.age)
    # default constructor
    def __init__(self):
        print("I will run without object")
    # parametrized constructor
    def __init__(self,name,age):
        self.name = name
        self.age = age



# s=Student() # creating object of student class
# Student.msg(s)
# s.msg()
s2=Student('Ram',20)
s2.student_info()
