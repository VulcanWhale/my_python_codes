a = int(input("please enter the first number: "))
b = int(input("please enter the second number: "))
c = int(input("please enter the third number: "))

def large(a,b,c):
    if a>b and a>c:
        print("{0} is the largest among the three numbers.".format(a))
    elif b>a and b>c:
        print("{0} is the largest among the three numbers.".format(b))
    else:
        print("{0} is the largest number among three numbers.".format(c))

large(a,b,c)