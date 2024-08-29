dr = [-1, -1, -1, 0, 1, 1, 1, 0]
dc = [-1, 0, 1, 1, 1, 0, -1, -1]

t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    arr = [[0] * n for _ in range(n)]

    mid = n // 2
    arr[mid - 1][mid] = arr[mid][mid - 1] = 1
    arr[mid][mid] = arr[mid - 1][mid - 1] = 2

    for _ in range(m):
        r, c, doll = map(int, input().split())
        r, c = r - 1, c - 1
        arr[r][c] = doll
        for i in range(8):
            nr, nc = r + dr[i], c + dc[i]
            while 0 <= nr < n and 0 <= nc < n:
                if arr[nr][nc] == 0:
                    break
                if arr[nr][nc] == doll:
                    nr, nc = nr - dr[i], nc - dc[i]
                    while r != nr or c != nc:
                        arr[nr][nc] = doll
                        nr, nc = nr - dr[i], nc - dc[i]
                    break
                nr, nc = nr + dr[i], nc + dc[i]

    b = w = 0
    for r in range(n):
        for c in range(n):
            if arr[r][c] == 1:
                b += 1
            if arr[r][c] == 2:
                w += 1
    print(f'#{tc} {b} {w}')