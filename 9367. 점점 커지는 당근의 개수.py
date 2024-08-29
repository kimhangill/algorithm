t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 1
    cnt = 1
    for r in range(1, n):  # 1 2 3 4
        if arr[r - 1] < arr[r]:  # 0 1 2 3 < 1 2 3 4
            cnt += 1
            ans = max(ans, cnt)
        else:
            cnt = 1

    print(f'#{tc} {ans}')