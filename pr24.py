#Python Program to Convert Decimal to Binary, Octal and Hexadecimal

n = int(input("Please enter a number: "))

binary = lambda x: bin(x)
octal = lambda x: oct(x)
hexadecimal = lambda x: hex(x)

print(f"The decimal value of {n} is:")
print(f"{binary(n)} in binary.")
print(f"{octal(n)} in octal.")
print(f"{hexadecimal(n)} in Hexadecimal.")