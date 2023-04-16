# 백준 1629 - 곱셈

# 아이디어: 시간초과에 유의하여야 한다. 그러기 위해 분할하여 계산하는 분할 정복(divide and conquer) 방식을 사용하여 풀이!

a, b, c = map(int, input().split())


def mul(a, b):
    if b == 1:
        return a % c
    else:
        tmp = mul(a, b // 2)
        if b % 2 == 0:
            return (tmp * tmp) % c
        else:
            return (tmp * tmp * a) % c


print(mul(a, b))
