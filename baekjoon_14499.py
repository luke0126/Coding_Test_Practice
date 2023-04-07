# 백준 14499 - 주사위 굴리기

# 아이디어: 주사위를 굴렸을 때 눈이 바뀌는 것을 고려하면서 시뮬레이션 하면서 구현

n, m, x, y, k = map(int, input().split()) # n: 세로, m: 가로, x: x좌표, y: y좌표, k: 명령어 갯수
board = [list(map(int, input().split())) for _ in range(n)]
order = list(map(int, input().split()))
bottom, east, north, south, west, top = 0, 0, 0, 0, 0, 0
dice = [bottom, east, north, south, west, top]


def roll(_dice, ord):
    btm, est, nrth, sth, wst, tp = _dice[0], _dice[1], _dice[2], _dice[3], _dice[4], _dice[5]
    if ord == 1: # 동쪽으로 움직이는 명령어
        _dice[0], _dice[1], _dice[2], _dice[3], _dice[4], _dice[5] = est, tp, nrth, sth, btm, wst
        #print('동쪽으로 이동!')
        return _dice
    elif ord == 2: # 서쪽으로 움직이는 명령어
        _dice[0], _dice[1], _dice[2], _dice[3], _dice[4], _dice[5] = wst, btm, nrth, sth, tp, est
        #print('서쪽으로 이동!')
        return _dice
    elif ord == 3: # 북쪽으로 움직이는 명령어
        _dice[0], _dice[1], _dice[2], _dice[3], _dice[4], _dice[5] = nrth, est, tp, btm, wst, sth
        #print('북쪽으로 이동!')
        return _dice
    else: # 남쪽으로 움직이는 명령어
        _dice[0], _dice[1], _dice[2], _dice[3], _dice[4], _dice[5] = sth, est, btm, tp, wst, nrth
        #print('남쪽으로 이동!, 주사위:')
        return _dice


for ord in order:
    #print(x, y)
    if ord == 1: # 동쪽으로 이동
        nx = x
        ny = y + 1
        #print('동')
    elif ord == 2: # 서쪽으로 이동
        nx = x
        ny = y - 1
        #print('서')
    elif ord == 3: # 북쪽으로 이동
        nx = x - 1
        ny = y
        #print('북')
    else: # 남쪽으로 이동
        nx = x + 1
        ny = y
        #print('남')
    if 0 <= ny < m and 0 <= nx < n:
        x, y = nx, ny
        dice = roll(dice, ord)
        if board[x][y] == 0: # 칸에 적혀있는 숫자가 0이라면
            board[x][y] = dice[0]  # 칸에 주사위 밑면 숫자를 복사한다.
            #print('주사위: ', dice)
            print(dice[5]) # 주사위 윗면 출력
        else: # 칸에 적혀있는 숫자가 0이 아니라면
            dice[0] = board[x][y] # 주사위 밑면에 해당 칸의 숫자를 복사한다.
            board[x][y] = 0 # 해당 칸은 0으로 만들어 준다.
            #print('주사위: ', dice)
            print(dice[5]) # 주사위 윗면 출력
    else:
        continue

