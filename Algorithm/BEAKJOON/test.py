import sys
sys.stdin = open('배열돌리기3.txt','r')

def rotate(d,r):
    arr_new = [[0] * M for _ in range(N)]
    if d == 1:
        for i in range(N):
            for j in range(M):
                arr_new[N-1-i][j] = arr[i][j]
        return arr_new
    elif d ==2:
        for i in range(N):
            for j in range(M):
                arr_new[i][M-1-j] = arr[i][j]
        return arr_new
    elif d == 3:
        arr_new = [[0] * N for _ in range(M)]
        for i in range(N):
            for j in range(M):
                arr_new[j][N-1-i] = arr[i][j]
        return arr_new
    elif d == 4:
        arr_new = [[0] * N for _ in range(M)]
        for i in range(N):
            for j in range(M):
                arr_new[M-j-1][i] = arr[i][j]
        return arr_new
    elif d == 5 :
        n = N//2
        m =  M//2
        for i in range(N):
            for j in range(M):
                if i < n and j < m:
                    arr_new[i][j+m] = arr[i][j]
                elif i < n and j >= m:
                    arr_new[i+n][j] = arr[i][j]
                elif i >=n and j >= m:
                    arr_new[i][j-m] = arr[i][j]
                elif i >= n and j < m:
                    arr_new[i-n][j] = arr[i][j]
        return arr_new
    elif d == 6 :
        n = N//2
        m =  M//2
        for i in range(N):
            for j in range(M):
                if i < n and j < m:
                    arr_new[i+n][j] = arr[i][j]
                elif i < n and j >= m:
                    arr_new[i][j-m] = arr[i][j]
                elif i >=n and j >= m:
                    arr_new[i-n][j] = arr[i][j]
                elif i >= n and j < m:
                    arr_new[i][j+m] = arr[i][j]
        return arr_new

T = int(input())
for t in range(T):
    N,M,R = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    d = list(map(int,input().split()))
    for k in d:
        print(k)
        arr = rotate(k,R)
        print(arr)


    if k == 3 or k == 4:
        for i in range(M):
            for j in range(N):
                print(arr[i][j] , end= ' ')
            print()
        print()
    else:
        for i in range(N):
            for j in range(M):
                print(arr[i][j] , end= ' ')
            print()
        print()