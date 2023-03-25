# 백준 2178 - 안전 영역

# 아이디어: 비가 온 양에 따라서 물에 잠긴 곳을 확인한 후 그 정보를 통해 dfs로 안전 영역 갯수를 구하는 방식으로 문제 풀이 접근

import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

n = int(input())
graph = []
highest = 0
num = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

highest = max(map(max, graph))


def dfs(x, y, h):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > h and not visited[nx][ny]: # 지역에서 벗어나지 않고 h값 보다 크고 방문하지 않은 곳이라면
            visited[nx][ny] = True
            dfs(nx, ny, h)


for h in range(highest):
    count = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] > h and not visited[i][j]: # 물에 잠기지 않고 방문하지 않은 곳이라면 해당 구역의 안전 영역을 알기 위해 dfs를 수행
                count += 1
                visited[i][j] = True
                dfs(i, j, h)
    num.append(count)
print(num)
print(max(num))
