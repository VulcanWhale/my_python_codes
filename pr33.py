# program to calculate the sum of natural numbers upto a limit using recursion

def rec_sum(n):
    if n <= 1:
        return n
    else:
        return n + rec_sum(n-1)

num = int(input("Please enter a number: "))

if num < 0:
    print("Please enter a positive number.")
else:
    print(f"The sum of natural numbers upto {num} is = ", rec_sum(num))