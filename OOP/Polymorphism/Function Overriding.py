# IN Ploymorphism where Poly means many and morph means form i.e Many Forms

class Employee:
    def get_designation(self):
        print("designation=Employee")

class Teacher(Employee):
    def get_designation(self):
        print("designation=Teacher")

t1=Teacher()
t1.get_designation()