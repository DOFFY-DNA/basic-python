def sum_of_digits(n):
    total = 0
    
    while n > 0:
        digit = n % 10   # get last digit
        total += digit
        n = n // 10      # remove last digit
        
    return total

print(sum_of_digits(312))