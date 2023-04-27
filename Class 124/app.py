import numpy as np

array_1 = np.array([0,1,2,3,4,5])
print(array_1)

array_2 = np.array([[1,5,6],[9,3,91],[31,64,12],[93,43,12]]) #row, col
#print(array_2[3,1])

array_2[3,1] = 44
#print(array_2)

a = np.array([[1,3],[4,5]])
b = np.array([[3,0],[8,4]])

print(a)
print("_________")
print(b)

row = 2
col = 2

c = [[0,0],[0,0]]

for i in range(row):
    for j in range(col):
        c[i][j] = a[i][j] + b[i][j]

print(c)
print("-----------------------")

#multiplication of arrays
x = np.array([[1,9],[32,4],[23,8]])

n = 5
m = np.zeros([3,2]) 

for i in range(3): #rows
    for j in range(2): #columnb
        m[i][j] = n * x[i][j]

print(m)
print("------------------")
#substraction of arrays

arr1 = np.array([[3,4],[2,1],[7,6]])
arr2 = np.array([[7,2],[2,5],[9,2]])

result = np.zeros([3,2]) #row,col

for row in range(3):
    for col in range(2):
        result[row][col] = arr2[row][col] - arr1[row][col]

print(result)
