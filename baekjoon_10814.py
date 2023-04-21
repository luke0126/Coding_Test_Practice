# 백준 10814 - 나이순 정렬

# 아이디어: 람다식을 이용하여 나이 기준으로 정렬

n = int(input())
arr = []
for _ in range(n):
    age, name = map(str, input().split())
    age = int(age)
    arr.append((age, name))

arr.sort(key=lambda x: x[0])

for i in arr:
    print(i[0], i[1])
