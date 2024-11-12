def findMaxSum(arr, k):
    n = len(arr)
    curr_sum = 0

    for i in range(k):
        curr_sum += arr[i]

    max_sum = curr_sum

    for i in range(k, n):
        curr_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum, curr_sum)

    return max_sum




arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4


print(findMaxSum(arr, k))