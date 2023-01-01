import sys, heapq
from collections import deque
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a!=b:
        if cost[a] <= cost[b]:
            parent[b] = a
        else:
            parent[a] = b


n,m,k = map(int,input().split())
cost = [0]+list(map(int,input().split()))
parent = [i for i in range(n+1)]
tot = 0

for _ in range(m):
    v,w = map(int,input().split())
    if v==w:
        continue
    union_parent(parent, v, w)

for idx, root in enumerate(parent):
    if idx == root:
        tot += cost[idx]

if tot <= k:
    print(tot)
else:
    print("Oh no")