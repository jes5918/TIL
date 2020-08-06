def coloring(li, ax, ay, bx, by, col):
    for x in range(ax, bx + 1):
        for y in range(ay, by + 1):
            li[x][y] += col
    return li

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0 for _ in range(10)] for i in range(10)]
    for i in range(N):
        aX, aY, bX, bY, color = map(int, input().split())
        arr = coloring(arr, aX, aY, bX, bY, color)

    cnt = 0
    for x in range(10):
        for y in range(10):
            if arr[x][y] == 3:
                cnt += 1
    print(f'#{tc} {cnt}')