# program for armstrong number
"""An Armstrong number (also known as a narcissistic number or pluperfect digital invariant) 
is a number that is equal to the sum of its own digits each raised to the power of the number of digits."""

def armstrong(n):
    l = len(str(n))
    sum = 0
    n2 = n

    while n2>0:
        d = n2 % 10
        sum += d ** l
        n2 //= 10

    return sum == n


n = int(input("Enter a number: "))

if armstrong(n):
    print(f"{n} is an armstrong number.")
else:
    print(f"{n} is not an armstrong number.")