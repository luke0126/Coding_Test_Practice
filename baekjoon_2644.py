# 백준 2644번 - 촌수 계산


import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())
start, end = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
result = []

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def dfs(v, count):  # count값은 재귀함수 돌기 전까지의 정보를 지니고 있어서 모든 노드를 탐색해도 촌수 계산할 때는 문제가 생기지 않는다.
    count += 1
    visited[v] = True
    if v == end:
        result.append(count - 1)

    for i in graph[v]:
        if not visited[i]:
            dfs(i, count)


dfs(start, 0)
if len(result) == 0:
    print(-1)
else:
    print(result[0])
