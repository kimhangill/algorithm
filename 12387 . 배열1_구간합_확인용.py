t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
 
    max_val = -float('inf')
    min_val = float('inf')
 
    for i in range(n-m+1):
        sum_val = sum(arr[i:i+m])
 
        if sum_val > max_val:
            max_val = sum_val
        if sum_val < min_val:
            min_val = sum_val
    ans = max_val - min_val
     
    print(f'#{tc} {ans}')