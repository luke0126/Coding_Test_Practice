# 백준 2579 - 계단 오르기

# 아이디어: 계단을 오를 때, 그 전의 칸까지의 최고 점수들을 배열에 저장한다. 어느 칸 까지 갈 때, 그 이전에 저장한 최고점을 활용하는 방법으로 접근(DP)

n = int(input())
stairs = [0]
dp = [0] * (n+1)
for i in range(n):
    stairs.append(int(input()))

for i in range(1, n+1):
    if i == 1: # 1번 계단 밟는 방법은 한 가지 뿐이다.
        dp[i] = stairs[i]
    elif i == 2: # 2번 계단은 한번에 2번 계단으로 가는 것 보다 1번->2번으로 가는 것이 항상 더 크다.
        dp[i] = stairs[i] + stairs[i-1]
    elif i == 3:
        dp[i] = max(stairs[i] + stairs[i-1], stairs[i] + stairs[i-2])
    else: # 세 칸을 연속으로 밟을 수 없다는 조건을 고려애햐 한다.
        # 만약, 6번 계단을 밟을 경우 4->6 와 5->6 방법이 있다.
        # 4->6의 경우 한번에 두 칸을 밟는 것이기에 세 칸을 연속으로 밟는 것은 신경 쓸 필요가 없다. (dp[4] + stairs[6])
        # 5->6의 경우 3->5->6 과 같이 두 칸을 건너 뛴 후 연속된 칸을 밟으면 된다.(dp[3] + stairs[5] + stairs[6])
        dp[i] = max(stairs[i] + dp[i-2], stairs[i] + stairs[i-1] + dp[i-3])

# 마지막 계단을 밟아야 하기 때문에 마지막 칸 까지 갔을 때 최대 점수를 출력해주면 된다.
print(dp[n])