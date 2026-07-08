u_name=input("Enter The Username :")
password=input("Enter the password :")

if u_name=="admin" and password=="pass":
    print("You Haved login")
elif u_name!="admin":
    print("Wrong Username")
else :
    print("Wrong Password")