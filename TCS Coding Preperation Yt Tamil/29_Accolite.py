def matrix_check(matx,n,m,x):
    i,j=0,m-1
    while i<n and j>=0:
        if matx[i][j]==x:
            return 1
        elif matx[i][j]>x:
            j-=1
        else:
            i+=1
    return 0
N1, M1 = 3, 3
mat1 = [
    [3, 30, 38],
    [44, 52, 54],
    [57, 60, 69]
]
X1 = 62
print(matrix_check(mat1, N1, M1, X1))  # Output: 0

# Example 2
N2, M2 = 1, 6
mat2 = [
    [18, 21, 27, 38, 55, 67]
]
X2 = 55
print(matrix_check(mat2, N2, M2, X2))  # Output: 1        
                















# def matSearch(mat, N, M, X):
#     # Start from the top-right corner of the matrix
#     i, j = 0, M - 1
    
#     # Traverse the matrix
#     while i < N and j >= 0:
#         if mat[i][j] == X:
#             return 1  # Element found
#         elif mat[i][j] > X:
#             j -= 1  # Move left
#         else:
#             i += 1  # Move down
    
#     return 0  # Element not found

# # Example 1
# N1, M1 = 3, 3
# mat1 = [
#     [3, 30, 38],
#     [44, 52, 54],
#     [57, 60, 69]
# ]
# X1 = 62
# print(matSearch(mat1, N1, M1, X1))  # Output: 0

# # Example 2
# N2, M2 = 1, 6
# mat2 = [
#     [18, 21, 27, 38, 55, 67]
# ]
# X2 = 55
# print(matSearch(mat2, N2, M2, X2))  # Output: 1
