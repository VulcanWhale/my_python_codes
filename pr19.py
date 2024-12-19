# program for armstrong number
"""An Armstrong number (also known as a narcissistic number or pluperfect digital invariant) 
is a number that is equal to the sum of its own digits each raised to the power of the number of digits."""

n = int(input("Please enter a number: "))

def armstrong(n):
    t_sum = 0
    l = len(str(n))

    t_sum = sum(n ** l for i in n)

    return t_sum == n


