# Queue FIFO

# Head and Tail

# En-Queue is used to add the elements
# De-Queue is used to delete the elements
from collections import deque

q = deque()

q.append('1st element')
q.append('2nd element')
q.append('3nd element')

print(q, '\n')

a = q.popleft()
print("the first popped elements is :", a)

b = q.popleft()
print("the second popped elements is :", b)

c = q.popleft()
print("the third popped elements is :", c)
