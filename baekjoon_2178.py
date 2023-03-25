# 백준 2178 - 미로 탐색

# bfs는 최단 경로를 보장하기에 이 문제는 bfs로 풀이한다.

from collections import deque

n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(map(int, input())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:  # 미로 범위 안이고 1이라면(갈 수 있는 길)
                queue.append((nx, ny))  # 인접한 곳에 대한 좌표를 넣어주고
                maze[nx][ny] = maze[x][y] + 1  # 해당 좌표는 이전 좌표에서의 경로 길이에서 1을 더하여 한칸 더 전진한 것을 나타내어 준다.
    return maze[n - 1][m - 1]  # 배열은 0부터 시작하기에 -1을 한 index를 return 한다.

print(bfs(0, 0))
