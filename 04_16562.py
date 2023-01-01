import sys

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
        # return find(root[x])
    return root[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if cost[x] < cost[y]:
        root[y] = x
    else:
        root[x] = y

N, M, k = map(int, sys.stdin.readline().split())
root = [x for x in range(N + 1)]
cost = [0] + list(map(int, sys.stdin.readline().split()))

for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    union(x, y)

sum_cost = 0

for i in range(1, N + 1):
    if (root[i] == i):
        sum_cost += cost[i]

if (sum_cost > k):
    print("Oh no")
else:
    print(sum_cost)

# [KeyWord]

# union - find algorhithm
# root = [x for x in range(N + 1)]
