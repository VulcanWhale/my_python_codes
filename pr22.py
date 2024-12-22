# python program to Display the powers of 2 using anonymous function
# i will use lambda function iin this program

def power(t):
    res = list(map(lambda x: 2**x, range(t)))

    for i in range(t):
        print("2 to the power of ", i, "is", res[i])


t = int(input("Pleasse enter the number of terms you want: "))
power(t)