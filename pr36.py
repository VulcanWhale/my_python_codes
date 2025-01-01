# program to add two matrices

# defining the matrices

import ast
a = ast.literal_eval(input("Please enter the first matrix as nested list (3x3): "))

b = ast.literal_eval(input("Please enter the second matrix as nested list (3x3): "))


#a = [[2,3,5],[4,27,12],[23,44,63]]

#b = [[7,4,2],[34,33,11],[13,23,19]]

res = [[0,0,0],
       [0,0,0],
       [0,0,0]]


for i in range(len(a)):
    for j in range(len(a[0])):
        res[i][j] = a[i][j] + b[i][j]

# printing the result
for r in res:
    print(r)