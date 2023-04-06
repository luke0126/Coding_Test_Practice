# 백준 13460 - 스타트와 링크

# 아이디어: 백트래킹을 이용해 각 팀에 사람을 넣어 사람들의 능력치를 더하며 각 팀의 차이를 최소인 것을 출력한다.

import sys

sys.setrecursionlimit(10 ** 9)
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
result = []


def dfs(num, idx): # num: 현재까지 팀에 선택된 사람 수, idx: 이번에 조사를 시작해야할 사람의 index
    if num == n // 2:
        stat1, stat2 = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    stat1 += board[i][j] # 팀에 추가한 사람들끼리의 능력치를 더한다.
                elif not visited[i] and not visited[j]:
                    stat2 += board[i][j] # 팀에 추가되지 않은 사람들(즉, 상대팀)끼리의 능력치를 더한다.
        result.append(abs(stat1 - stat2))

    for i in range(idx, n):
        if not visited[i]:  # 방문하지 않았다면
            visited[i] = True  # 방문 처리 해주고
            dfs(num + 1, i + 1) # 방문 횟수를 하나 늘려주고, i 번째 사람까지 선택했으니 그 다음 번쨰 사람부터 조사하면 된다.
            visited[i] = False


dfs(0, 0)
print(min(result))
