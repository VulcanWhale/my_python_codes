import cmath

a = eval(input('Please enter the coefficient of a: '))
b = eval(input('Please enter the coefficient of b: '))
c = eval(input('Please enter the coefficient of c: '))


#solution1 = (-b + cmath.sqrt(b**2 - 4 * a * c)) / (2 * a)
#solution2 = (-b - cmath.sqrt(b**2 - 4 * a * c)) / (2 * a)


print(f"The solutions for this quadratic equation are {(-b + cmath.sqrt(b**2 - 4 * a * c)) / (2 * a)} and {(-b - cmath.sqrt(b**2 - 4 * a * c)) / (2 * a)}")
