
t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    dr = [-1,1,0,0]
    dc = [0,0,-1,1]

    ans = 0
    for _ in range(m):
        r1, c1, k = map(int, input().split())

        for r in range(4):  # 사각형의 시작과 끝
            for c in range(k+1):
                nr = r1 + dr[r] * c
                nc = c1 + dc[c] * c
                if 0 <= nr < n and 0 <= nc < n:
                    ans = ans + arr[nr][nc]
                    arr[nr][nc] = 0

    print(f'#{tc} {ans}')