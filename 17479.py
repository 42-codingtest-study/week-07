# 정식당
# https://www.acmicpc.net/problem/17479

import sys

input = sys.stdin.readline

A, B, C = map(int, input().split())
normal = dict()
special = dict()
service = set()
n_price = 0
s_price = 0
spec_cnt = 0
serv_cnt = 0
for _ in range(A) :
    menu, price = input().split()
    normal[menu] = int(price)
for _ in range(B) :
    menu, price = input().split()
    special[menu] = int(price)
for _ in range(C) :
    service.add(input().replace("\n", ""))	# 계속 안되길래 보니까 개행이 포함되어있었다..

for _ in range(int(input())) :
    menu = input().replace("\n", "")
    if str(menu) in normal.keys() :
        n_price += normal[menu]
    elif menu in special.keys() :
        s_price += special[menu]
        spec_cnt += 1
    else :
        serv_cnt += 1

total = "Okay"
if n_price < 20000 and spec_cnt > 0 :
    total = "No"
else :
    if n_price + s_price < 50000 and serv_cnt > 0 :
        total = "No"
    elif serv_cnt > 1 :		# 보너스 메뉴는 하나만 가능
        total = "No"

print(total)