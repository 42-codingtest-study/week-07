#준석아 국민 835002-04-222604
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
costs = [0] + list(map(int, input().split()))
friends = [i for i in range(n + 1)]

def find(x):
    if x == friends[x]:
        return x
    else:
        if costs[friends[x]] > costs[x]:
            costs[friends[x]] = costs[x]
        else:
            costs[x] = costs[friends[x]]
        friends[x] = find(friends[x])
        return friends[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if costs[x] > costs[y]:
        costs[x] = costs[y]
    else:
        costs[y] = costs[x]
    if x < y:
        friends[y] = x
    else:
        friends[x] = y

#친구 맺기
for i in range(m):
    a, b = map(int, input().split())
    union(a, b)

#최소비용 친구 찾기
tmp = set()
money = 0
for i in range(1, n + 1):
    a = find(i)
    if a in tmp:
        continue
    else:
        tmp.add(a)
        money += costs[a]

if money <= k:
    print(money)
else:
    print("Oh no")