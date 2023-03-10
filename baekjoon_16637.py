# 백준 16637번 - 괄호 추가하기

n = int(input())
splitMul = input().split('*')
splitAdd = []
temp = []
splitSub = []
answer = 1
for i in splitMul:
    splitAdd.append(i.split('+'))

for i in splitAdd:
    if len(i) == 2:
        temp.append(int(i[0]) + int(i[1]))
    else:
        temp.append(i[0].split('-'))

for i in temp:
    if type(i) is int: # 요소가 int라면
        answer = answer * i # answer에 i값을 곱해서 초기화 시켜준다.

    else: # 요소가 list라면
        if temp.index(i) != 0: # 만약 첫번째 index가 아니라면
            if len(i) == 1:     # 해당 요소값의 길이가 1이라면
                answer = answer * int(i[0]) # answer에 요소 값 만큼 곱해준다.
            elif len(i) == 2:
                answer = answer * int(i[0])
                answer = answer - int(i[1])

        else: # 만약 첫번째 index일 경우
            if len(i) == 1:
                answer = answer * int(i[0])
            else:
                answer = answer * int(i[0])
                answer = answer - int(i[1])
print(splitMul)
print(splitAdd)
print(temp)
print(answer)