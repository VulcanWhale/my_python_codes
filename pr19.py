# program for armstrong number
"""An Armstrong number (also known as a narcissistic number or pluperfect digital invariant) 
is a number that is equal to the sum of its own digits each raised to the power of the number of digits."""

def armstrong(n):
    t_sum = 0
    l = len(str(n))

    t_sum = sum(n ** l for i in str(n))

    return t_sum == n

n = int(input("Please enter a number: "))

if armstrong(n):
    print(f"{n} is an armstrong number.")
else:
    print(f"{n} is not an armstrong number.")