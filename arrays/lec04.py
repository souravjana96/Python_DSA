# def find_max(arr):
#     n = len(arr)
#     max = arr[0]
#     for i in range(1, n):
#         if(arr[i] > max):
#             max = arr[i]
#     return max

# def find_min(arr):
#     n = len(arr)
#     min = arr[0]
#     for i in range(1, n):
#         if(arr[i] < min):
#             min = arr[i]
#     return min

# arr = [45, 22, -3, 156, 12, 73, -15, -34]
# min_val = find_min(arr)
# print(min_val)



def find_kth_max(arr, n, k):
    for j in range(k):
        max = j
        for i in range(j+1, n):
            if(arr[i] > arr[max]):
                max = i
        
        arr[j], arr[max] = arr[max], arr[j]
    
    return arr[k-1]

def find_kth_min(arr, n, k):
    for j in range(k):
        min = j
        for i in range(j+1, n):
            if(arr[i] < arr[min]):
                min = i

        arr[j], arr[min] = arr[min], arr[j]

    return arr[k-1]

arr = [45, 22, -3, 156, 12, 73, -15, -34]
n = len(arr)
k = 2
# res = find_kth_max(arr, n, k)
res = find_kth_min(arr, n, k)
print(res)