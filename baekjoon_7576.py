# 백준 7576 - 토마토

# 아이디어: 안 익은 토마토가 익으면 해당 좌표까지 걸린 시간을 좌표값에 넣어준다. 그렇게 하여 모두 익게 되는 경우를 파악하고 그때까지 걸린 시간을 출력한다.
from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = 0
ripe = deque()
for i in range(n): # 익은 토마토의 위치 정보를 입력
    for j in range(m):
        if graph[i][j] == 1:
            ripe.append([i, j])

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

while True:
    if len(ripe) == 0:
        break
    x, y = ripe.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1 # 새로 익은 토마토는 그 전의 토마토가 익은 날짜에 하루를 더해 해당 토마토가 익기까지 걸린 시간을 구한다.
                ripe.append([nx, ny]) # 새로 익을 토마토 위치 정보 삽입

for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit()
    answer = max(answer, max(i))

print(answer - 1) # 주의! 익은 토마토의 좌표에 들어있는 값이 1부터 시작하였다. 그렇기 때문에 1을 빼줘야 답이 된다.