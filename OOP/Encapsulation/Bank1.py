# Encapsulation is the process of binding class and data in single uint 
# In data encapsulation we use public, private, protected 
# For Protected we use _name and private we use __name 
# getter and setter are used for accessing private data for encapsulation


class BankAccount:
    def __init__(self,name,balance):
        self.name=name #Public
        self.__balance = balance #Private - data mangling

    def get_balance(self):  #getter
        return self.__balance
    
    def set_balance(self,newBalance): #setter
        self.__balance=newBalance

acc1=BankAccount("DOFFY", 9000_0000)

acc1.set_balance(200_000)
print(acc1.name,acc1.get_balance())