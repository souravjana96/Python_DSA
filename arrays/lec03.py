def find_element_in_array(arr, target):
    for ele in arr:
        if(ele == target):
            return True
    return False

arr = [4, 2, 7, 5, 19]
target = 7
res = find_element_in_array(arr, target)
print(res)