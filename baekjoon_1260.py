# 백준 1260 - DFS와 BFS

from collections import deque

n, m, v = map(int, input().split())

graph = [[0] * (n + 1) for _ in range(n + 1)]  # 각 정점에 대해 나타내기 위한 초기화 (n+1)을 곱한 이유는 index를 좀 더 편하게 보기 위해서이다.
dfs_visited = [False] * (n + 1)
bfs_visited = [False] * (n + 1)

# 그래프를 초기화 했으면 다음으로는 연결을 나타낸다. 이때, 간선은 양방향이므로 x에서 y 와 y에서 x를 생각해야한다.
for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1


# dfs를 구현해보자
def dfs(v):
    dfs_visited[v] = True  # 정점 v에 방문을 했기에 True로 바꿔 정점에 방문한 것을 나타내어 준다.
    print(v, end=' ')  # 방문한 점을 출력한다.
    for i in range(1, n + 1):
        if not dfs_visited[i] and graph[v][i] == 1:  # v와 연결되어 있고 아직 방문하지 않은 정점의 index 값을 받아 재귀함수를 사용해 탐색한다.
            dfs(i)


# bfs를 구현해보자
def bfs(v):
    bfs_visited[v] = True # 정점 v에 방문을 했기에 True로 바꿔 정점에 방문한 것을 나타내어 준다.
    queue = deque() # queue를 사용하는 것보다 O(n)(시간복잡도)이 작으므로 deque를 사용한다.
    queue.append(v) # deque에 방문한 v를 넣어준다.
    while queue:
        popV = queue.popleft() # deque의 가장 왼쪽 값을 pop시킨다. 즉, 가장 먼저 들어온 값을 출력한다.
        print(popV, end=' ')
        for i in range(1, n + 1):
            if not bfs_visited[i] and graph[popV][i] == 1: # v와 연결되어 있고 아직 방문하지 않은 정점을 찾는다.
                queue.append(i) # 찾았다면 queue에 넣어준다.
                bfs_visited[i] = True # 해당 정점에 방문했다는 것으로 바꿔준다.


dfs(v)
print()
bfs(v)
