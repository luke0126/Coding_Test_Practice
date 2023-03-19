# 백준 2667번 - 단지번호붙이기

import sys

sys.setrecursionlimit(10000)  # 파이썬에는 재귀 제한이 있기 때문에 재귀 허용치를 제한하여 런타임에러를 방지했다.

n = int(input())
graph = []
num = []
count = 0
village = 0

for i in range(n):
    graph.append(list(map(int, input())))

dx = [0, 0, 1, -1] # 가로 이동
dy = [1, -1, 0, 0] # 세로 이동


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False


for i in range(n):
    for j in range(n):
        if dfs(i, j):
            num.append(count)
            village += 1
            count = 0

num.sort()
print(village)
for i in range(len(num)):
    print(num[i])
