for tc in range(1, 11):         #문제번호
    dump = int(input())         # 덤프횟수
    arr = list(map(int, input().split()))  #덤프 목록
 
    for d in range(dump):           # 덤프 개수만큼 순회
        max_h, min_h = arr[0], arr[0]   # 최대값, 최소값 초기 설정
 
        for i in range(100):      # 최대가로길이만큼 모두다 순회하겠다
            if arr[i] >= max_h:   # 순회하면서 최대값 갱신
                max_h = arr[i]
                idx_max = i         # 최대값 인덱스 확보
 
            if arr[i] <= min_h:     # 최소값 갱신
                min_h = arr[i]
                idx_min = i         # 최소값 인덱스 확보
 
        arr[idx_max] -= 1           # 최대값 -1 / 덤프
        arr[idx_min] += 1           # 최소값 +1 / 덤프
 
 
    max_h, min_h = arr[0], arr[0]   # 최대값, 최소값 초기설정
    # 최대 높이, 최소 높이 찾기 / 갱신
    for i in range(100):            # 가로길이 100
        if arr[i] >= max_h:         # 최대값 확인
            max_h = arr[i]
        if arr[i] <= min_h:         # 최소값 확인
            min_h = arr[i]
 
    print(f'#{tc} {max_h - min_h}')
