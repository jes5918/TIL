for tc in range(1, 11):
    N = int(input())
    ap = list(map(int, input().split()))
    cnt = 0
    for i in range(2, N-2):
        b = max(ap[i-2], ap[i-1], ap[i+1], ap[i+2])
        if ap[i] > b:
            cnt += ap[i] - b
    print(f'#{tc} {cnt}')