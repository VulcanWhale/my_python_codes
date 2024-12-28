# making a simple calculator application in python

def inp():
    a = float(input('Enter the first number: '))
    b = float(input('Enter the second number: '))
    return a,b


print("This is a simple calculator. \nPlease choose an option given below: \n1>ADD\n2>SUBTRACT\n3>MULTIPLICATION\n4>DIVISION\n5>EXIT")
c = int(input("Enter your option: "))

while True:
    if c == 5:
        print("Thank you!")
        break

    a,b = inp()
