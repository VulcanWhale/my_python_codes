#python program to check if a number is even or odd

n = float(input("please enter a number: "))

def oddeven(n):
    if n == 0:
        print("You have entered zero.")
    elif n % 2 == 0:
        print(str(n) +"is an even number.")
    else:
        print(str(n) + "is an odd number.")

oddeven(n)    