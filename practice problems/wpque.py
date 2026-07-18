name=input("What is Your Name :")
brith_year=int(input("What is Your Brith Year :"))
current_year=int(input("What is Your Current Year :"))
print("Hello",name,"!")

age= current_year-brith_year
print("You are",age,"Years Old")
if(age<=12):
    print("Category:Child")
elif(age<=19):
    print("Category:Teenager")
elif(age<=59):
    print("Category:Adult")
#elif(age>=60):
   # print("Category:Sr.C")
else:
    print("Category:Sr.C")