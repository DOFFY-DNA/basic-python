# Simple Calculators

def calculator(a,b,op):
    if(op=="+"):
        s=a+b
    elif(op=="-"):
        s=a-b
    elif(op=="*"):
        s=a*b
    elif(op=="/"):
        s=a/b
    
    return s

op=input("Enter The Operation Symbol :")
a=int(input("Enter The Value of a :"))
b=int(input("Enter The Value of b :"))
print("The Arithmetic Operation is :",calculator(a,b,op))