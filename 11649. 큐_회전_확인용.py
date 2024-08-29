from collections import deque

t = int(input())
for tc in range(1, t + 1):
    n, m = list(map(int, input().split()))
    arr = deque(list(map(int, input().split())))

    for i in range(1, m + 1):
        fir = arr.popleft()
        arr.append(fir)

    print(f'#{tc} {arr[0]}')