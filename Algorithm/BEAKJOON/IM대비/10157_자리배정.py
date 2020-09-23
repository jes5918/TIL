import sys
R, C = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
if K > R * C:
    print(0)
else:
    arr = [[0] * C for _ in range(R)]
    d = 0  # 방향 0 : 우 , 1 : 하, 2 : 좌 , 3 : 상
    r = 0
    c = 0
    num = 1
    while True:
        arr[r][c] = num
        if num == K:
            break
        num += 1

        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] == 0:
            r, c = nr, nc
        else:
            d = (d + 1) % 4
            r += dr[d]
            c += dc[d]
    print(r + 1, c + 1)