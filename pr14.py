import math
n = float(input("Please enter a number: "))

flag = False

if n == 0 or n == 1:
    print("not prime.")
elif n == 2:
    print("prime no.")
elif n > 2:
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n % i == 0:
            flag = True
        else:
            flag = False

if flag == True:
    print("not prime")
else:
    print("prime")
    