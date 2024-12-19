#y = int(input("please enter a year: "))

def leap(y):
    if (y % 400 == 0) and (y % 100 == 0):
        print("{0} is a leap year".format(y))
    elif (y % 4 == 0) and (y % 100 != 100):
        print("{0} is a leap year".format(y))
    else:
        print("{0} is not a leap year".format(y))

leap(y = int(input("please enter a year: ")))