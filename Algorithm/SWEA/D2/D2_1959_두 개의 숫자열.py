for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    list_N = list(map(int, input().split()))
    list_M = list(map(int, input().split()))
    res = []
    if N < M:
        for i in range(0, M-N+1):
            tmp = []
            for j in range(N):
                tmp.append(list_N[j] * list_M[j+i])
            res.append(sum(tmp))
    else:
        for i in range(0, N-M+1):
            tmp = []
            for j in range(M):
                tmp.append(list_M[j] * list_N[j+i])
            res.append(sum(tmp))  
    print(f'#{t} {max(res)}')