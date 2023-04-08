# 백준 15655 - N과 M(6)

# 아이디어: 해당 숫자가 결과를 출력하는 배열에 존재하지 않으면 값을 넣는다.
n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
result = []


def dfs(idx):
    if m == len(result):
        print(' '.join(map(str, result)))
        return
    for i in range(idx, n):
        if nums[i] not in result:
            result.append(nums[i])
            dfs(i+1)
            result.pop()


dfs(0)
