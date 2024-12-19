#python program to print the multiplication table

n = int(input("Please enter a number: "))

def table(n):
    if n == 0:
        print("Please enter a valid integer!")
    else:
        for i in range(1,11):
            print(n, " * ", i, " = ", n*i)
table(n)