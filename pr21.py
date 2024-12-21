# python program to print the sum of natural numbers upto a limit 
# we are going to takr the limit as input from the user here

def sumnat(n):
    sum,i = 0,1
    while i<=n :
        sum += i
        i +=1
    return sum


n = int(input("Please enter a number: "))
print("the sum is: ", sumnat(n))