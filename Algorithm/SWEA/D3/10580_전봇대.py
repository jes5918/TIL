import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    pole = [list(map(int, input().split())) for _ in range(N)]
    pole.sort(key=lambda x: x[0])
    cnt = 0
    for i in range(N):
        res = pole[i][1]
        for j in range(i + 1, N):
            if pole[j][1] < res:
                cnt += 1
    print('#{} {}'.format(tc, cnt))
