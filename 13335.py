# 트럭
# https://www.acmicpc.net/problem/13335

from collections import deque

n, w, L = map(int, input().split())
trucks = deque(list(map(int, input().split())))
bridge = deque([0 for _ in range(w - 1)])
bridge.append(trucks.popleft())		# 초기 값 설정
time = 1
while trucks :
    if sum(bridge) - bridge[0] + trucks[0] <= L :	# 맨 앞 트럭이 들어가면 다리의 첫번째 트럭이 빠져야하니까
        bridge.popleft()
        bridge.append(trucks.popleft())
    else :	# 트럭이 못들어가면 0을 추가
        bridge.popleft()
        bridge.append(0)
    time += 1
while sum(bridge) != 0 :	# 만약 다리에 아직 트럭이 남아있다면 빼줘야함
    bridge.popleft()
    time += 1
print(time)