def lcm(a,b):
    if a>b:
        greater = a
    else:
        greater = b

    while True:
        if((greater % a == 0) and (greater % b == 0)):
            res = greater
            break
        greater += 1
    return res

def inp():
    x = int(input("Please enter the 1st number: "))
    y = int(input("Please enter the 2nd number: "))
    
    res = lcm(x,y)
    print(f"The lcm of {x} and {y} is {res}.")

inp()
