import sys

sys.stdin = open('input3.txt', 'r')
from itertools import combinations


def check(com):
    res = 0
    temp = [[987654321] for _ in range(len(home))]
    for c in com:
        res += c[2]
        i = 0
        while i < len(home):
            temp[i] += [abs(c[0] - home[i][0]) + abs(c[1] - home[i][1])]
            i += 1
    for t in temp:
        res += min(t)
    return res


def combination():
    res = 987654321
    for k in range(1, len(chicken) + 1):
        for combi in combinations(chicken, k):
            res = min(res, check(combi))
    return res


for tc in range(1, int(input().rstrip()) + 1):
    N = int(input().rstrip())
    board = [[int(x) for x in input().rstrip().split()] for _ in range(N)]
    chicken = []
    home = []
    for i in range(N):
        for j in range(N):
            if board[i][j] > 1:
                chicken += [[i, j, board[i][j]]]
            elif board[i][j] == 1:
                home += [[i, j]]
    print('#{} {}'.format(tc, combination()))
