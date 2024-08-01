
# def find_diagonal_sum(mat, n):
#     pd_sum = 0
#     sd_sum = 0
#     for i in range(n):
#         for j in range(n):

#             if(i == j):
#                 pd_sum += mat[i][j]
            
#             if( i == n-1-j):
#                 sd_sum += mat[i][j]

#     print('Principal Diagonal sum =', pd_sum)
#     print('Secondary Diagonal sum =', sd_sum)


def find_diagonal_sum(mat, n):
    for i in range(n):
        for j in range(i+1, n):
            mat[i][j], mat[j][i] = mat[i][j], mat[j][i]


mat = [ [1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = 3

# find_diagonal_sum(mat, n)

for i in range(n):
        for j in range(i+1, n):
            mat[i][j], mat[j][i] = mat[i][j], mat[j][i]

for i in range(n):
    for j in range(n):
        print(mat[i][j], end=' ')
    print()
