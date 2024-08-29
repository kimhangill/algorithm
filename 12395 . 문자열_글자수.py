t = int(input())
for tc in range(1, t+1):
    str1 = input()
    str2 = input()
    v_d = {}
 
    for s1 in str1:
        v_d[s1] = 0
 
    for s2 in str2:
        if s2 in v_d:
            v_d[s2] = v_d[s2] + 1
 
    max_val = 0
    for val in v_d.values():
        if max_val < val:
            max_val = val
 
    print(f'#{tc} {max_val}')