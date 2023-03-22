# 백준 1388 - 바닥 장식

import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    # '-' 일 경우
    if graph[x][y] == '-':
        graph[x][y] = 1
        for i in range(4):
            ny = y + dy[i]
            if (0 < ny < m) and graph[x][ny] == '-':
                dfs(x, ny)
    # '|' 일 경우
    if graph[x][y] == '|':
        graph[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            if (0 < nx < n) and graph[nx][y] == '|':
                dfs(nx, y)


n, m = map(int, input().split())  # n: 세로, m: 가로
graph = []
for _ in range(n):
    graph.append(list(input()))

answer = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == '-' or graph[i][j] == '|':
            dfs(i, j)
            answer += 1

print(answer)
