# 백준 11053 - 가장 긴 증가하는 부분 수열

# 아이디어: 배열을 돌면서 해당 숫자까지의 수열 길이를 갱신하며 최고 길이 값을 찾는다.

n = int(input())
nums = list(map(int, input().split()))
dp = [1] * n # 어떤 수가 됐건 수열은 하나 이상 존재하기에 1로 초기화 시킨다.
for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]: # 현재 숫자가 이전 숫자보다 크다면
            dp[i] = max(dp[i], dp[j]+1) # 이전의 숫자 중에서 가장 긴 길이에 수열이 하나 더 늘었기에 1을 더해준다.
print(max(dp))