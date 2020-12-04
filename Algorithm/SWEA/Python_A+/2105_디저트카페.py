import sys

sys.stdin = open('input2.txt', 'r')

delta = [(-1, -1), (-1, 1), (1, 1), (1, -1)]


def check(x, y, rotate_cnt, dessert_cnt, pa):
    global result
    nx = delta[rotate_cnt][0] + x
    ny = delta[rotate_cnt][1] + y
    if rotate_cnt == 3 and nx == stx and ny == sty:
        result = max(result, dessert_cnt)
        return

    if 0 <= nx < N and 0 <= ny < N:
        if not visited[nx][ny]:
            if board[nx][ny] in pa:
                return
            visited[nx][ny] = True
            pa.append(board[nx][ny])
            check(nx, ny, rotate_cnt, dessert_cnt + 1, pa)
            if rotate_cnt < 3:
                check(nx, ny, rotate_cnt + 1, dessert_cnt + 1, pa)
            pa.remove(board[nx][ny])
            visited[nx][ny] = False


for tc in range(1, int(input()) + 1):
    N = int(input())
    board = [[int(x) for x in input().split()] for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    result = -1
    for i in range(N):
        for j in range(N):
            stx, sty = i, j
            path = [board[i][j]]
            visited[i][j] = True
            check(i, j, 0, 1, path)
            visited[i][j] = False
    print('#{} {}'.format(tc, result))
