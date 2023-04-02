# 백준 4673 - 셀프 넘버

# 아이디어: 주어진 범위에서 생성자가 있는 숫자들을 분류하여 제외시키면 된다,

nonSelf = []
for i in range(1, 10001):
    nonSelf.append(i + sum(map(int, str(i)))) # 생성자가 있는 숫자들을 대입! 즉, 셀프 넘버가 아닌 수들을 넣는다.
    if i not in nonSelf:
        print(i)