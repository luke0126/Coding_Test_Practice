# 백준 20920번 - 영단어 암기는 괴로워

# 조건 1: 자주 나오는 단어일수록 앞에
# 조건 2: 해당 단어의 길이가 길수록 앞에
# 조건 3: 알파벳 사전 순으로 앞에 있는 단어일수록 앞에
# M보단 긴 단어만 외운다고 생각하면 됨.

# 람다식 정렬 써서 조건 1, 2, 3을 한번에 정렬

import sys
n, m = map(int, sys.stdin.readline().split())
word_dict = {}

for _ in range(n):
    word = sys.stdin.readline().rstrip()

    if len(word) >= m:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

# 순서대로 조건 1, 2, 3
word_dict = sorted(word_dict.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for i in word_dict:
    print(i[0])
    