def ks (total_num, page):  # 함수 정의 ()
    lo = 1                  # 제일 낮은 페이지 쪽수
    hi = total_num          # 마지막 페이지 쪽수
    cnt = 0                  
  
    while lo <= hi:         # lo가 hi보다 작거나 같으면 실행
        mid_idx = int((lo + hi) / 2)    # 중간값 설정 = (첫+마지막) 나누기2
        if mid_idx == page:             # 중간값 = 찾는값 같으면 바로 찾음
            return cnt
        elif mid_idx > page:            
            hi = mid_idx                
            cnt = cnt + 1                    
        else:
            lo = mid_idx
            cnt = cnt + 1
    return -1                       # 못찾았으면 -1 리턴
  
T = int(input())   # 반복 횟수
  
for tc in range(1, T+1): # tc = 문제번호 1~3
    P, A, B = map(int, input().split())     # p = 전체 페이지 쪽 수
  
    A_cnt = ks (P, A)
    B_cnt = ks (P, B)
  
  
    # 빨리 펼치는 사람을 저장
    if A_cnt < B_cnt:      
        ans = 'A'
    elif A_cnt > B_cnt:
        ans = 'B'
    else:
        ans = 0
  
    print(f'#{tc} {ans}')