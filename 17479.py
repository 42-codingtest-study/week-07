import sys
input= sys.stdin.readline

A , B, C = map(int,input().split())

nom_li = dict() #일반메뉴
spe_li = dict() #특별메뉴
ser_li = dict() #서비스메뉴

for _ in range(A): #일반메뉴판
    food , price = map(str,input().rstrip().split())
    nom_li[food] = int(price)

for _ in range(B): #특별메뉴판
    food2 , price2= map(str,input().rstrip().split())
    spe_li[food2] = int(price2)

for _ in range(C):
    food3 = input().rstrip()
    ser_li[food3] = 1

N = int(input()) #음식 주문수

nom_cnt = 0 # 일반메뉴 주문가격
ser_cnt = 0 # 일반 + 특별메뉴 주문가격
spe_check = 0 # 스페셜 메뉴를 주문했는지
ser_check = 0 #서비스 메뉴는 하나까지만 가능
error = 0


for _ in range(N):
    name = input().rstrip()
    if name in ser_li.keys():
        ser_check += 1
    
    elif name in spe_li.keys():
        ser_cnt += spe_li.get(name)
        spe_check += 1
    
    elif name in nom_li.keys():
        nom_cnt += nom_li.get(name)
        ser_cnt += nom_li.get(name)

if spe_check !=0 and nom_cnt < 20000 or ser_check >=2 or ser_check ==1 and ser_cnt < 50000:
    print("No")
else:
    print("Okay")