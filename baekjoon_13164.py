# 백준 13164 - 행복 유치원

n, k = map(int, input().split())
kids = list(map(int, input().split()))
answer = 0

kids.sort()
gap = []

# 쉽게 생각하면 각 원생들 사이에 칸막이가 있는데 여기서 어떤 칸막이를 치워야 원생들의 키차이가 작을지를 결정하는 것이다.
# 그렇기에 키차이 만큼을 배열로 오름차순으로 배열하고 그 중에서 차이가 적은 칸막이 부터 치우면 된다.
# 이때 5명의 원생이 있는데,
# 4개의 조로 나누려고 하면 1개의 칸막이를 치우면 된다.
# 3개의 조로 나누려고 하면 2개의 칸막이를 치우면 된다.
# 2개의 조로 나누려고 하면 3개의 칸막이를 치우면 된다.
# 1개의 조로 나누려고 하면 4개의 칸막이를 치우면 된다.
# 즉, n명을 k개의 조로 나누려고 하면 n-k 만큼의 칸막이를 치우면 된다.
# 그 중에서 가장 작은 차이만큼을 계산하여야 하므로 차이들을 오름차순으로 배열해서 n-k개 까지의 차이를 더하면 정답이 된다.
for i in range(len(kids)-1):
    gap.append(kids[i+1]-kids[i])

gap.sort()
print(sum(gap[:n-k]))