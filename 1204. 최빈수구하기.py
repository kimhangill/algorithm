t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = [0] * 102
 
    for a in arr:
        cnt[a] += 1
 
    max_index = 0
    for a in range(len(cnt)):
        if cnt[a] >= cnt[max_index]:
            max_index = a
 
    print(f'#{tc} {max_index}')