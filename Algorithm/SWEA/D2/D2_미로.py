def findmiro(xx, yy):
    global res
    if (xx, yy) == (13, 13):
        res = 1
        return res
    visit.append((xx, yy))
    for a, b in dxdy:
        nx = xx + a
        ny = yy + b
        if 0 <= nx < 16 and 0 <= ny < 16 and (miro[nx][ny] == 0 or miro[nx][ny] == 3) and ((nx, ny) not in visit):
            findmiro(nx, ny)

for _ in range(10):
    N = int(input())
    miro = [[int(j) for j in input()] for i in range(16)]
    dxdy = [(-1, 0),(1, 0),(0, -1),(0, 1)]
    visit = []
    res = 0
    findmiro(1, 1)
    print(f'#{N} {res}')