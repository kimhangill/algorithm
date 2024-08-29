dr = [0, 1, 1, 1]
dc = [1, 1, 0, -1]


def check_omok(arr):
    for r in range(N):
        for c in range(N):
            if arr[r][c] == '.': continue
            for i in range(4):
                for j in range(1, 4 + 1):
                    nr, nc = r + dr[i] * j, c + dc[i] * j
                    if nr < 0 or nr >= N or nc < 0 or nc >= N or arr[nr][nc] == '.':
                        break
                else:
                    return 'YES'
    return 'NO'


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [input() for _ in range(N)]

    print(f'#{tc} {check_omok(arr)}')