t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    arr = []
    for a in range(n):
        arr.append(list(map(int, input().split())))

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    max_val = 0
    for r in range(n):
        for c in range(m):
            temp = arr[r][c]
            k = temp
            for i in range(4):
                for j in range(1, temp + 1):
                    nr = r + dr[i] * j
                    nc = c + dc[i] * j
                    if 0 <= nr < n and 0 <= nc < m:
                        k = k + arr[nr][nc]
                if k > max_val:
                    max_val = k
    print(f'#{tc} {max_val}')