# 백준 2109 - 순회강연

import heapq
n = int(input())
suggestion = []
for _ in range(n):
    suggestion.append(list(map(int, input().split())))

suggestion.sort(key=lambda x: x[1])
pay = []

for i in suggestion: # 마감일이 얼마 남지 않은 순으로 오름차순을 했고 이를 하나씩 살펴보면
    heapq.heappush(pay, i[0]) # pay 배열에 제안의 금액을 하나씩 넣어준다.
    # 이때, 하루에 한 강의만 할 수 있기에 받아들일 제안의 갯수가 곧 시간의 흐름을 뜻한다.
    # 흘러간 시간(받아들일 제안의 갯수)이 확인 중인 제안의 데드라인보다 크다면
    # 확인 중인 제안과 받아들이려고 했던 제안 중 비용이 더 적은 제안을 거절해야한다.
    # 이러한 과정을 거쳐 데드라인을 넘지 않는 선에서 최대한의 비용을 챙길 수 있게 된다.
    if len(pay) > i[1]:
        heapq.heappop(pay)
print(sum(pay))
