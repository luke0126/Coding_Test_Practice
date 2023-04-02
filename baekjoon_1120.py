# 백준 1120 - 문자열

# 아이디어: 앞 뒤에 아무 알파벳이나 추가한다는 조건이 있기에 a의 남는 위치에 b와 같은 알파벳을 추가한다고 생각하면 된다.

a, b = map(str, input().split())
dif = []
for i in range(len(b) - len(a) + 1): # a와 b의 문자열이 같을 때에도 비교를 해야하기 때문에 1을 더해준다.
    count = 0
    for j in range(len(a)):
        if a[j] != b[j + i]: # b의 탐색 시작점을 바꿔가며 a 전체 탐색
            count += 1
    dif.append(count)
print(min(dif))
