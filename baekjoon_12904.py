# 백준 12904 - A와 B

# 아이디어: s 를 t 로 만들 수 있다는 것은 t를 해당 조건대로 문자를 하나씩 빼서 만들 수 있다는 뜻이다. 이를 이용해 풀이!

s = list(input())
t = list(input())
possible = False
while t:
    # 조건 1: 문자열의 뒤에 A를 추가하는 조건 => 이 과정을 반대로 생각하면 마지막에 A라면 조건 1을 수행했다는 것
    if t[-1] == 'A': # t의 마지막이 A라면
        t.pop() # A 빼주기
    # 조건 2: 문자열을 뒤집고 뒤에 B를 추가하는 조건 => B라면 B를 빼주고 문자열 뒤집기
    elif t[-1] == 'B':
        t.pop()
        t.reverse()
    if s == t:
        possible = True
        break

if possible:
    print(1)
else:
    print(0)
