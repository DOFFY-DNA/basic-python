class Laptop:
    storage_type="ssd"

    def __init__(self,RAM,storage):
        self.RAM=RAM
        self.storage=storage

    def get_info(self): #instance Method
        print(f"Laptop has {self.RAM} RAM And {self.storage} {self.storage_type}")

l1=Laptop("16gb","512gb")
l2=Laptop("16gb","1TB")

l1.get_info()
l2.get_info()