# For constructor you can create only one constructor for each class if you 
# multiple constructors for each class The last one will be valid means only the last one will be run

class Student:
    def __init__(self,name, cgpa): #Parameterized constructor
        self.name=name
        self.cgpa=cgpa
    
    def get_cgpa(self):
        return self.cgpa

stud1=Student("DOFFY",9.0)
stud2=Student("LUFFY",8.0)
stud3=Student("NAMI",9.9)
stud4=Student("ZORO",9.5)

print(f"{stud1.name} has cgpa={stud1.get_cgpa()}")
print(f"{stud2.name} has cgpa={stud2.get_cgpa()}")
