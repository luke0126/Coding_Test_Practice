# 백준 1476 - 날짜 계산

e, s, m = map(int, input().split())
year = 1

while True:
    if ((year-e) % 15 == 0) and ((year-s) % 28 == 0) and ((year-m) % 19 == 0):
        break
    year += 1

print(year)
