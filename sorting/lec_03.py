def bubble_sort(arr):
    n = len(arr)

    for s in range(n):
        swap = False
        for j in range(n-1-s):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
        if not swap:
            break

arr = [-2, 45, 0, 11, -9]
bubble_sort(arr)
print('Sorted Array', arr)
