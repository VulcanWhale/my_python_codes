# program to convert decimal number to binary number using recursion

def bin(num):
    if num > 1:
        bin(num // 2)
    print(n % 2, end = ' ')

n = int(input("Please enter the decimal number: "))

bin(n)
print()