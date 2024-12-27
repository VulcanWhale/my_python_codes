# program to find the factor of a number

n = int(input("Please enter a number: "))
i = 1
while i <= n/2:
    if n % i == 0:
        print(f"{i} is a factor of {n}")
    i += 1
print(f"{n} is a factor of {n} itself.")