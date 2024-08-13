# def reverse_string(str):
#     res_str = ''
#     for char in str:
#         res_str = char + res_str
    
#     return res_str

def reverse_string(str):
    return str[::-1]

str = 'abcd'
rev_str = reverse_string(str)
print(rev_str)