def tran(matrix,n):
    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[j][i]
N1 = 4
matrix1 = [
    [1, 1, 1, 1],
    [2, 2, 2, 2],
    [3, 3, 3, 3],
    [4, 4, 4, 4]
]
tran(matrix1, N1)
print(matrix1)

N2 = 2
matrix2 = [
    [1, 2],
    [-9, -2]
]
tran(matrix2, N2)
print(matrix2)            