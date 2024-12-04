
# queue = []

# queue.append(10)
# queue.append(20)
# queue.append(30)

# queue.pop(0)

# print(queue[0])




from collections import deque

queue = deque()


queue.append(10)
queue.append(20)
queue.append(30)


print(queue[0])

queue.popleft()

print(queue[0])
