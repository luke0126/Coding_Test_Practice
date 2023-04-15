# 백준 17609 - 회문

# 아이디어: 양쪽 끝점을 비교하면서 같으면 회문, 다르다면 유사회문인지 판단!

def check(left, right, type):
    result = type
    while left < right:
        if str[left] != str[right] and type == 0:
            a = check(left + 1, right, type + 1)
            b = check(left, right - 1, type + 1)
            result = min(a, b)
            return result
        elif str[left] != str[right] and type == 1:
            return 2
        else:
            left += 1
            right -= 1
    return result


n = int(input())
for _ in range(n):
    str = input()
    answer = check(0, len(str) - 1, 0)
    print(answer)
