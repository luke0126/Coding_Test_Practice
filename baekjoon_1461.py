# 백준 1461 - 도서관

n, m = map(int, input().split())
locations = list(map(int, input().split()))

positive = []
negative = []
maxFar = 0

for i in locations:
    maxFar = max(abs(i), maxFar)
    if i > 0:
        positive.append(i)
    else:
        negative.append(abs(i))
# 내림차순으로 정렬한다. 왜냐하면, 가장 먼 곳부터 m권씩 반납해야 최소 걸음으로 반납할 수 있기 때문에 내림차순으로 정렬한다.
positive.sort(reverse=True)
negative.sort(reverse=True)

count = 0
# m권씩 옮길 수 있다. 더 멀리 있는 책을 옮기면 그것보다 짧은 거리에 있는 책은 멀리 있는 곳까지 가는 동안에 옮기면 되기에 for문은 m씩 증가시킨다.
for i in range(0, len(positive), m):
    # 책을 옮기고 원점에서 다른 책들을 가지러 가야하기에 2를 곱해준다.
    count += positive[i]*2
for i in range(0, len(negative), m):
    count += negative[i]*2

# 가장 멀리 있는 책은 옮기고 다시 원점으로 돌아올 필요가 없으므로 그 거리만큼 빼주면 정답이 된다.
answer = count - maxFar
print(answer)
