from collections import deque

input_count = int(input())
input_values = input().split()

storage = deque(enumerate(input_values))
answer = []

while storage:

    idx, value = storage.popleft()
    answer.append(idx + 1)
    if (int(value) > 0):
        storage.rotate( -(int(value) - 1))
    else:
        storage.rotate( -(int(value)))

# [Error]
# RuntimeError: deque mutated during iteration

# [Code]
# for idx, value in storage:
#     answer.append(idx + 1)
#     storage.rotate(-int(value))
#     storage.popleft()

# [Issue]
# Deque size cannot be changed during iteration

print(' '.join(map(str, answer)))

# [KeyWord]

# how to casting
# enumerate()
# depue()
# init list
# split()
# join()
# map()
