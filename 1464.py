# 뒤집기
# https://www.acmicpc.net/problem/1464

S = input()
for i in range(len(S) - 1) :
    # print(S, S[0], S[i], S[i + 1], S[i::-1], S[i + 1:], S[i + 1::-1], S[i + 2:])
    if S[i] > S[i + 1] and S[0] >= S[i + 1] :	# 위에 찍어보면서 했음
        S = S[i::-1] + S[i + 1:]
        if S[i] >= S[i + 1] :
            S = S[i + 1::-1] + S[i + 2:]
print(S)