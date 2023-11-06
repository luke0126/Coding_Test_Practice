# 백준 2138번 - 전구와 스위치

n = int(input())
current = list(map(int, input().rstrip()))
target = list(map(int, input().rstrip()))

# 전구 상태 변경
def onoff(num):
    if num == 0:
        num = 1
    else:
        num = 0
    return num

# 목표로 바꾸는 함수
def switch(c, cnt):
    count = cnt
    if count == 1:
        c[0] = onoff(c[0])
        c[1] = onoff(c[1])
    for i in range(1, n):
        if c[i-1] != target[i-1]:
            count += 1
            c[i-1] = onoff(c[i-1])
            c[i] = onoff(c[i])
            if i != n-1:
                c[i+1] = onoff(c[i+1])
    if c == target:
        return count
    else:
        return -1

res1 = switch(current[:], 0)
res2 = switch(current[:], 1)
if res1 >= 0 and res2 >= 0:
    print(min(res1, res2))
elif res1 >= 0 and res2 < 0:
    print(res1)
elif res1 < 0 and res2 >= 0:
    print(res2)
else:
    print(-1)
