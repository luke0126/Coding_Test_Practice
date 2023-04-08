# 백준 15651 - N과 M(3)

# 아이디어: 같은 숫자를 방문해야하기 때문에 방문 여부를 확인할 필요가 없다. 즉, 주어진 범위 내의 모든 숫자를 탐색하면 된다.

n, m = map(int, input().split())
result = []


def dfs(num):
    if m == len(result):
        print(' '.join(map(str, result)))
        return
    for i in range(1, n+1):
        result.append(i)
        dfs(i+1)
        result.pop()

dfs(1)
