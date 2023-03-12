# 백준 2217 - 로프

n = int(input())
rope = []
for _ in range(n):
    rope.append(int(input()))

rope.sort(reverse=True)
temp = []
for i in range(n):
    temp.append((i+1)*rope[i])

answer = max(temp)
print(answer)