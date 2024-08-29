t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    max_val = float('-inf')
    min_val = float('inf')
 
    for i in arr:
        if i > max_val:
            max_val = i
        elif i < min_val:
            min_val = i
    ans = max_val -min_val
    print(f'#{tc} {max_val-min_val}')