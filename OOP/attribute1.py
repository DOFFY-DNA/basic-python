# Class and Instance Attribute

class Student:
    college_name="ABC College"  #class

    def __init__(self,name,gpa):
        self.name=name      #Instance
        self.gpa=gpa

stu1=Student("DOFFY", 9.2)

print(stu1.name)
print(stu1.college_name)     #This is Used to run from instance Attribute
#print(Student.college_name) #This is Used to run from Class Attribute