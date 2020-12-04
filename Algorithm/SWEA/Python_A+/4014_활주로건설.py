import sys

sys.stdin = open('input3.txt', 'r')


def check(road):
    global result
    before_val = road[0]
    cnt = 1
    for i in range(1, len(road)):
        if abs(before_val - road[i]) > 1:
            return
        if road[i] > before_val:
            if cnt < X:
                return
            else:
                cnt = 1
        elif road[i] < before_val:
            if i + X > len(road):
                return
            else:
                for j in range(i, i + X):
                    if road[i] != road[j]:
                        return
                cnt = -X + 1
        else:
            cnt += 1
        before_val = road[i]
    result += 1


for tc in range(1, int(input()) + 1):
    N, X = map(int, input().split())
    board = [[int(x) for x in input().split()] for _ in range(N)]
    result = 0
    for b in board:
        check(b)
    for b in list(zip(*board)):
        check(list(b))
    print('#{} {}'.format(tc, result))
