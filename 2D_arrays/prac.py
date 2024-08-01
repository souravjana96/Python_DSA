# def spiral_print(mat, m, n):
#     left = 0
#     right = n-1
#     top = 0
#     bottom = m-1
#     count = 0
#     while(count < m*n):
#         if(count >= m*n):
#             return
#         for j in range(left, right+1):
#             print(mat[top][j], end=' ')
#             count += 1
            
#         if(count >= m*n):
#             return
#         for i in range(top+1, bottom+1):
#             print(mat[i][right], end=' ')
#             count += 1
        
#         if(count >= m*n):
#             return
#         for j in range(right-1, left-1, -1):
#             print(mat[bottom][j], end=' ')
#             count += 1
            
#         if(count >= m*n):
#             return
#         for i in range(bottom-1, top, -1):
#             print(mat[i][left], end=' ')
#             count += 1
                
#         left += 1
#         right -= 1
#         top += 1
#         bottom -= 1


# m = 4
# n = 5
# mat = [[1,2,3, 4, 17], [5, 6, 7, 8, 18], [9, 10, 11, 12, 19], [13, 14, 15, 16, 20]]

# for row in mat:
#     for ele in row:
#         print(ele, end=' ')
#     print()

# # print()
# spiral_print(mat, m, n)





