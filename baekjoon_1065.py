# 백준 1065 - 한수

n = int(input())
answer = 0

for i in range(1, n+1):
    if i < 100:
        answer += 1
    else:
        arr = list(map(int, str(i)))
        if arr[2] - arr[1] == arr[1] - arr[0]:
            answer += 1

print(answer)



