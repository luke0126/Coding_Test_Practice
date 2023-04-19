# 백준 9012 - 괄호

# 아이디어: 괄호가 쌍이 맞아야 한다. 그러기 위해서 check라는 변수로 쌍을 찾아야하는 괄호를 확인하며 0이 된다면 올바른 문장이라는 것으로 풀이

t = int(input())

for _ in range(t):
    arr = list(input())
    check = 0
    for i in arr:
        if i == '(':
            check += 1
        elif i == ')':
            check -= 1
        if check < 0:
            print('NO')
            break
    if check == 0:
        print('YES')
    elif check > 0:
        print('NO')

