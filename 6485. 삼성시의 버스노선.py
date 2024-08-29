for tc in range(1, t + 1):
    n = int(input())
    cnt = [0] * 5001
    for r in range(n):
        a, b = map(int, input().split())
        for c in range(a, b + 1):
            cnt[c] = cnt[c] + 1

    p = int(input())
    ans = []
    for _ in range(p):
        bus_stop = int(input())
        ans.append(cnt[bus_stop])

    ans = ' '.join(map(str, ans))
    print(f'#{tc} {ans}')