str = input()
result = str[0]
for i in range(1, len(str)):
    if result[i-1] < str[i]:
        result = str[i] + result
    else:
        result = result + str[i]
print(result[::-1])
