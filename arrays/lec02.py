 
def reverse_array(arr, start, end):
    diff = end - start
    for i in range(diff//2 + 1):
        arr[start+i], arr[end-i] = arr[end-i], arr[start+i] 


def rotate_array_by_d_times(arr, n, d):
    d = d%n
    reverse_array(arr, 0, d-1)
    reverse_array(arr, d, n-1)
    reverse_array(arr, 0, n-1)


arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]
d = 4
n = len(arr)

rotate_array_by_d_times(arr, n, d)
print(arr)