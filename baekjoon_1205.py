# 백준 1205번 - 등수 구하기

# 아이디어: 랭킹의 점수가 새로운 점수 이하이면 그 등수가 새로운 점수의 등수가 되면서 반복문 수행

n, score, p = map(int, input().split())

if n == 0:
    print(1)
else:
    rank = list(map(int, input().split()))

    if n == p and rank[-1] >= score:
        print(-1)
    else:
        answer = n + 1
        for i in range(n):
            if rank[i] <= score:
                answer = i + 1
                break
        print(answer)
