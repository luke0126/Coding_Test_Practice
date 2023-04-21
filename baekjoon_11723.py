# 백준 11723번 - 집합

# 아이디어: 각 명령어에 따라 집합에 값을 적절히 처리

import sys
input = sys.stdin.readline
m = int(input())
S = set()
for _ in range(m):
    temp = input().split()
    if len(temp) == 1:
        order = temp[0]
    else:
        order, num = temp

    if order == "add":
        S.add(int(num))
    elif order == "remove":
        if int(num) in S:
            S.remove(int(num))
    elif order == "check":
        if int(num) in S:
            print(1)
        else:
            print(0)
    elif order == "toggle":
        if int(num) in S:
            S.remove(int(num))
        else:
            S.add(int(num))
    elif order == "all":
        S = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
    elif order == "empty":
        S.clear()
