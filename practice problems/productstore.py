class Product:
    count=0

    def __init__(self,name,price):
        self.name=name
        self.price = price
        Product.count+=1

    def get_info(self):     #Instance Method
        print(f"price of {self.name} is Rs.{self.price}")

    @classmethod
    def get_count(cls):
        print(f"Total Products In store ={cls.count}")

    @staticmethod
    def calc_discount(price,discount):
        print(f"Discounted Price={price-(price*discount/100)}")

p1=Product("Phone",10_000)
p2=Product("Laptop",50_000)
p3=Product("phone",10)

p1.calc_discount(p1.price,12)