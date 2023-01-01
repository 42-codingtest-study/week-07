#굳이 왜 이런 짓을,,,
import sys
input = sys.stdin.readline

s = list(str(input().rstrip()))
n = len(s)

def reverse(num, str):
	left = 0
	right = num - 1
	while left < right:
		temp = str[right]
		str[right] = str[left]
		str[left] = temp
		left += 1
		right -= 1
	return str

for i in range(1, n):
	if s[i] < s[i - 1] and s[i] <= s[0]:
		reverse(i, s)
		if s[i - 1] >= s[i]:
			reverse(i + 1, s)

print(''.join(s))