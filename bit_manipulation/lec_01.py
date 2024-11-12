# def checkKthBit(num, k):
#     if num & (1 << k) == 0:
#         print('Kth bit is Not Set bit')
#     else:
#         print('Kth bit is Set bit')


# num = 10

# checkKthBit(num, 3)




def countSetBit(num):
    count = 0

    while num > 0:
        if num & 1 != 0:
            count += 1
        
        num = num >> 1
    
    return count


num = 0

print(countSetBit(num))