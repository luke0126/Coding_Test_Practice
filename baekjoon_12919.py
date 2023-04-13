# 백준 12919 - A와 B 2

# 아이디어: t에서 백트래킹하며 조건 1, 2를 만족시키게 끔 문자를 하나씩 빼서 s를 만들어보면서 풀이!


s = list(input())
t = list(input())
check = False


def dfs(graph):
    global check

    if len(graph) == len(s):  # 문자를 하나씩 빼가면 백트래킹한 것과 s가 같다면
        if graph == s:
            check = True
        return

    if graph[0] == "B":
        graph.reverse()
        graph.pop()
        dfs(graph)
        graph.append("B")
        graph.reverse()

    if graph[-1] == "A":
        graph.pop()
        dfs(graph)
        graph.append("A")


dfs(t)

if check:
    print(1)
else:
    print(0)
