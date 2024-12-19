n = int(input("Please enter a number: "))


def fact(n):
    if n < 0 :
        print("Please enter a positive integer.")
    elif n == 0:
        print("the factorial of 0 is 1.")
    else:
        f = 1
        for i in range(1,n+1):
            f = f*i
        print(f"the factorial of {n} is {f}")

fact(n)