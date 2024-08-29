T = int(input())  # 첫번째 입력값 / 문제 개수


def dict_oper(A, B, oper):  # 계산식 함수 만들기
    if oper == '+':  # 연산자가 +일 경우
        return A + B  # A+B
    elif oper == '-':  # 만약 연산자가 -일 경우
        return A - B  # A-B
    elif oper == '*':  # 만약 연산자가 *일 경우
        return A * B  # A*B
    elif oper == '/':  # 만약 연산자가 / 일 경우
        return int(A / B)  # A/B


oper = ['+', '-', '*', '/']  # oper가
for tc in range(1, T + 1):  # tc = 문제번호
    arr = list(input().split())  #
    stack = []  # stack = False
    for i in range(len(arr)):  # 문자 개수만큼 돌린다
        if arr[i] == '.':  # 만약 .을 만난다면
            if not stack or len(stack) >= 2:  # 스택에 원소들이 없으면 = not stack 또는 스택안에 길이가 2개 이상이면 / 1개여야함
                ans = 'error'  # error
                break  # 멈춘다
            ans = stack.pop()  # stack에서 마지막것을 꺼내라

        elif arr[i] not in oper:  # 만약 arr[i]이 [+ - * /]와 같은게 없다면
            stack.append(arr[i])  # 스택에 arr[i]를 추가
        else:
            if len(stack) < 2:  # stack안에 길이가 2보다 작은면
                ans = 'error'  # error / 1개인 경우 계산할수 없으므로
                break  # 멈춘다
            B = stack.pop()  # 스택에서 마지막 꺼를 뺴라
            A = stack.pop()  # 스택에서 마지막 꺼를 뺴라
            result = dict_oper(int(A), int(B), arr[i])  # 결과값(정상이면 1개) = 위의 계산기를 결과값에 넣는다
            stack.append(result)  # 스택에 결과값 넣기
    print(f'#{tc} {ans}')  # 출력 문제번호랑 답을