import sys
sys.stdin = open("input2.txt", "r")

def udlr(xx, yy, cnt, cnt_num):
    for i in range(4):
        pointX = xx + dx[i]
        pointY = yy + dy[i]
        if N > pointX >= 0 and N > pointY >= 0:  # 상하좌우 index 값이 0보다 같거나크고 N보다 작을때
            if arr[xx][yy] + 1 == arr[pointX][pointY]:
                if cnt == 1:
                    cnt_num = arr[xx][yy]
                cnt += 1
                return udlr(pointX, pointY, cnt, cnt_num)
            else:
                if cnt_num == -1:
                    break
                else:
                    dict_cnt[cnt_num] = cnt
                    break

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[int(x) for x in input().split()] for y in range(N)]
    dx = [0, 0, -1, 1] # 위 아래
    dy = [-1, 1, 0, 0] # 좌 우
    maxcnt_num = -1
    dict_cnt = {}
    for x in range(N):
        for y in range(N):
            cnt = 1
            maxcnt_num = -1
            udlr(x, y, cnt, maxcnt_num)
    print(dict_cnt)
    # print(f'#{tc} {maxcnt_num} {cnt}')