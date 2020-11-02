import sys

sys.stdin = open('input7.txt', 'r')


def bus(cnt, now, bat):
    global res
    if cnt < res:
        if now + bat >= N:
            res = cnt
            return
        for i in range(now + 1, now + bat + 1):
            bus(cnt + 1, i, board[i])

for tc in range(1, int(input()) + 1):
    board = list(map(int, input().split()))
    N = res = board[0]
    bus(0, 1, board[1])
    print('#{} {}'.format(tc, res))
