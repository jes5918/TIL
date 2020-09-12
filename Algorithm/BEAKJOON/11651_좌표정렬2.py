import sys

N = int(input())
xy = []
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    xy.append((a, b))

xy = sorted(xy, key=lambda x: (x[1], x[0]))
for i in range(N):
    for j in range(2):
        print(xy[i][j], end=' ')
    print()