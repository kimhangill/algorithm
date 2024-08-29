def fibo(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 3
    elif n > 2:
        return fibo(n - 1) + fibo(n - 2) * 2


t = int(input())
for tc in range(1, t + 1):
    n = int(input()) // 10

    print(f'#{tc} {fibo(n)}')