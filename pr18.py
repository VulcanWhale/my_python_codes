#print the fibonacci sequence upto a certain numbers

n = int(input('Please enter the upper limit for the sequence: '))

n1,n2 = 0,1

if n == 0:
    print(0)
elif n==1:
    print(1)
else:
    for i in range(2,n+1):
        print(n1)
        t = n1+n2
        n1 = n2
        n2 = t
        i = i+1
        
