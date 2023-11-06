# 백준 2531번 - 회전 초밥

n, d, k, c = map(int, input().split())  
sushi = [int(input()) for _ in range(n)]

# 초밥 종류별 개수를 저장
type = {}
max_count = 0  # 최대로 먹을 수 있는 초밥 종류의 개수

# 초기 k개의 초밥 개수 세팅
for i in range(k):
    type[sushi[i]] = type.get(sushi[i], 0) + 1
    if type[sushi[i]] == 1:
        max_count += 1

# 회전 초밥을 먹는 경우를 탐색
answer = max_count
for i in range(n):
    # 왼쪽 초밥 제외
    type[sushi[i]] -= 1 
    if type[sushi[i]] == 0:
        del type[sushi[i]]
        max_count -= 1
    # 오른쪽 초밥 추가
    type[sushi[(i + k) % n]] = type.get(sushi[(i + k) % n], 0) + 1 
    if type[sushi[(i + k) % n]] == 1:
        max_count += 1

    if c not in type:
        answer = max(answer, max_count + 1)
    else:
        answer = max(answer, max_count)

print(answer)

