# 친구비
# https://www.acmicpc.net/problem/16562

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
N, M, k = map(int, input().split())
prices = list(enumerate(map(int, input().split()), start = 1))	# 인덱스 저장해놓고
prices.sort(key = lambda x : x[1])	# 친구비가 저렴한 순서대로 정렬
prices = [(0, 0)] + prices	# 인덱스 맞춰주기 위해 하나 추가
friends = [[] for _ in range(N + 1)]
for _ in range(M) :
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

total = 0
visited = [0 for _ in range(N + 1)]

def dfs(friend) :	# (1, 10)
    if len(friends[friend[0]]) == 0 :
        return
    for next in friends[friend[0]] :	# 친구 관계 파악
        if visited[next] == 0 :		# 친구의 친구인데 아직 친구비 안냈다면
            visited[next] = 1		# 친구비 안내고
            for i in range(len(prices)) :	# 인덱스 찾아준다
                if prices[i][0] == next :	# 맞는 인덱스라면 재귀
                    dfs(prices[i])

for i in range(1, len(prices)) :	# 모든 친구들을 다 검색해야한다.
    if visited[prices[i][0]] == 0 :	# 친구비 안냈다면 dfs 시작
        total += prices[i][1]
        visited[prices[i][0]] = 1
        dfs(prices[i])

if k - total < 0 :
    print("Oh no")
else :
    print(total)