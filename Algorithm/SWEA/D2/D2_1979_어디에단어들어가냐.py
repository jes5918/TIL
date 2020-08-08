def ro90(li):
    tmp = [[0]*N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            tmp[y][N-x-1] = li[x][y]
    return tmp

def discrim(lists):
    for x in range(N):
        global res
        cnt = 0
        for y in range(N):
            if lists[x][y]:
                cnt += 1
                if y == N-1 and cnt == target:
                    res += 1
                    cnt = 0
            else:
                if cnt == target:
                    res += 1
                cnt = 0
    return res

for tc in range(1, int(input())+1):
    N, target = map(int, input().split())
    puz = [[int(x) for x in input().split()] for _ in range(N)]
    res = 0
    a = discrim(puz)
    res = 0
    b = discrim(ro90(puz))
    print(f'#{tc} {a+b}')
