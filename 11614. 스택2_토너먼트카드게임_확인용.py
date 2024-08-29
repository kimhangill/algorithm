def find_min(s, e):
    if s == e:  # 종료 장치
        return s
    else:
        mid = (s + e) // 2  # 중간 값 장치
        lidx = find_min(s, mid)  # 왼쪽가기 위한 장치
        ridx = find_min(mid + 1, e)  # 오른쪽가기 위한 장치

        if (arr[lidx] == 1 and arr[ridx] == 3) or (arr[lidx] == 2 and arr[ridx] == 1) or (
                arr[lidx] == 3 and arr[ridx] == 2) or (arr[lidx] == arr[ridx]):  # 왼쪽이 이길 경우
            return lidx
        return ridx


T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 사람 숫자
    arr = list(map(int, input().split()))  # 가위 바위 보 순서대로

    ans = find_min(0, N - 1)

    print(f'#{tc} {ans + 1}')