# program to calculate the factorial of a given number using recursion

def rec_fac(n):
    if n == 1:
        return n
    else:
        return n * rec_fac(n-1)
    
num = int(input("Please enter a number: "))

if num < 0:
    print("factorial is not possible for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print(f'The factorial of {num} is', rec_fac(num))