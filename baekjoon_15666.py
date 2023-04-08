# 백준 15666 - N과 M(12)

# 아이디어: 현재 숫자와 다음에 조사할 숫자를 비교하여 현재 숫자보다 크거나 같은 숫자만 탐색하게 한다.
n, m = map(int, input().split())
nums = list(set(map(int, input().split())))
nums.sort()
result = []
visited = [False] * (len(nums) + 1)


def dfs(num):
    if m == len(result):
        print(' '.join(map(str, result)))
        return
    for i in range(len(nums)):
        if nums[i] >= num:
            result.append(nums[i])
            dfs(nums[i])
            result.pop()


dfs(nums[0])
