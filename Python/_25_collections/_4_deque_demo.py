# deque

# it is open at both the ends

from collections import deque

deque_obj = deque([1,2,3,4,5])
print(deque_obj)

deque_obj.append(100)
print(deque_obj)

deque_obj.appendleft(200)
print(deque_obj)

deque_obj.extendleft([7,8,9])
print(deque_obj)