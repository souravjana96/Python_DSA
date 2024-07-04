arr1 = []
for i in range(0, 4):
    arr1.append(int(input(f'Enter number {i+1}:\n')))

print(arr1)
arr1.sort(reverse=False)
print(arr1)