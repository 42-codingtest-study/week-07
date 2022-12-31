#굳이 왜 이런 짓을,,,
import sys
input = sys.stdin.readline

s = list(str(input()))

def reverse(num, iterable):
	left = 0
	right = num - 1
	while left < right:
		temp = iterable[right]
		iterable[right] = iterable[left]
		iterable[left] = temp
		left += 1
		right -= 1
	return iterable