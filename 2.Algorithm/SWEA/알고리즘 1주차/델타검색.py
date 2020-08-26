arr = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
N = len(arr)
M = len(arr[0])

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for x in range(N):
    for y in range(M):
        for i in range(4):
            testX = x + dx[i]
            testY = y + dy[i]
            if 0 <= testX < N and 0 <= testY < M:
                print(arr[testX][testY], end = ' ')