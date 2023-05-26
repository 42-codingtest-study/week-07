n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))

bridge = [0] * w
unit_time, weight = 0

while trucks:
    unit_time += 1
    bridge.pop(0)
    if (sum(bridge) + trucks[0] <= L):
        bridge.append(trucks.pop(0))
    else:
        bridge.append(0)

print(unit_time + w)

# [Error Code]

# for idx in range(0, n):
#     sum = truck_list[idx]
#     for jdx in range(idx + 1, n):
#         sum += truck_list[jdx]
#         if (sum > L):
#             break
#         save_time += 1  

# let's avoid `Hard Coding`

# [KeyWord]

# sum()
# how to get list value
