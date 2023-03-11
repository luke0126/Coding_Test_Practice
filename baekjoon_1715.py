# 백준 1715 - 카드 정렬하기

import heapq

# 일반 배열을 사용했을 때 메모리 초과가 발생하여 heapq를 이용

n = int(input())
cards = []
for i in range(n):
    heapq.heappush(cards, int(input()))

answer = 0

if len(cards) == 1:
    print(answer)
else:
    while len(cards) > 1:
        temp = heapq.heappop(cards) + heapq.heappop(cards)
        answer += temp
        heapq.heappush(cards, temp)
    print(answer)