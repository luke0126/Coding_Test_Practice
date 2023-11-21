# 백준 15989번 - 1,2,3 더하기 4

t = int(input())
dp = [1 for i in range(10001)]
answers = [int(input()) for _ in range(t)]

# 1과 2의 합으로 나타내는 방법의 수
for i in range(2, 10001):
    dp[i] += dp[i - 2]

# 1, 2, 3의 합으로 나타내는 방법의 수
for i in range(3, 10001):
    dp[i] += dp[i - 3]

for i in answers:
    print(dp[i])