#python program to print the area of a triangle

print(f"The area of the triangle is {((((s := (a := float(input('Please enter the first side: '))) + (b := float(input('Please enter the second side: '))) + (c := float(input('Please enter the third side: ')))) / 2) * (s - a) * (s - b) * (s - c)) ** 0.5) :0.2f}")