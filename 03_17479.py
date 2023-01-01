import sys

a, b, c = map(int, sys.stdin.readline().split())

menu_a = {}
menu_b = {}
menu_c = []

for i in range(a):
    menu = sys.stdin.readline().split()
    menu_a[menu[0]] = int(menu[1])

for i in range(b):
    menu = sys.stdin.readline().split()
    menu_b[menu[0]] = int(menu[1])

for i in range(c):
    menu = sys.stdin.readline().rstrip()
    menu_c.append(menu)

order_count = int(sys.stdin.readline().rstrip())
sum_a = 0
sum_b = 0
b_count = 0
c_count = 0

for i in range(order_count):
    order = sys.stdin.readline().rstrip()
    # if menu_a.keys(order):
    if order in menu_a.keys():
        sum_a += menu_a[order]
    elif order in menu_b.keys():
        sum_b += menu_b[order]
        b_count += 1
    else:
        c_count += 1
        
if sum_a < 20000 and b_count:
    print("No")
elif sum_a + sum_b < 50000 and c_count:
    print("No")
elif c_count > 1:
    print("No")
else:
    print("Okay")


# [Issue]

# `&` is not `and` !!!
# `&&` is `and` in the python

# [KeyWord]

# dict
# sys.stdin.readline()
# rstrip()
