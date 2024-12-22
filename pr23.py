#Python Program to Find Numbers Divisible by Another Number
"""we will take list as user input for storing the numbers to be divisible
next we will take a int input for dividing the numbers on the list.

here we will use filter() to filter the data and store the output on a list"""

lst = eval(input("Please enter a list of integers: "))
n = int(input("Please enter the divisor: "))


def div(n):
	return lambda x:(x % n == 0)

filtered_list = list(filter(div(n), lst))

for i in filtered_list:
	print(i, "is divisible by", n)