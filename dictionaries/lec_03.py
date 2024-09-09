def find_palindrome_permutation(str):
    dic1 = {}
    for char in str:
        dic1[char] = dic1.get(char, 0) + 1

    
    count = 0
    for key, val in dic1.items():
        if val%2 != 0:
            count += 1
    
    return count <= 1

str = 'hello'
res = find_palindrome_permutation(str)
print(res)