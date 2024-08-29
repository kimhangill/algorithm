t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input()))

    ans = 0
    cnt = 0
    for val in arr:
        if val == 1:
            cnt += 1
            ans = max(ans, cnt)
        else:
            cnt = 0
    print(f'#{tc} {ans}')