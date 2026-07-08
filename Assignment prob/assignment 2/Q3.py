def print_digits(n):
    while n > 0:
        digit = n % 10      # get last digit
        print(digit)
        n = n // 10         # remove last digit
    return n

print_digits(312)