# 백준 20437번 - 문자열 게임 2

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    w = sys.stdin.readline().rstrip()
    k = int(sys.stdin.readline())

    # 각 문자의 개수 딕셔너리
    letter_dict = {}

    for char in w:
        letter_dict[char] = letter_dict.get(char, 0) + 1

    check = False
    max_answer = -1
    min_answer = len(w)

    # 특정 문자열의 위치 index를 저장하는 딕셔너리
    check_dict = {}

    # 모든 문자열에 대해서
    for i in range(len(w)):
        # 해당 문자열이 k개 이하이면 다음 문자
        if letter_dict[w[i]] < k:
            continue

        # k개 이상인 문자를 찾으면 정답이 있음
        check = True
        # 해당 문자열을 key로하고 index리스트를 value로 갖는 딕셔너리
        if w[i] in check_dict:
            check_dict[w[i]].append(i)
        else:
            check_dict[w[i]] = [i]


    for key, value_list in check_dict.items():
        for i in range(len(value_list) - k + 1):
            max_answer = max(max_answer, value_list[i+k-1] - value_list[i] + 1)
            min_answer = min(min_answer, value_list[i + k - 1] - value_list[i] + 1)

    if check:
        print(min_answer, max_answer)
    else:
        print(-1)
