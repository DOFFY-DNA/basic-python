# Initializing self constructor and passing name

class Student:
    def __init__(self,name): #Parameterized constructors
        self.name=name
    

stud1=Student("DOFFY")
stud2=Student("LUFFY")
stud3=Student("NAMI")
stud4=Student("ZORO")

print(stud1.name)
print(stud2.name)
print(stud3.name)
print(stud4.name)