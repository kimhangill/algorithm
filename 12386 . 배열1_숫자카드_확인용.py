t = int(input())                        # 문제 개수
  
for tc in range(1, t + 1):          # tc=문제 번호
    n  = int(input())                # 카드의 개수
    m = list(map(int, input()))    # 카드의 숫자들
      
    counts = [0] * 10              # 카운팅하기위한 초기 설정값 0-9
    for i in range(n):              # 카드의 개수만큼 반복
        counts[m[i]] += 1          # 카드의 숫자의 인덱스에 +1씩 개수만큼 추가
  
    max_idx = 0                    # 최대 인덱스 초기값 설정 
    for i in range(10):             # 각 자리 확인
        if counts[max_idx] <= counts[i]:      # 최대값 갱신
            max_idx = i                        
            
  
    print(f'#{tc} {max_idx} {counts[max_idx]}')