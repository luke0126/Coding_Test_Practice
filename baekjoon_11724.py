# 백준 11724번 - 연결 요소의 개수

import sys

sys.setrecursionlimit(10000)  # 파이썬에는 재귀 제한이 있기 때문에 재귀 허용치를 제한하여 런타임에러를 방지했다.
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

count = 0


def dfs(v):
    visited[v] = True
    for i in range(1, n + 1):
        if not visited[i] and graph[v][i] == 1:
            dfs(i)


for i in range(1, n + 1):
    if not visited[i]: # 방문하지 않은 점이라면 dfs를 실행한다. 즉, 새로 dfs를 한다는 것은 서로 연결되어 있지 않다는 뜻이므로 count값을 키워준다.
        dfs(i)
        count += 1

print(count)
