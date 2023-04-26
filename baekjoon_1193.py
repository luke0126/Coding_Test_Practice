# 백준 1193번 - 분수 찾기

# 아이디어: 지그재그 규칙을 찾아서 풀이ㅁ

num = int(input())

line = 1
while num > line:
    num -= line
    line += 1

if line % 2 == 0:
    a = num
    b = line - num + 1
else:
    a = line - num + 1
    b = num

print(a, '/', b, sep='')
