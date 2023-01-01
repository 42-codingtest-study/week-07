#영기야 영기야!!
import sys
input = sys.stdin.readline

normal = dict()
special = dict()
service = set()

normalPrice = 0
totalPrice = 0
serviceCnt = 0
specialCnt = 0

def setMenu(normal, special, service) :
    A, B, C = map(int, input().split(" "))
    for _ in range(A) :
        menu, price = input().rstrip().split(" ")
        normal[menu] = int(price)
    for _ in range(B) :
        menu, price = input().rstrip().split(" ")
        special[menu] = int(price)
    for _ in range(C) :
        menu = input().rstrip()
        service.add(menu)

def getOrder(normal, special, service) :
	N = int(input())
	global normalPrice
	global totalPrice
	global serviceCnt
	global specialCnt
	for _ in range(N) :
		menu = input().rstrip('\n')
		if menu in normal :
			normalPrice += normal[menu]
			totalPrice += normal[menu]
		elif menu in special :
			totalPrice += special[menu]
			specialCnt += 1
		elif menu in service :
			serviceCnt += 1
		else :
			sys.exit("No")

setMenu(normal, special, service)
getOrder(normal, special, service)

answer = "Okay"
if specialCnt > 0 and normalPrice < 20000 :
    answer = "No"
else :
	if serviceCnt > 1 :
		answer = "No"
	elif serviceCnt == 1 and totalPrice < 50000 :
		answer = "No"
print(answer)