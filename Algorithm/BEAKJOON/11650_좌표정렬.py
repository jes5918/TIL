N = int(input())
xy = []
for i in range(N):
    a, b = map(int, input().split())
    xy.append((a, b))

xy = sorted(xy, key=lambda x: (x[0], x[1]))
for i in range(N):
    for j in range(2):
        print(xy[i][j], end=' ')
    print()