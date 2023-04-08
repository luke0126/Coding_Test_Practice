# 백준 20057 - 마법사 상어와 토네이도

# 아이디어: 토네이도가 이동하는 것을 고려하며 해당 비율을 신경써서 푼다.

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
# 세로축을 x, 가로축을 y 라고 생각하자! (r,c)는 A[r][c]

left = [(1, 1, 0.01), (-1, 1, 0.01), (1, 0, 0.07), (-1, 0, 0.07), (1, -1, 0.1), (-1, -1, 0.01), (2, 0, 0.02),
        (-2, 0, 0.02)]
right = [(x, -y, z) for x, y, z in left]
up = [(y, x, z) for x, y, z in left]
down = [(-y, x, z) for x, y, z in left]


def cal(time, dx, dy, direction):  # 모래를 계산하는 함수
    global answer, sx, sy

    for _ in range(time):
        sx += dx  # x 좌표
        sy += dy  # y 좌표
        if sy < 0:  # y 좌표가 범위를 넘어가면 멈춘다.
            break

        total = 0  # a를 구하기 위한 변수
        for dx, dy, z in direction:
            nx = sx + dx
            ny = sy + dy
            if z == 0:  # a(나머지)
                new_sand = board[sx][sy] - total
            else:
                new_sand = int(board[sx][sy] * z)
                total += new_sand

            if 0 <= nx < N and 0 <= ny < N:
                board[nx][ny] += new_sand
            else:
                answer += new_sand


for i in range(1, N + 1):
    if i % 2:
        cal(i, 0, -1, left)
        cal(i, 1, 0, down)
    else:
        cal(i, 0, 1, right)
        cal(i, -1, 0, up)
print(answer)
