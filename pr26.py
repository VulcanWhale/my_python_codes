# Python program to find the HCF of two numbers 

def gcd(a,b):
    if a>b:
        small = b
    else:
        small = a
    
    for i in range(1,small+1):
        if ((a % i == 0) and (b % i == 0)):
            r = i
    return r

num1 = int(input("Please enter the 1st number: "))
num2 = int(input("Please enter the 2nd number: "))

res = gcd(num1,num2)

print(f"the hcf/gcd of {num1} and {num2} is {res}.")