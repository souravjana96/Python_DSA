# def counvert_string_into_camel_case(str):
#     res_str = str[0].upper()
#     n = len(str)
#     for i in range(1, n):
#         if(str[i-1] == ' ' ):
#             res_str = res_str + str[i].upper()
#         else:
#             res_str = res_str + str[i]
#     return res_str

# def counvert_string_into_camel_case(str):
#     temp_list = str.split(" ")
#     for i in range(len(temp_list)):
#         temp_list[i] = temp_list[i].capitalize()
    
#     return ' '.join(temp_list)
    

# str = 'Hi there i am sourav'
# print(str)
# print(counvert_string_into_camel_case(str))



colors = ["Red", "Blue", "Green", "Yellow"]
colors.reverse()