# 백준 20055 - 컨베이어 벨트 위의 로봇
 
from collections import deque
n, k = map(int, input().split())
durability = deque([int(i) for  i in input().split()])
visited = deque([0] * n)
answer = 0


while 1:
    durability.rotate(1)
    visited.rotate(1)
    visited[-1]=0 
    if sum(visited): 
        for i in range(n-2, -1, -1): 
            if visited[i] == 1 and visited[i+1] == 0 and durability[i+1]>=1:
                visited[i+1] = 1
                visited[i] = 0
                durability[i+1] -= 1
        visited[-1]=0
    if visited[0] == 0 and durability[0]>=1:
        visited[0] = 1
        durability[0] -= 1
    answer += 1
    if durability.count(0) >= k:
        break
                
print(answer)
