# program to print the armstrong numbers in a range


def armrange(l,u):
    for n in range(l,u+1):
        le = len(str(n))
        sum = 0
        n2 = n

        while n2>0:
            d = n2 % 10
            sum += d ** le
            n2 //= 10

        if n == sum:
            print(n)

lower = int(input("Please enter the lower limit: "))
upper = int(input("Please enter the upper limit: "))

armrange(lower,upper)