# 백준 4963 - 섬의 개수

# 아이디어: dfs를 통해 더 이상 동, 서, 남, 북, 대각선 방향으로 걸어갈 수 없다면 섬이라는 뜻이므로 이를 이용해 dfs를 몇 번 돌았는지 계산하여 섬 개수를 구한다.

import sys

sys.setrecursionlimit(10 ** 9)

move = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]  # 북, 북동, 동, 남동, 남, 남서, 서, 북서


def dfs(x, y, board):
    board[x][y] = 0
    for (i, j) in move:
        nx, ny = x + i, y + j
        if 0 <= nx < h and 0 <= ny < w and board[nx][ny] == 1:
            dfs(nx, ny, board)


while True:
    w, h = map(int, input().split())
    count = 0
    if (w, h) == (0, 0): # w, h 값이 0, 0 이라면 종료
        break
    graph = [list(map(int, input().split())) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                dfs(i, j, graph)
                count += 1
    print(count)
