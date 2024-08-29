for tc in range(1, 11):  # 문제 번호
    n = int(input())  # 문제 길이
    arr = input()  # 주어진 입력값

    st = []  # 연사자 모음
    num = []  # 피연산자 모음
    sum_1 = 0  # 정수 총합

    for a in arr:  # 주어진 입력값 돌리기
        if a.isdecimal():  # 0~9숫자인경우
            num.append(a)  # 피연사자 모음에 추가
            sum_1 = sum_1 + int(a)  # 추가동시에 총합을 갱신
        else:  # 0~9숫자가 아닌경우
            num.append(a)  # 피연사자 모음에 추가
    print(f'#{tc} {sum_1}')  # 출력값
