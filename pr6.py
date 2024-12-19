#print(f"the swapped value of x is: { (x := float(input('Please enter the value for x: '))), (y := (float(input('please enter the value for y: '))))[1]}, y = {(x, y := y, x)[0]} ")


x = int(input("Enter value for x: "))
y = int(input("Enter value for y: "))

print(f"After swapping: x = {(x, y := y, x)[1]}, y = {x}")

