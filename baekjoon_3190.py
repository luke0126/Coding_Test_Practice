# 백준 3190 - 뱀

# 아이디어: 한 칸씩 옮겨가며 사과 있을 경우 뱀의 위치를 나타내는 큐 값에 사과 위치를 넣어주고 없다면 뱀의 꼬리 부분을 pop하고 머리 부분을 다음 좌표값으로 넣어 위치 이동시킨다.
# 방향을 고려해주는 함수를 통해 문제 조건에서 주어진 시간 만큼 지나면 회전하게 해주며 문제의 정답을 구한다.

from collections import deque

n = int(input())
graph = [[0] * n for _ in range(n)]
k = int(input())
for _ in range(k):
    ax, ay = map(int, input().split())
    graph[ax - 1][ay - 1] = 1

trans = []
l = int(input())
for _ in range(l):
    time, c = map(str, input().split())
    trans.append((int(time), c))

move = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # 북, 동, 남, 서 -> 시계 방향


def turn(direction, current):
    if direction == 'L':
        current = (current + 3) % 4
        return current
    else:
        current = (current + 1) % 4
        return current


snake = deque()
snake.append((0, 0))
move_index = 1
x, y = 0, 0
count = 0

while True:
   # print(count, '초 지남!')
   # print(snake)
    for i in trans:
        if i[0] == count:
            move_index = turn(i[1], move_index)
     #       print('회전!')
    nx = x + move[move_index][0]
    ny = y + move[move_index][1]
    if nx < 0 or nx >= n or ny < 0 or ny >= n or (nx, ny) in snake:
        count += 1
     #   print('종료!')
        break
    if graph[ny][nx] == 1: # 사과가 있다면 (유의! 수평으로 움직이는 것은 graph[a][b]에서 b 값이 변하는 것을 생각해야 함.)
        graph[ny][nx] = 0
        x, y = nx, ny
        snake.append((x, y))
     #   print('사과 있다! 길이 증가!')
    else: # 사과가 없다면
        x, y = nx, ny
        snake.popleft() # 기존에 있던 뱀의 위치의 가장자리를 빼주고
        snake.append((x, y)) # 새로 옮긴 좌표로!
       # print('사과 없다!')
    count += 1

print(count)
