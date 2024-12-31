# program to convert decimal number to binary number using recursion

def dtb(num):
    if num > 1:
        dtb(num // 2)
    print(num % 2, end = ' ')

n = int(input("Please enter the decimal number: "))

dtb(n)
print()