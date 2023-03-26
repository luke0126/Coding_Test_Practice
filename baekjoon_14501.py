# 백준 14501 - 퇴사

# 아이디어: 최대 수익을 벌어야 하기에 모든 그리디로 하게 될 경우 최적의 해답을 주는 것을 보장할 수 없기에 dp로 모든 경우를 확인하여 최대 수익을 확인한다.

n = int(input())
t = []
p = []
for _ in range(n):
    time, pay = map(int, input().split())
    t.append(time)
    p.append(pay)
dp = [0 for _ in range(n+1)]

for i in range(n): # i+1 번째 날을 선택했을 때
    for j in range(i + t[i], n+1): # i+1번째 날에 상담을 진행했을 때 상담이 가능한 모든 날짜를 확인
        if dp[j] < dp[i] + p[i]: # 수익을 최대로 얻기 위해 dp에 값을 저장
            dp[j] = dp[i] + p[i]

print(max(dp))