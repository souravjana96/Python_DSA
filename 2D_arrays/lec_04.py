
def spiral_traversal(mat, m, n):

    left = 0
    right = n-1
    top = 0
    bottom = m-1
    count = 0
    res = []

    while(count < m*n):
        if(count >= m*n):
            break
        for j in range(left, right+1):
            i = top
            res.append(mat[i][j])            
            count += 1

        if(count >= m*n):
            break
        for i in range(top+1, bottom+1):
            j = right
            res.append(mat[i][j])            
            count += 1

        if(count >= m*n):
            break
        for j in range(right-1, left-1, -1):
            i = bottom
            res.append(mat[i][j])            
            count += 1

        if(count >= m*n):
            break
        for i in range(bottom-1, top, -1):
            j = left
            res.append(mat[i][j])            
            count += 1

        left += 1
        right -= 1
        top += 1
        bottom -= 1

    return res


def print_mat(mat):
    for row in mat:
        for ele in row:
            print(ele, end=' ')
        print()
    print()

mat = [[1, 2, 3, 4, 17], [5, 6, 7, 8, 18], [9, 10, 11, 12, 19], [13, 14, 15, 16, 20], [21, 22, 23, 24, 25]]
m = 5
n = 5


print_mat(mat)
ans = spiral_traversal(mat, m, n)
print(ans)
