# Brainf*ck
# https://www.acmicpc.net/problem/2733

# 결과 다 나오는데 왜 안되는지 모르겠습니다 .... ㅜ 아쉬워라
import sys
from collections import deque
input = sys.stdin.readline
for cnt in range(1, int(input()) + 1) :
    line = input().replace("\n", "")
    array = deque([0] * 32768)
    pointer = 0
    print("PROGRAM #" + str(cnt) + ":")
    cmd = ''
    while line != "end" :
        if line.find("%") >= 0 :
            cmd += line[:line.find("%")]
        elif line.find("%") == -1 :
            cmd += line
        line = input().replace("\n", "")
    error = []
    for i in cmd :
        if i == '[' :
            error.append(i)
        elif i == ']' :
            error.pop()
    answer = ''
    i = 0
    while len(error) == 0 and i < len(cmd) :
        if cmd[i] == '>' :
            array.rotate(-1)
        elif cmd[i] == '<' :
            array.rotate(1)
        elif cmd[i] == '+' :
            array[0] = 0 if array[0] == 255 else array[0] + 1
        elif cmd[i] == '-' :
            array[0] = 255 if array[0] == 0 else array[0] - 1
        elif cmd[i] == '.' :
            answer += chr(array[0])
        elif cmd[i] == '[' and array[0] == 0 :
            while cmd[i] != ']' :
                i += 1
        elif cmd[i] == ']' and array[0] != 0 :
            while cmd[i] != '[' :
                i -= 1
        i += 1
    if len(error) != 0 :
        print("COMPILE ERROR")
    else :
        print(answer)