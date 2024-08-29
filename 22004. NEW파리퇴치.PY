t = int(input())
for tc in range(1, t+1):
    n, h,w = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    max_val = 0
    for r in range(n-h+1):
        for c in range(n-w+1):
            sum_val = 0

            for i in range(h):
                for j in range(w):
                    dr = r+i
                    dc = c+j
                    if 0<=dr<n and 0<=dc<n:
                        sum_val = sum_val+ arr[dr][dc]
            for i in range(1,h-1):
                for j in range(1,w-1):
                    dr = r+i
                    dc = c+j
                    if 0 <= dr <n and 0<=dc<n:
                        sum_val = sum_val - arr[dr][dc]

            if sum_val > max_val:
                max_val = sum_val
    print(f'#{tc} {max_val}')

# t = int(input())
# for tc in range(1, t + 1):
#     n, h,w = map(int, input().split())
#     arr = []
#     for i in range(n):
#         arr.append(list(map(int, input().split())))
#
#     max_val = 0
#     dr = (-1, -1, -1, 0, 0, 1, 1, 1)
#     dc = (-1, 0, 1, -1, 1, -1, 0, 1)
#     for r in range(n):
#         for c in range(n):
#             temp = arr[r][c]
#             k = temp
#             for i in range(8):
#                 nr = r + dr[i]  # 상하좌우 이동한 좌표
#                 nc = c + dc[i]
#                 if 0 <= nr < n and 0 <= nc < n:
#                     temp += arr[nr][nc]  # 좌표 따라서 이동한 값
#             temp = temp -k
#             if temp > max_val:
#                 max_val = temp
#     print(f'#{tc} {max_val}')
