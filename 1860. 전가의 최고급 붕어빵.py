t = int(input())
for tc in range(1, t+1):
    n,m,k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    ans = 'Possible'
    cnt = 0
    for i in range(n):
        cnt +=1
        if (arr[i]//m)*k < cnt:
            ans = 'Impossible'
            break
    print(f'#{tc} {ans}')