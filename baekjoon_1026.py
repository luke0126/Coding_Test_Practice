# 백준 1026 - 보물

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
answer = 0

a.sort()

for i in range(n):
    answer = answer + a[i] * max(b)
    b.pop(b.index(max(b))) # b 배열은 재정렬할 수 없기에 하나씩 pop하는 방식으로 정답을 구한다.

print(answer)