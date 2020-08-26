import numpy as np

def horizontal(x, n, m):
    result = ''
    for i in x:
        for j in range(n-m+1):
            a = i[j:j+m]
            for k in range(m//2):
                if a[k] != a[-(k+1)]:
                    break
            else:
                result += a
    return result

def vertical(a, n, m):
    result = np.array(a)
    for x in range(n):
        for y in range(n-m+1):
            for i in range(m//2):
                if a[x][y] != a[x][m-y]:
                    break
            else:
                re = result[x:(x-1),y:(m-y)]
    return result

for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [input() for i in range(N)]
    result = horizontal(arr, N, M)
    if result == False:
        result = vertical(arr, N, M)

    print(f'#{t} {result}')