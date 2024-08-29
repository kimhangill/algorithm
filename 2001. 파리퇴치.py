t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    max = 0
    for r in range(n-m+1):
        for c in range(n-m+1):
            sum = 0
            for i in range(m):
                for j in range(m):
                    sum = sum + arr[r+i][c+j]
            if sum > max:
                max = sum
    print(f'#{tc} {max}')