from collections import deque

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    Q = deque()
    for i in range(1, n + 1):
        Q.append(i)

    while len(Q) > 1:
        Q.popleft()
        fir = Q.popleft()
        Q.append(fir)

    ans = Q[0]
    print(f'#{tc} {ans}')