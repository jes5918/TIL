def bfs(x, result):
    global max_work
    if result <= max_work:
        return
    if x == N:
        if max_work < result:
            max_work = result
        return
    for y in range(N):
        if not idx[y]:
            idx[y] = 1
            bfs(x + 1, result * work[x][y] * 0.01)
            idx[y] = 0


for test_case in range(1, int(input()) + 1):
    N = int(input())
    work = [list(map(int, input().split())) for _ in range(N)]
    idx = [0] * N
    max_work = 0
    bfs(0, 1)

    print('#{} {:6f}'.format(test_case, max_work * 100))