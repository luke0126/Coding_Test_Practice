# 백준 15650 - N과 M(2)

# 아이디어: [1,2] 가 이미 나왔기에 [2,1]은 나오면 안 된다. 이를 위해 for문을 num부터 돌려 중복을 피한다.

n, m = map(int, input().split())
result = []
visited = [False for _ in range(n+1)]


def dfs(num):
    if m == len(result):
        print(' '.join(map(str, result)))
        return
    for i in range(num, n+1):
        if visited[i] == False:
            visited[i] = True
            result.append(i)
            dfs(i + 1)
            result.pop()
            visited[i] = False


dfs(1)
