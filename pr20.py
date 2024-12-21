# program to print the armstrong numbers in a range

l = int(input("Please enter the lower limit: "))
u = int(input("Please enter the upper limit: "))

for n in range(l,u+1):
    l = len(str(n))
    sum = 0
    n2 = n

    while n2>0:
        d = n2 % 10
        sum += d ** l
        n2 //= 10
    if n == sum:
        print(n)
        