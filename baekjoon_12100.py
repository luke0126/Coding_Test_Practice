# 백준 12100 - 2048(easy)

# 아이디어: 5번 실행했을 때 최대값을 구하는 것이기에 각각의 상황을 트리로 생각하여 dfs로 탐색하는 방식으로 해결

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

print(board)


def move(map, direction):
    for i in range(n):
        for j in range(n):
            if direction == 'u': # 상
                print('상')
                if i > 0 : # 블록이 맨 위에 있지 않을 때
                    if map[i][j] == map[i-1][j]: # 서로 같은 수의 블럭이라면
                        map[i-1][j] = map[i-1][j] + map[i][j]
                        move(map, direction)

            elif direction == 'd': # 하
                print('하')
                if 0 < i < n: # 블록이 맨 위에 있지 않을 때
                    if map[i][j] == map[i+1][j]: # 서로 같은 수의 블럭이라면
                        map[i+1][j] = map[i+1][j] + map[i][j]

            elif direction == 'l': # 좌
                print('좌')

            else: # 우
                print('우')


for _ in range(5):
    move()
