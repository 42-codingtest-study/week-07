# 소수의 곱
# https://www.acmicpc.net/problem/2014

import heapq	# 우선순위 큐와 비슷하게 사용할 수 있다
K, N = map(int, input().split())
pq = []
prime = list(map(int, input().split()))
[heapq.heappush(pq, i) for i in prime]	# 초기값 힙에담아줌
for i in range(N) :
    p1 = heapq.heappop(pq)	# 자동으로 가장 작은 값 뽑아짐
    for p2 in prime :
        heapq.heappush(pq, p1 * p2) # 기존 소수 값과 작은 값의 곱을 힙에 포함시켜줌
        if p1 % p2 == 0 :	# 이 조건이 만족한다면 힙에 중복되는 값이 있는거임
            break
print(p1)
