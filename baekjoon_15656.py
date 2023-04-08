# 백준 15655 - N과 M(6)

# 아이디어: 중복된 수가 들어갈 수 있으므로 모든 수를 탐색하는 방법으로 백트래킹한다.
n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
result = []


def dfs():
    if m == len(result):
        print(' '.join(map(str, result)))
        return
    for i in range(n):
        result.append(nums[i])
        dfs()
        result.pop()


dfs()
