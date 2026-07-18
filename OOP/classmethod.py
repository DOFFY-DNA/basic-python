# We where Using self as parameter for instance but for class we are giving parameter as cls
#And Decorater is also used for defining or saying using that method and it is given in @classmethod

class Laptop:
    storage_type="ssd"

    def __init__(self,RAM,storage):
        self.RAM=RAM
        self.storage=storage


    @classmethod
    def get_storage_type(cls):
        print(f"Storage type= {cls.storage_type}")

    def get_info(self): #instance Method
        print(f"Laptop has {self.RAM} RAM And {self.storage} {self.storage_type}")

l1=Laptop("16gb","512gb")
l2=Laptop("16gb","1TB")

Laptop.get_storage_type() #Calling using class
l2.get_storage_type() # we can also call using object name