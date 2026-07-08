def calc_fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i  # fact=fact*i

    return fact

n=int(input("Enter The Number :"))
print(calc_fact(n))