# 백준 1931 - 회의실 배정

n = int(input())
reservation = []

for i in range(n):
    start, end = map(int, input('').split())
    reservation.append([start, end])

# 종료 시간이 빠른 순으로 정렬해야 다음에 선택할 수 있는 경우가 많아진다. 또한, 종료 시간이 같을 경우, 시작 시간이 빠른 순으로 정렬해야 선택할 수 있는 경우가 더 많아진다.
# 그러므로 시작 시간이 빠른 순으로 정렬 후에 종료 시간이 빠른 순으로 정렬한다.
reservation.sort(key=lambda time: time[0]) # 시작 시간이 빠른 순으로 정렬한다.
reservation.sort(key=lambda time: time[1]) # 종료 시간이 빠른 순으로 정렬한다.

now = 0
answer = 0
for s, e in reservation:
    if now <= s:
        now = e
        answer += 1

print(answer)
