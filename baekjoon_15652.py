# 백준 15652 - N과 M(4)

# 아이디어: 현재 숫자와 다음 들어올 숫자의 크기를 비교해서 현재 숫자보다 크다면 방문하고 작은 수라면 방문하지 않게 한다.
n, m = map(int, input().split())
result = []


def dfs(num):
    if m == len(result):
        print(' '.join(map(str, result)))
        return
    for i in range(1, n+1):
        result.append(i)
        if num <= i + 1:
            dfs(i+1)
        result.pop()

dfs(1)
