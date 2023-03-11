# 백준 16637번 - 괄호 추가하기

n = int(input())
splitMul = input().split('*')
splitAdd = []
splitSub = []

exp = []
answer = 1

print('곱하기 기준으로 나눈 배열')
print(splitMul)

for i in splitMul:
    splitAdd.append(i.split('+'))

print('더하기 기준으로 나눈 배열')
print(splitAdd)

for i in splitAdd:
    if len(i) == 1:
        exp.append(int(i[0]))
    elif len(i) == 2:
        exp.append(int(i[0])+int(i[1]))
    else:
        exp.append([i[j: j + 2] for j in range(0, len(i), 2)])

for i in exp:
    if type(i) is list:
        for j in range(len(i)):
            if len(i[j]) == 2:
                i[j] = int(i[j][0])+int(i[j][1])
            else:
                i[j] = int(i[j][0])

print('더하기 한 값 배열')
print(exp)

for i in exp:
    if type(i) is list:
        splitSub.append(i.split('-'))

print('빼기 기준으로 나눈 배열')
print(splitSub)


answer = exp[0]
for i in range(1, len(exp)):
    if type(exp[i]) is list:
        answer = answer * exp[i][0]
        answer = answer + exp[i][1]

print(answer)

# for i in temp:
#     if type(i) is int: # 요소가 int라면
#         answer = answer * i # answer에 i값을 곱해서 초기화 시켜준다.
#
#     else: # 요소가 list라면
#         if temp.index(i) != 0: # 만약 첫번째 index가 아니라면
#             if len(i) == 1:     # 해당 요소값의 길이가 1이라면
#                 answer = answer * int(i[0]) # answer에 요소 값 만큼 곱해준다.
#             elif len(i) == 2:
#                 answer = answer * int(i[0])
#                 answer = answer - int(i[1])
#
#         else: # 만약 첫번째 index일 경우
#             if len(i) == 1:
#                 answer = answer * int(i[0])
#             else:
#                 answer = answer * int(i[0])
#                 answer = answer - int(i[1])
