'''
어떻게 풀어볼까
일단 2차원 배열로 입력받고


'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    li = list([int(x) for x in input().split()] for _ in range(N))
    result = []
    cnt_x = 0
    cnt_y = 0
    for x in range(N):
        for y in range(N):
            if li[x][y] != 0:
                cnt_x += 1
            if li[x][y] == 0:
                for z in range(x, N):
                    if li[z][y-1] != 0:
                        cnt_y += 1
                    if li[z][y-1] == 0:
                        result += [cnt_x, cnt_y]
                        cnt_x = 0
                        cnt_y = 0
                        break
    print(result)

            
            