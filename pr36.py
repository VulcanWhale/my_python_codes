# program to add two matrices

# defining the matrices

a = [[2,3,5],
     [4,27,12],
     [23,44,63]]

b = [[7,4,2],
     [34,33,11],
     [13,23,19]]

res = [[0,0,0],
       [0,0,0],
       [0,0,0]]


for i in (len(a)):
    for j in range(len(a[0])):
        res[i][j] = a[i][j] + b[i][j]

# printing the result
for r in res:
    print(r)