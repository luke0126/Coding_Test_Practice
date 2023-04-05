# 백준 13460 - 구슬 탈출 2

# 아이디어:

from collections import deque

n, m = map(int, input().split())  # n: 세로, m: 가로
board = [list(input()) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            rx, ry = i, j  # 빨간 공의 첫 위치
        if board[i][j] == 'B':
            bx, by = i, j  # 파란 공의 첫 위치

dx = [0, 0, -1, 1]  # 좌, 우
dy = [-1, 1, 0, 0]  # 상, 하
deq = deque()
deq.append((rx, ry, bx, by))  # 각 공의 위치들이 움직임에 따라 달라진다. 이를 모든 경우를 나타낸 트리의 노드 값으로 보고 풀이를 하기 위해 visited에 값을 넣어 방문처리를 한다.
count = 0
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]  # 빨간공의 가로, 세로 위치 / 파란공의 가로, 세로 위치를 확인
visited[rx][ry][bx][by] = True

def move(graph, x, y, direction):
    cnt = 0
    # 구슬이 안 움직이는 조건: 벽이 막힐 경우, 구멍에 들어갈 경우
    while graph[x + dx[direction]][y + dy[direction]] != '#' and graph[x][y] == '0':
        x += dx[direction]
        y += dy[direction]
        cnt += 1
    return x, y, cnt


while deq:
    rx, ry, bx, by = deq.popleft()
    visited[rx][ry][bx][by] = True
    if count > 10:
        print(-1)
        exit(0)
    for i in range(4):
        nrx, nry, rcount = move(board, rx, ry, i)
        nbx, nby, bcount = move(board, bx, by, i)
        if board[nbx][nby] != '0':  # 파란공이 구멍으로 나가면 안 되는 상황이므로 파란공이 구멍 위에 안 있는 상황에서
            if board[nrx][nry] == '0':
                print(count)
                exit(0)
            if board[nrx][nry] == board[nbx][nby]:  # 빨간공과 파란공이 같은 위치에 있으면
                if rcount < bcount:  # 파란공 더 많이 움직였다면 => 빨간공이 파란공보다 진행방향으로 더 앞에 있다는 뜻
                    # 파란공을 한 칸 뒤로 보낸다.
                    nbx -= dx[i]
                    nby -= dy[i]
                else:
                    nrx -= dx[i]
                    nry -= dy[i]
            if not board[nrx][nry][nbx][nby]:
                board[nrx][nry][nbx][nby] = True
                deq.append((nrx, nry, nbx, nby))
                count += 1
