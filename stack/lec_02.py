
def prevSmallerEle(arr):
    res = []

    st = []
    for i in range(len(arr)):
        while st and st[-1] <= arr[i]:
            st.pop()

        if st:
            res.append(st[-1])
        else:
            res.append(-1)
        
        st.append(arr[i])
    
    return res

arr = [5, 12, 6, 9, 18, 14, 2, 7]
print(arr)
print(prevSmallerEle(arr))