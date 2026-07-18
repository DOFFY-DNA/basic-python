# IN Ploymorphism where Poly means many and morph means form i.e Many Forms

class Teacher:
    def get_designation(self):
        print("designation=Teacher")

class Accountant():
    def get_designation(self):
        print("designation=Accountant")

t1=Teacher()
t1.get_designation()

acc1=Accountant()
acc1.get_designation()