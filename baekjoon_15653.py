# 백준 15653 - N과 M(5)

# 아이디어: 주어진 숫자를 오름차순 정렬하고 백트래킹을 한다.
n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
result = []
visited = [False] * n


def dfs():
    if m == len(result):
        print(' '.join(map(str, result)))
        return
    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            result.append(nums[i])
            dfs()
            result.pop()
            visited[i] = False

dfs()
