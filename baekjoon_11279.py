# 백준 11279 - 최대 힙

import heapq
import sys

n = int(input())
heap = []

# heapq는 최소 힙을 지원한다. 그렇기에 최대 힙을 이용하기 위해선 값을 입력할 때 -를 곱해서 가장 큰 값이 가장 작은 값이 되게 한 후
# pop을 할 때, 다시 -를 곱해서 원래의 값으로 출력하면 최대 힙을 구현할 수 있다.
for i in range(n):
    num = int(sys.stdin.readline()) # int(input())으로 하면 시간 초과 발생함.
    if num > 0:
        heapq.heappush(heap, -num)
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(-heapq.heappop(heap))
