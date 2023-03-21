# 백준 11725 - 트리의 부모 찾기

import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
visited = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(n-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

result = {}
for i in range(n + 1):
    result[i] = 0


def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
            result[i] = v


dfs(1)
answer = list(result.values())
for i in range(2, n+1):
    print(answer[i])
