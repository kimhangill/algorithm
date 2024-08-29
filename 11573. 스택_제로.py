t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    s = []

    for i in arr:
        if i == 0:
            s.pop()
            # i가 0일때 앞의 숫자를 지운다.
        else:  # 0이 아닐때는 다음 것을 추가한다.
            s.append(i)

    print(f'#{tc} {sum(s)}')
