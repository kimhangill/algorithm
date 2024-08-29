t=int(input())
for tc in range(1,t+1):
    arr = input()
    s = []
    for a in arr:
        if s and a == s[-1]:
            s.pop()
        else:
            s.append(a)
    print(f'#{tc} {len(s)}')