# Assigning Default Value
#Also Non Default argument should come first like (a,b=3) a is non default argument(value) and b is Default argument(value)
def sum (a,b=3): #Here b is GIven Default Value
    return a+b

print(sum(5,6))
print(sum(5))