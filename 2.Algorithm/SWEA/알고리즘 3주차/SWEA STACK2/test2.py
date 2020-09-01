import sys
sys.stdin = open("input5.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[int(x) for x in input().split()] for y in range(N)]
    dxdy = [(-1, 0),(1, 0),(0, -1),(0, 1)]
    res = []
    for x in range(N):
        for y in range(N):
            tmp = []
            cnt = 1
            tmp.append([x, y])
            while tmp:
                [xx, yy] = tmp.pop()
                for a, b in dxdy:
                    pointX = xx + a
                    pointY = yy + b
                    if N > pointX >= 0 and N > pointY >= 0:  # 상하좌우 index 값이 0보다 같거나크고 N보다 작을때
                        if arr[xx][yy] + 1 == arr[pointX][pointY]:
                            tmp.append([pointX, pointY])
                            cnt += 1
                            break
            res += [[arr[x][y], cnt]]
    res = sorted(res, key = lambda x : (-x[1], x[0]))
    print(f'#{tc} {res[0][0]} {res[0][1]}')