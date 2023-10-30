# 백준 19941번 - 햄버거 분배

n, k = map(int, input().split())
arr = list(input())
answer = 0

for i in range(len(arr)):
    # 햄버거이면 패스, 사람이라면 어떤 햄버거를 먹는 것이 좋은지 확인
    if arr[i] == 'P':
        # 사람들은 거리가 k 이하인 햄버거를 먹을 수 있음
        for j in range(i-k, i+k+1):
            # 배열 범위 안 벗어나게 설정
            if 0 <= j < n:
                # 햄버거라면
                if arr[j] == 'H':
                    arr[j] = 'X'
                    answer += 1
                    break
    
print(answer)

