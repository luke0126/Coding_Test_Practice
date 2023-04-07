# 백준 12100 - 2048(easy)

# 아이디어: 5번 실행했을 때 최대값을 구하는 것이기에 각각의 상황을 트리로 생각하여 dfs로 탐색하는 방식으로 해결

from copy import deepcopy

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
directions = ['u', 'd', 'l', 'r']


def move(graph, direction):
    if direction == 'u':
        for j in range(n):
            flag = 0
            for i in range(1, n):
                if graph[i][j] != 0:  # 끝 값 바로 아래에 있는 값이 0이 아니라면
                    if graph[flag][j] == 0:  # 만약, 끝 값이 0이라면
                        graph[flag][j] = graph[i][j]  # 끝 값 바로 아래에 있는 값이 한칸 위로 이동하는 것이기에 해당 값을 넣는다.
                        graph[i][j] = 0  # 한 칸 위로 올라갔기 때문에 원래 있던 자리는 빈자리가 되기에 0을 넣는다.
                        flag += 1  # 한 번의 이동에서 이미 합쳐진 블록은 다시 합칠 수 없기 때문에 한 칸 내려서 끝 값을 새로 지정한다.
                    elif graph[flag][j] == graph[i][j]:  # 만약, 끝 값과 바로 아래에 있는 값과 같다면
                        graph[flag][j] += graph[i][j]  # 두 값을 더해준다.
                        graph[i][j] = 0  # 끝 블록 바로 아래 블록이 끝 블록과 합쳐졌기에 해당칸은 이제 빈칸이 된다.
                        flag += 1  # 한 번의 이동에서 이미 합쳐진 블록은 다시 합칠 수 없기 때문에 한 칸 내려서 끝 값을 새로 지정한다.
                    else:  # 만약, 끝 값이 바로 아래 값과 다르다면
                        flag += 1  # 합쳐질 수 없기 때문에 끝 값을 한 칸 아래로 내려 끝 값을 새로 지정한다.

    elif direction == 'd':
        for j in range(n):
            flag = n - 1
            for i in range(n - 2, -1, -1):
                if graph[i][j] != 0:  # 끝 값 바로 위에 있는 값이 0이 아니라면
                    if graph[flag][j] == 0:  # 만약, 끝 값이 0이라면
                        graph[flag][j] = graph[i][j]  # 끝 값 바로 위에 있는 값이 한칸 아래로 이동하는 것이기에 해당 값을 넣는다.
                        graph[i][j] = 0  # 한 칸 아래로 내려갔기 때문에 원래 있던 자리는 빈자리가 되기에 0을 넣는다.
                        flag -= 1  # 한 번의 이동에서 이미 합쳐진 블록은 다시 합칠 수 없기 때문에 한 칸 올려서 끝 값을 새로 지정한다.
                    elif graph[flag][j] == graph[i][j]:  # 만약, 끝 값과 바로 위에 있는 값과 같다면
                        graph[flag][j] += graph[i][j]  # 두 값을 더해준다.
                        graph[i][j] = 0  # 끝 블록 바로 윗 블록이 끝 블록과 합쳐졌기에 해당칸은 이제 빈칸이 된다.
                        flag -= 1  # 한 번의 이동에서 이미 합쳐진 블록은 다시 합칠 수 없기 때문에 한 칸 올려서 끝 값을 새로 지정한다.
                    else:  # 만약, 끝 값이 바로 윗 값과 다르다면
                        flag -= 1  # 합쳐질 수 없기 때문에 끝 값을 한 칸 위로 올려 끝 값을 새로 지정한다.

    elif direction == 'l':
        for i in range(n):
            flag = 0
            for j in range(1, n):
                if graph[i][j] != 0:  # 끝 값 바로 오른쪽에 있는 값이 0이 아니라면
                    if graph[i][flag] == 0:  # 만약, 끝 값이 0이라면
                        graph[i][flag] = graph[i][j]  # 끝 값 바로 오른쪽에 있는 값이 한칸 옆으로 이동하는 것이기에 해당 값을 넣는다.
                        graph[i][j] = 0  # 한 칸 오른쪽으로 갔기 때문에 원래 있던 자리는 빈자리가 되기에 0을 넣는다.
                        flag += 1  # 한 번의 이동에서 이미 합쳐진 블록은 다시 합칠 수 없기 때문에 오른쪽으로 한 칸 옮겨 끝 값을 새로 지정한다.
                    elif graph[i][flag] == graph[i][j]:  # 만약, 끝 값과 바로 위에 있는 값과 같다면
                        graph[i][flag] += graph[i][j]  # 두 값을 더해준다.
                        graph[i][j] = 0  # 끝 블록 바로 오른쪽 블록이 끝 블록과 합쳐졌기에 해당칸은 이제 빈칸이 된다.
                        flag += 1  # 한 번의 이동에서 이미 합쳐진 블록은 다시 합칠 수 없기 때문에 오른쪽으로 한 칸 옮겨 끝 값을 새로 지정한다.
                    else:  # 만약, 끝 값이 바로 오른쪽 값과 다르다면
                        flag += 1  # 합쳐질 수 없기 때문에 끝 값을 오른쪽으로 한 칸 옮겨 끝 값을 새로 지정한다.

    else:
        for i in range(n):
            flag = n - 1
            for j in range(n - 2, -1, -1):
                if graph[i][j] != 0:  # 끝 값 바로 왼쪽에 있는 값이 0이 아니라면
                    if graph[i][flag] == 0:  # 만약, 끝 값이 0이라면
                        graph[i][flag] = graph[i][j]  # 끝 값 바로 왼쪽에 있는 값이 한칸 옆으로로 이동하는 것이기에 해당 값을 넣는다.
                        graph[i][j] = 0  # 한 칸 왼쪽으로 때문에 원래 있던 자리는 빈자리가 되기에 0을 넣는다.
                        flag -= 1  # 한 번의 이동에서 이미 합쳐진 블록은 다시 합칠 수 없기 때문에 왼쪽으로 한 칸 옮겨 끝 값을 새로 지정한다.
                    elif graph[i][flag] == graph[i][j]:  # 만약, 끝 값과 바로 왼쪽에 있는 값과 같다면
                        graph[i][flag] += graph[i][j]  # 두 값을 더해준다.
                        graph[i][j] = 0  # 끝 블록 바로 왼쪽 블록이 끝 블록과 합쳐졌기에 해당칸은 이제 빈칸이 된다.
                        flag -= 1  # 한 번의 이동에서 이미 합쳐진 블록은 다시 합칠 수 없기 때문에 왼쪽으로 한 칸 옮겨 끝 값을 새로 지정한다.
                    else:  # 만약, 끝 값이 바로 윗 값과 다르다면
                        flag -= 1  # 합쳐질 수 없기 때문에 끝 값을 왼쪽으로 한 칸 옮겨 끝 값을 새로 지정한다.
    return graph


def dfs(graph, cnt):
    global answer
    if cnt == 5: # 5번 했을 때
        for i in range(n):
            for j in range(n):
                answer = max(answer, graph[i][j]) # 배열 내 최대값 찾기
        return

    for i in directions:
        temp_board = move(deepcopy(graph), i) # 유의! 얕은 복사를 하면 서로 다른 부모를 가진 노드들이 서로에게 영향을 미치게 되기에 깊은 복사로 이러한 일을 방지한다.
        dfs(temp_board, cnt + 1)


answer = 0
dfs(board, 0)
print(answer)
