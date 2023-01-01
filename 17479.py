# _*_ coding: utf-8 _*_
#백준 17479 > 정식당

import sys

A, B, C = map(int, sys.stdin.readline().split())

dt_A = dict()
dt_B = dict()
li_C = list()

for i in range(A):
    menu = sys.stdin.readline().split()
    dt_A[menu[0]] = int(menu[1])

for i in range(B):
    menu = sys.stdin.readline().split()
    dt_B[menu[0]] = int(menu[1])

for i in range(C):
    li_C.append(sys.stdin.readline().rstrip())

N = int(sys.stdin.readline())
A_price = 0
B_price = 0
B_cnt = 0
C_cnt = 0
for i in range(N):
    menu = sys.stdin.readline().rstrip()
    if menu in dt_A.keys():
        A_price += dt_A[menu]
    elif menu in dt_B.keys():
        B_price += dt_B[menu]
        B_cnt += 1
    else:
        C_cnt += 1

res = "Okay"
if A_price < 20000 and B_cnt > 0:
    res = "No"
else:
    if A_price + B_price < 50000 and C_cnt > 0:
        res = "No"
    elif C_cnt > 1:
        res = "No"

print(res)