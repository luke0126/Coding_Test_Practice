# 백준 10815 - 숫자 카드

# 아이디어: dictionary를 통해 시간초과를 해결하며 풀이!

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
compares = list(map(int, input().split()))

dic = {}

for o in compares:
    dic[o] = 0

for c in cards:
    if c in dic:
        dic[c] = 1

for d in dic:
    print(dic[d], end=' ')
