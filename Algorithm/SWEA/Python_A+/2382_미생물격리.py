import sys

sys.stdin = open('input2.txt', 'r')

delta = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
reverse_dir = [0, 2, 1, 4, 3]
for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    now = {}
    for _ in range(K):
        x, y, num, d = map(int, input().split())
        now[(x, y)] = [[num, d]]

    while M:
        M -= 1
        nextstep = {}
        for point, value in now.items():
            nx = point[0] + delta[value[0][1]][0]
            ny = point[1] + delta[value[0][1]][1]
            if nx == 0 or ny == 0 or nx == N - 1 or ny == N - 1:
                nnum = value[0][0] // 2
                nd = reverse_dir[value[0][1]]
            else:
                nnum = value[0][0]
                nd = value[0][1]

            if (nx, ny) not in nextstep:
                nextstep[(nx, ny)] = [[nnum, nd]]
            else:
                nextstep[(nx, ny)].append([nnum, nd])

        for n in nextstep:
            if len(nextstep[n]) > 1:
                virus = 0
                temp = 0
                for x in nextstep[n]:
                    virus += x[0]
                    if temp < x[0]:
                        temp = x[0]
                        d = x[1]
                nextstep[n] = [[virus, d]]
        now = nextstep

    result = 0
    for res in nextstep.values():
        result += res[0][0]
    print('#{} {}'.format(tc, result))
