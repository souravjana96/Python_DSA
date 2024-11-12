def bubble_sort(arr):
    n = len(arr)
    for s in range(n):
        swap = 0
        for j in range(0, n-1-s):
            if arr[j][1] > arr[j+1][1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap += 1
        if swap == 0:
            return


people = [
    ('Alice', 30), 
    ('Bob', 25),
    ('Charlie', 30),
    ('David', 25),
    ('Eve', 35),
    ('Smith', 25),
]

# Sort by age
bubble_sort(people)
print(people)