t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = []
    for a in range(n):
        arr.append(list(map(int,input().split())))
 
 
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    max_val = float('-inf')
    for r in range(n):
        for c in range(n):
            temp = arr[r][c]
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < n and 0 <= nc < n:
                    temp = temp + arr[nr][nc]
            if temp > max_val:
                max_val = temp
    print(f'#{tc} {max_val}')