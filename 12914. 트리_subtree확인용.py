T = int(input())  # 문제번호
for tc in range(1, T + 1):
    E, N = map(int, input().split())  # E=5, N=1 간선의 개수, 최상위 번호=1
    arr = list(map(int, input().split()))  # 부모+자식 쌍으로 번호 / 2 1 / 2 5 / 1 6 / 5 3 / 6 4

    L = [0] * (E + 2)  # [0, 0, 0, 0, 0, 0, 0]  # 왼쪽 리스트
    R = [0] * (E + 2)  # [0, 0, 0, 0, 0, 0, 0] # 오른쪽 리스트

    for i in range(0, len(arr), 2):  # len(arr)=10 / 0 2 4 6 8
        p, c = arr[i], arr[i + 1]  # p, c = arr[0], arr[1] p=부모 번호 c=자식번호
        if L[p] == 0:  # L리스트에 0이라면 부모번호에 자식번호추가
            L[p] = c
        else:  # L리스트에 0이 아니라면 R리스트에 부모번호에 자식번호추가
            R[p] = c

    cnt = 0  # 카운트 셀 변수 생성


    def dfs(v):
        global cnt

        if v == 0:
            return
        dfs(L[v])
        cnt += 1
        dfs(R[v])


    dfs(N)
    print(f'#{tc} {cnt}')