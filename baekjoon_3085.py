# 백준 3085 - 사탕 게임

# 아이디어: 교환을 한번만 했을 때 최대의 길이를 얻기 위해서는 하나씩 교환을 해보고 그때 최대 길이를 추출하면 된다. 맵의 크기가 50 이하이기에 브루트포스 방법으로 접근!

n = int(input())
graph = [list(input()) for _ in range(n)]
answer = 0


def check(arr):
    length = 1
    # 가로로 최대 길이 탐색
    for i in range(len(arr)):
        count = 1
        for j in range(1, len(arr)):
            if arr[i][j] == arr[i][j - 1]:
                count += 1 # 앞의 것과 같다면 최대 길이 값을 하나 늘려준다.
            else:
                count = 1 # 다르다면 다시 1로 초기화 시킨다.

            if count > length:
                length = count # 새로 구한 최대 길이가 더 길다면 갱신해준다.

        # 세로로 최대 길이 탐색
        count = 1
        for j in range(1, len(arr)):
            if arr[j][i] == arr[j - 1][i]:
                count += 1 # 앞의 것과 같다면 최대 길이 값을 하나 늘려준다.
            else:
                count = 1 # 다르다면 다시 1로 초기화 시킨다.

            if count > length:
                length = count  # 새로 구한 최대 길이가 더 길다면 갱신해준다.

    return length


for i in range(n):
    for j in range(n):
        # 가로 바꾸기
        if j + 1 < n and graph[i][j] != graph[i][j+1]: # 주어진 칸을 벗어나지 않고 인접한 사탕의 색이 서로 다를 때
            graph[i][j], graph[i][j + 1] = graph[i][j + 1], graph[i][j] # 가로로 바꿨을 때
            temp = check(graph) # 인접한 사탕들과의 최대 길이값을 반환한다.

            if temp > answer:
                answer = temp

            # 바꿨던 것을 다시 원래대로 돌려놓기
            graph[i][j], graph[i][j + 1] = graph[i][j + 1], graph[i][j]

        # 세로 바꾸기
        if i + 1 < n and graph[i][j] != graph[i+1][j]: # 주어진 칸을 벗어나지 않고 인접한 사탕의 색이 서로 다를 때
            graph[i][j], graph[i + 1][j] = graph[i + 1][j], graph[i][j]
            temp = check(graph)

            if temp > answer:
                answer = temp

            # 바꿨던 것을 다시 원래대로 돌려놓기
            graph[i][j], graph[i + 1][j] = graph[i + 1][j], graph[i][j]

print(answer)
