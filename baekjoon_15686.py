# 백준 15686 - 치킨 배달

# 아이디어: 무작위로 m개를 선택하고 모든 경로 탐색하여 문제 풀이!


from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]


def dfs(num, i):  # n: 조사할 치킨집 수 i: 조사할 치킨집 번호
    global result
    val = 0
    if num == m: # 조사할 치킨집의 수와 m이 같다면
        for h in house:
            hr, hc = h[0], h[1]
            distance = 2 * n

            for s in select:
                sr, sc = s[0], s[1]
                temp = abs(hr - sr) + abs(hc - sc)
                if temp < distance:
                    distance = temp
            val += distance

        if val < result:
            result = min(val, result)
            return

    for idx in range(i, len(chicken)):
        select.append(chicken[idx])
        dfs(num + 1, idx + 1)
        select.pop()


chicken = deque()
house = deque()
select = deque()

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append((i, j))
        elif graph[i][j] == 2:
            chicken.append((i, j))

result = n * 2 * len(house)

for t in range(len(chicken)):
    dfs(0, t)

print(result)
