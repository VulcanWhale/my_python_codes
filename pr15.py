# program to print prime numbers in a range
import math


lb = int(input("please enter a lower bound: "))
ub = int(input("please enter an upper bound: "))

for i in range(lb, ub+1):
    if i > 1:
        for j in range(2, int(math.sqrt(i))+1):
            if i % j == 0:
                break
        else:
            print(i)