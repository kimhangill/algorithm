t = int(input())
for tc in range(1, t + 1):
    V, E = map(int, input().split())

    arr = []
    for i in range(E):
        arr.append(list(map(int, input().split())))

    G = [[0] * (V + 1) for _ in range(V + 1)]
    visited = [0] * (V + 1)

    start, end = map(int, input().split())

    ############양방향 >> 단방향 수정해야 할 부분###############
    for i in arr:
        u, v = i[0], i[1]
        G[u][v] = 1


    def dfs(v):
        visited[v] = 1
        for w in range(1, V + 1):
            if G[v][w] == 1 and not visited[w]:
                dfs(w)


    dfs(start)
    if visited[end] == 1:
        ans = 1
    else:
        ans = 0
    print(f'#{tc} {ans}')