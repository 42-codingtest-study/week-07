#핸들이 고장난 에잇톤 트럭
import sys
input = sys.stdin.readline

n, w, l = map(int, input().split())
trucks = list(map(int, input().split()))

bridge = [0] * w
time = 0

while bridge:
	time += 1
	bridge.pop(0)
	if trucks:
		if sum(bridge) + trucks[0] <= l:
			bridge.append(trucks.pop(0))
		else:
			#트럭있는데 못올리면 일단 0으로 채움
			bridge.append(0)
print(time)