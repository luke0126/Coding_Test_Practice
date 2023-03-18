# 백준 1789 - 수들의 합

s = int(input())
result = 0
count = 0

while True:
    count += 1
    result += count
    if result > s:
        break

answer = count - 1
print(answer)