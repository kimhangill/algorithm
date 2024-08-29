def win(arr,n):         # 함수정의
    for i in range(n-1):    
        if i%2==1:          # 홀수이면 진행
            minidx=i        # 최소값 설정
            for j in range(i+1,n):  # 앞에 있는 것이랑 비교할려고 i + 1  ex) i=0 j=1  n인이유 갯수 맞출라고 뒤로 1칸 밀림
                if arr[j]<arr[minidx]: # 뒤 < 앞 이면  minidx는 앞으로 갱신
                    minidx=j
            arr[i], arr[minidx]=arr[minidx], arr[i] # 앞뒤 위치가 바뀜
  
        else:                                               # 짝수이면
            maxidx=i                                        # 최대값 설정
  
            for j in range(i+1,n):                          
               if arr[j]>arr[maxidx]:                            # 뒤 > 앞 뒤가 더크면
                   maxidx=j                                     #최대값 설정
            arr[i],arr[maxidx]=arr[maxidx],arr[i]           # 조건 충족시 앞뒤가 바뀜
    return arr[:10]                                             # 정답을 arr 저장
if __name__=="__main__":        # 처음시작하는 의미
    t=int(input())                      # t = 문제번호
    for i in range(t):
        n=int(input())                  # 10 10개의 숫자 갯수
        arr=list(map(int, input().split())) # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
        answer=win(arr,n)                   
  
        print(f'#{i+1} {" ".join(map(str, answer))}') # 출력