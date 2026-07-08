salary=int(input("Enter The Salary :"))

if(salary<30000):
    tax=(salary*5)/100
    print("The Final Tax is :",tax)
elif(salary<=70000):
    tax=(salary*15)/100
    print("The Final Tax is :",tax)
elif(salary>70000):
    tax=(salary*25)/100
    print("The Final Tax is :",tax)

