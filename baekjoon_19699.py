# 백준 19699번 - 소-난다!

from itertools import combinations
n, m = map(int, input().split())
h = [int(i) for i in input().split()]

arr = list(combinations(h,m))
answer = []

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False  
    return True

for i in arr:
    if isPrime(sum(i)):
        answer.append(sum(i))

answer = set(answer)

answer = sorted(list(answer))

if answer:
    print(' '.join(map(str, answer)))
else:
    print('-1')

