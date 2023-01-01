# _*_ coding: utf-8 _*_
#백준 2346 > 풍선 터트리기

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque(enumerate(map(int, input().split())))
a = []

while q:
    idx, paper = q.popleft()
    a.append(idx + 1)

    if paper > 0:
        q.rotate(-(paper - 1))
    elif paper < 0:
        q.rotate(-paper)

print(' '.join(map(str, a)))