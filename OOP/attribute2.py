# Class and Instance Attribute
#Here Instance have Higher priority Attribute so it will print value of PI From Instance and class has lower priority.

class Student:
    college_name="ABC College"  #class
    PI =3.1

    def __init__(self,name,gpa):
        self.name=name      #Instance
        self.gpa=gpa
        self.PI=3.14

stu1=Student("DOFFY", 9.2)

print(stu1.PI)
print(Student.PI) #If we call using class name it will return value of PI From Class

