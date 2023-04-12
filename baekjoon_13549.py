# 백준 13549 - 숨바꼭질 3

# 아이디어: 순간이동을 하는 경우 시간이 흐르지 않기 때문에 이 점을 유의하여 각 지점까지 방문하기 위해 걸린 시간을 해당 좌표들에 넣고 왔다갔다 한다.
# 최단 경로를 찾는 것이므로 bfs로 풀이!

from collections import deque

n, k = map(int, input().split())

queue = deque()
queue.append(n)
pos = [0] * 100001
pos[n] = 1

while queue:
    now = queue.popleft()
    if now == k:
        print(pos[k] - 1)
        break
    for next in (now * 2, now + 1, now - 1):
        if 0 <= next < 100001 and pos[next] == 0:
            if next == now * 2: # 순간이동
                pos[next] = pos[now] # 순간이동하면 시간 증가 안 함
                queue.append(next)
            else: # 앞, 뒤 이동
                pos[next] = pos[now] + 1 # 시간 1초 증가
                queue.append(next)
