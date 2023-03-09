# 백준 1541 - 잃어버린 괄호


expression = input().split('-') # 가장 최소값을 구하기 위해서는 '-'를 기준으로 수식을 나누어야한다.
num = [] # '-'를 기준으로 나눈 수식들의 합들을 저장하기 위한 배열

for i in expression:
    total = 0
    tmp = i.split('+') # '+'를 기준으로 분류하여 덧셈을 한다.
    for j in tmp:
        total += int(j)
    num.append(total)

# 이제 배열들의 원소를 하나씩 빼면 된다.

answer = num[0]
for i in range(1, len(num)):
    answer -= num[i]

print(answer)
