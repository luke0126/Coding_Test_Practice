# 백준 1446 - 지름길

# n: 지름길의 갯수 / d: 고속도로 길이
# 반복문 실행하면서 visited의 각 원소에 현재 위치까지 오는데 얼마나 걸리는지 확인하면서 접근


n, d = map(int, input().split())
info = [list(map(int,input().split())) for i in range(n)]
visited = [i for i in range(d+1)]


# 주어진 길이까지 갔는지 확인하기 위해 반복문 실행

for current in range(d+1):
    for start, end, distance in info:
        visited[current] = min(visited[current], visited[current-1]+1)
        # 현재 위치가 start와 같으면 비교! 목적지보다 넘어가는 거 방지!
        if current == start and end <= d and visited[current] + distance < visited[end] :
            # 이동을 하게 되면 현재 위치까지 이동한 값과 새로 이동할 거리를 넣기
            visited[end] = visited[current] + distance



print(visited[d])

