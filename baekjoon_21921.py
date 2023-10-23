# 백준 21921번 - 블로그

import sys
input = sys.stdin.readline

n, x = map(int, input().split())
info = list(map(int, input().split()))


# 누적 방문자 수 구하기
cum_visitors = [0]
for i in range(n):
    cum_visitors.append(cum_visitors[i] + info[i])

print(cum_visitors)

gap = []
day = 0

# 현재 확인 중인 날부터 x일까지가 n일보다 작다면
while day + x <= n:
    # 누적합으로 이루어져 있기 때문에 x일 후와 현재 날짜 간의 방문자 수를 빼기
    gap.append(cum_visitors[day+x]-cum_visitors[day])
    day += 1


if sum(info) == 0:
    print('SAD')
else:
    # 최대가 얼마인지
    print(max(gap))
    # 최댓값과 같은 날이 얼마인지
    print(gap.count(max(gap)))