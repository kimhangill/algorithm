T = int(input())  # 첫번째 입력값
for tc in range(1, T + 1):  # tc=문제번호
    N, M = map(int, input().split())  # n= nxn 배열 m=회문길이
    arr = [list(map(str, input())) for _ in range(N)]  # nxn배열 생성

    for i in range(N):  # ㅇ
        for j in range(N - M + 1):  # n배열 - 글자길이
            word_row = arr[i][j:j + M]  # 첫번째 줄에 j에서 회문길이만큼
            if word_row == word_row[::-1]:  # 문자와 회문이 같으면
                print(f"#{tc} {''.join(word_row)}")  # 문자열 집어넣기
                break

            word_col = []

            for k in range(j, j + M):  # 회문길이만큼
                word_col.append(arr[k][i])  #
            if word_col == word_col[::-1]:  # 문자랑 회문이랑 같으면
                print(f"#{tc} {''.join(word_col)}")  # 문제번호랑문제 출력
                break
