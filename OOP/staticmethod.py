# We where Using self as parameter for instance but for static we cannot use instance,class
#And Decorater is also used for defining or saying using that method and it is given in @staticmethod

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

    @staticmethod
    def calc_discount(price,discount):
        final_price=price-(discount*price/100)
        print(f"Discounted price={final_price}")

l1=Laptop("16gb","512gb")

l1.calc_discount(40_00,10 )