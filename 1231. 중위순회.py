for tc in range(1, 11):
    V = int(input())
    # 정점 번호가 1번부터 V번이기 때문에
    L = [0] * (V + 1)
    R = [0] * (V + 1)
    match = [0] * (V + 1)
    for _ in range(V):
        info = list(input().split())
        p = int(info[0])
        match[p] = info[1]
        c_lst = [int(i) for i in info[2:]]
        for c in c_lst:
            if L[p] == 0:
                L[p] = c
            else:
                R[p] = c
    print(f'#{tc}', end=' ')


    def dfs(v):
        if v == 0:
            return
        dfs(L[v])
        print(match[v], end='')
        dfs(R[v])


    dfs(1)
    print()