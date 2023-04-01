# 백준 1012 - 유기농 배추

# 아이디어: 배추가 있는 곳의 상하좌우를 확인하여 인접한 배추가 있는 곳을 확인하고 인접한 배추가 있다면 방문처리를 하고 하나의 영역으로 묶어서 영역을 세어주는 방식으로 풀이

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

t = int(input())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if graph[ny][nx] == 1: # 인접한 배추가 있다면
                graph[ny][nx] = -1 # 해당 배추는 방문한 것으로 처리한다.
                dfs(nx, ny) # 인접한 곳에 배추가 있는지 확인


for _ in range(t):
    m, n, k = map(int, input().split())
    answer = 0
    graph = [[0] * m for _ in range(n)]

    for _ in range(k): # 배추 위치 정보 입력
        X, Y = map(int, input().split())
        graph[Y][X] = 1

    for x in range(m):
        for y in range(n):
            if graph[y][x] == 1:
                dfs(x, y)
                answer += 1
    print(answer)
