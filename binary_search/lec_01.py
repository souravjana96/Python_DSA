  
def lowerBound(arr, target):
    l = 0
    h = len(arr) - 1

    while l <= h:
        m = l + (h-l)//2

        if arr[m] < target:
            l = m + 1
        else:
            h = m - 1
    return l

def upperBound(arr, target):
    l = 0
    h = len(arr)-1
    while l <= h:
        m = l + (h-l)//2

        if arr[m] <= target:
            l = m+1
        else:
            h = m-1
    
    return l


arr = [1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 5, 6, 6, 6]

lb = lowerBound(arr, 12)
ub = upperBound(arr, 12)
print("Lower Bound of", 12, 'is:', lb)
print("Upper Bound of", 12, 'is:', ub)

