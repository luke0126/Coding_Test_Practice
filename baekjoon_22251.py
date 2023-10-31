# 백준 22251번 - 빌런 호석

def check(target, x_digit):
    global count
    for i in range(1, n+1):
        if i == target:
            continue
        if checkReverse(i, x_digit):
            count += 1

# 반전시킬 수 있는지 확인하는 함수
def checkReverse(target, x_digit):
    target = changeDigit(target)
    gap = 0
    for i in range(k):
        for j in range(7):
            if display[x_digit[i]][j] != display[target[i]][j]:
                gap += 1
                if gap > p:
                    return False
    return True

# 숫자를 배열로 바꾸는 함수
def changeDigit(x):
    result = []
    for i in range(k-1, -1, -1):
        result.append(x % 10)
        x //= 10
    return result


# 입력 받기
n, k, p, x = map(int, input().split())

display = [[1, 1, 1, 0, 1, 1, 1],   
           [0, 0, 1, 0, 0, 0, 1],   
           [0, 1, 1, 1, 1, 1, 0],   
           [0, 1, 1, 1, 0, 1, 1],   
           [1, 0, 1, 1, 0, 0, 1],   
           [1, 1, 0, 1, 0, 1, 1],   
           [1, 1, 0, 1, 1, 1, 1],   
           [0, 1, 1, 0, 0, 0, 1],   
           [1, 1, 1, 1, 1, 1, 1],   
           [1, 1, 1, 1, 0, 1, 1]]   

count = 0

x_digit = changeDigit(x)
check(x, x_digit)
print(count)
