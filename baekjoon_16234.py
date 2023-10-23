# 백준 16234번 - 인구 이동

# 조건 1: 국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 연다.
# 조건 2: 위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.
# 조건 3: 국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합이라고 한다.
# 조건 4: 연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
# 조건 5: 연합을 해체하고, 모든 국경선을 닫는다.

from collections import deque

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0

while True:
    visited = [[False] * n for _ in range(n)]
    flag = False
    for i in range(n):
        for j in range(n):
            # 아직 방문하지 않았다면
            if visited[i][j] == False:
                visited[i][j] = True
                queue = deque()
                union = []
                queue.append((i,j))
                union.append((i,j))
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if (0 <= nx < n) and (0 <= ny < n) and visited[nx][ny] == False:
                            # 조건 1
                            if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                                visited[nx][ny]=True
                                queue.append((nx,ny))
                                union.append((nx,ny))

                if len(union) > 1: 
                    flag = True
                    people = sum(graph[x][y] for x,y in union) // len(union)
                    for x, y in union: 
                        graph[x][y] = people

    if not flag: 
        print(result)
        break
        
    result += 1