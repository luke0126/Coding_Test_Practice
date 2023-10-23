# 백준 19637번 - if문 좀 대신 써줘

import sys
n,m = map(int, sys.stdin.readline().split())

step = [sys.stdin.readline().split() for _ in range(n)]


for _ in range(m):
    inp = int(sys.stdin.readline())
    left, right = 0, n - 1
    while(left<=right):
        mid = (left+ right) // 2
        if int(step[mid][1]) >= inp:
            right = mid - 1
        else:
            left = mid + 1
            mid = left
    print(step[mid][0])