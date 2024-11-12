def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min = i
        for j in range(i, n):
            if arr[j][1] < arr[min][1]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]



people = [
    ('Alice', 30), 
    ('Bob', 25),
    ('Charlie', 30),
    ('David', 25),
    ('Eve', 35),
    ('Smith', 25),
]

# Sort by age

selection_sort(people)
print('Sorted Array', people)