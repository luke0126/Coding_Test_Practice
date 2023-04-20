# 백준 10773 - 제로

# 아이디어: 0이 들어오면 pop하고 나머지 숫자가 들어오면 스택에 수를 넣는 방법을 계속하여 배열의 합을 출력

k = int(input())

arr = []
for _ in range(k):
    temp = int(input())
    if temp == 0:
        arr.pop()
    else:
        arr.append(temp)

print(sum(arr))

