# 백준 2992 - 크면서 작은 수

# 아이디어: 나올 수 있는 수들의 조합을 구해 이들 중 주어진 수보다 큰 것들만 배열에 저장하고 이 배열에서 가장 작은 값을 출력한다.

x = list(input())
result = []


def combi(array, n):
    num = []
    if n == 0:
        return [[]]
    for i in range(len(array)): # 주어진 수들로 조합한다.
        temp = array[:i] + array[i + 1:]
        remain = combi(temp, n - 1)
        for j in remain:
            num.append([array[i]] + j)
    return num


case = combi(x, len(x))
for i in case:
    if int("".join(i)) > int("".join(x)): # 주어진 숫자보다 해당 숫자가 더 크다면
        result.append(int("".join(i))) # 주어진 숫자보다 더 큰 수를 모아두는 배열에 넣는다.

if len(result) == 0:
    print(0)
else:
    print(min(result))
