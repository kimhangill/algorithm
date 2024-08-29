t = int(input())
for tc in range(1, t + 1):
    arr = str(input())
    ans = 0
    if arr == arr[::-1]:
        ans = 1
    else:
        ans = 0

    print(f'#{tc} {ans}')