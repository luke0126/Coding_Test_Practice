# 백준 13458 - 시험 감독

# 아이디어: 각 시험장에 총감독관은 무조건 1명이 배치가 되어야 한다. 각 시험장에서 응시하는 학생에서 총감독관이 감독할 수 있는 학생 수를 뺀 후, 남은 인원은 부감독관이 감독하게 하면 된다.

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
count = 0

for i in a:
    if i - b > 0:
        count += 1
        if (i - b) % c != 0:
            count += ((i-b) // c) + 1
        else:
            count += (i-b) // c
    else:
        count += 1

print(count)