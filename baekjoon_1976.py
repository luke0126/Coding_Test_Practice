# 백준 1976 - 여행 가자

def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x

n = int(input())
m = int(input())
parent = [i for i in range(n+1)]

for i in range(n):
    li = list(map(int, input().split()))
    for j in range(n):
        if li[j] == 1:
            union(i+1, j+1)

plan = list(map(int, input().split()))
flag = True

for i in range(m-1):
    if find(plan[i]) != find(plan[i+1]):
        flag = False

if flag:
    print("YES")
else:
    print("NO")
