#python program to check if a number is positive, negative or zero

def check():
    n = float(input('please enter a number: '))
    
    if n == 0:
        print("you have entered zero.")
    elif n > 0:
        print("you have enterd a positive number")
    else:
        print("you have entered a negative number.")

    
check()