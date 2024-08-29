def bfs(s, g, lst):
    visited = [0] * (V + 1)  # 방문리스트 만들기
    q = []  # q만들기
    q.append(s)  # 인큐
    visited[s] = 1  # 방문 시작점 1로 표시

    # 탐색
    while q:
        v = q.pop(0)  # 디큐
        if v == g:  # 정점의 숫자와 도착지점이랑 같으면
            return visited[v] - 1  # 방문횟수 -1
        else:
            for w in lst[v]:  # 인접 접점 찾기
                if visited[w] == 0:  # 만약 큐안에없다면
                    q.append(w)  # 인큐
                    visited[w] = visited[v] + 1  # visit 방문표시
    else:
        return 0


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())  # v =점개수 e=간선
    arr = [list(map(int, input().split())) for _ in range(E)]  # 간선 수만큼 리스트안에
    S, G = map(int, input().split())  # s = 시작점  g = 도착지점

    match = [[] for _ in range(V + 1)]  #

    # 인접 정점 리스트 만들기
    for i in range(E):
        v1, v2 = arr[i][0], arr[i][1]
        match[v1].append(v2)
        match[v2].append(v1)

    print(f'#{tc} {bfs(S, G, match)}')