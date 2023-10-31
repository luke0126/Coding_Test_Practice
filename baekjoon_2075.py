# 백준 2075번 - N번째 큰 수

import heapq

n = int(input())
heap = []

for _ in range(n):
    nums = list(map(int, input().split()))
    for num in nums:
        # heap의 수를 n만큼 계속 유지하여 메모리 초과 방지하기
        if len(heap) < n:
            heapq.heappush(heap, num)
        else:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

print(heap[0])
