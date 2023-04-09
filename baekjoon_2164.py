# 백준 2164 - 카드 2

# 아이디어: deque을 이용하여 제일 위에 있는 카드를 없애고 그 다음 카드를 맨 뒤로 보내면서 반복문을 돌며 문제 해결

from collections import deque
n = int(input())
card = deque([i for i in range(1, n+1)])

while len(card) > 1:
    card.popleft()
    card.append(card.popleft())

print(card[0])
