# 백준 15903 - 카드 합체놀이

n, m = map(int, input().split())
cards = list(map(int, input().split()))

# 합이 가장 작으려면 가장 작은 값과 그 다음으로 작은 값을 더하면 된다.
for _ in range(m):
    cards.sort()
    temp = cards[0] + cards[1]
    cards[0] = temp
    cards[1] = temp

answer = sum(cards)
print(answer)
