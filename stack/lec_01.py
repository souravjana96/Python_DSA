from collections import deque

st = deque()

st.append(10)
st.append(20)
st.append(30)
st.append(40)

# print(st)
st.pop()
st.pop()
st.pop()
st.pop()

if st:
    print(st[-1])
    st.pop()
else:
    print('The stack is empty')



