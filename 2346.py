#풍선 팡팡
import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
#인덱스와 원소로 이루어진 튜플 만듬 - 동시접근 가능
q = deque(enumerate(map(int, input().split())))
result = []

while q:
    idx, paper = q.popleft()
    result.append(idx + 1)

    if paper > 0:
		#리스트 회전시킬때 사용
		#pop한 이후이기때문에 +1 되어있어서 -1함
        q.rotate(-(paper - 1))
    elif paper < 0:
        q.rotate(-paper)

for ans in result:
	print(ans, end = ' ')