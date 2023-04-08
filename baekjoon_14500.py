# 백준 14500 - 테트로미노

# 아이디어: 'ㅗ', 'ㅏ', 'ㅜ', 'ㅓ' 의 경우 2번째 탐색까지는 dfs로 갔다가 나머지는 한번씩만 탐색해주면 된다.

n, m = map(int, input().split())  # n: 세로, m: 가로
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
max_val = max(map(max, board))
answer = 0

dx = [-1, 1, 0, 0]  # 상, 하
dy = [0, 0, -1, 1]  # 좌, 우


def dfs(x, y, count, tsum):
    global answer
    if tsum + max_val * (4-count) <= answer:
        return

    if count == 4:
        answer = max(answer, tsum)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            if count == 2:
                visited[nx][ny] = True
                dfs(x, y, count + 1, tsum + board[nx][ny])
                visited[nx][ny] = False
            visited[nx][ny] = True
            dfs(nx, ny, count + 1, tsum + board[nx][ny])
            visited[nx][ny] = False


for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])
        visited[i][j] = False


print(answer)
