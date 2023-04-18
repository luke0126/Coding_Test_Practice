# 백준 7568 - 덩치

# 아이디어: 몸무게랑 키를 묶어서 리스트에 저장한 후 자신보다 모두가 큰 사람의 수를 카운트!

n = int(input())

info = []
ans = []
for i in range(n):
    weight, height = map(int, input().split())
    info.append((weight, height))

for i in range(n):
    count = 0
    for j in range(n):
        if info[i][0] < info[j][0] and info[i][1] < info[j][1]:
            count += 1
    ans.append(count + 1)

for d in ans:
    print(d, end=" ")
