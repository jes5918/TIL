import sys
sys.stdin = open('mg.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    mag = [[int(x) for x in input().split()] for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            mag[j][i]

    print('#{} {}'.format(tc, cnt))

