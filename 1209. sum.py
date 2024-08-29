def sumarr(arr):  
    max = -1   # 음수값이 없어서 0보다 작은 수로 초기값 설정
  
    for i in arr:   
        tmp = 0
        for j in i:
            tmp += j
        if tmp >= max:
            max = tmp
  
    for i in range(100):    # 100x100 전체 탐색
        tmp = 0
        for j in range(100):    # 열 총합의 최대값 갱신
            tmp += arr[j][i]    
        if tmp >= max:
            max = tmp
  
    tmp = 0
    for i in range(100):        # 100x100 전체 탐색
        tmp += arr[i][i]        
  
    if tmp >= max:               
        max = tmp                # 왼쪽 우하향 최대값 조회 후 층족시 갱신
  
    tmp = 0
    for i in range(100):        # 100x100 전체 탐색
        tmp += arr[i][99 - i]   
  
    if tmp >= max:
        max = tmp               # 오른쪽 좌하향 대각선 최대값 조회후 충족시 갱신
    return max
if __name__=="__main__":  # 위부터 말고 여기서부터 시작한다는 표시
    for tc in range(10):  # tc=문제번호
        n = int(input())    # 
        arr = []            # 빈 리스트 생성
        for _ in range(100):    # 100
            arr.append(list(map(int, input().split())))     
        answer=sumarr(arr)      
        print(f'#{tc+1} {answer}')  # 출력