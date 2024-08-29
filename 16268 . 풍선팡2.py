t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
 
    max_val = 0
    dr = (-1, 1, 0, 0)
    dc = (0, 0, -1, 1)
    for r in range(n):
        for c in range(m):
            temp = arr[r][c]
            for i in range(4):
                nr = r + dr[i]  # 상하좌우 이동한 좌표
                nc = c + dc[i]
                if 0<=nr<n and 0<=nc<m:
                    temp += arr[nr][nc]  # 좌표 따라서 이동한 값
            if temp > max_val:
                max_val = temp
    print(f'#{tc} {max_val}')
