import sys
sys.stdin = open("ot.txt", "r")

def othelo(x, y):
    # 바꿔야할 좌표를 저장할 temp변수 설정
    temp = []
    # 돌 놓기
    arr[x][y] = bw
    # 델타값에 튜플로 저장되어 있기 때문에 dx, dy로 불러옴
    for dx, dy in delta:
        nx = x + dx
        ny = y + dy
        while True:
            # 행렬 범위 넘어가면 브레이크
            if (nx < 0 or nx > N - 1) or (ny < 0  or ny > N - 1):
                temp = []
                break
            # 돌이 없는 빈칸일때 브레이크
            if not arr[nx][ny]:
                temp = []
                break
            # 같은돌이 나오면 브레이크
            if arr[nx][ny] == bw:
                break
            # 다른돌이 나오면 temp에 좌표 저장
            # 다음칸으로 이동하기 위해 같은 dx, dy를 더해서 이동
            else:
                temp.append((nx, ny))
                nx += dx
                ny += dy
        # 바꿔야할 오셀로가 들어 있는 temp의 좌표들에게 값 변화시킴
        for rx, ry in temp:
            if bw == 1:
                arr[rx][ry] = 1
            else:
                arr[rx][ry] = 2

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [[0]*N for _ in range(N)]

    # 8 방향 델타
    delta = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    # 시작 2x2에 채워넣는 과정
    start = N // 2
    arr[start-1][start-1] = 2
    arr[start][start] = 2
    arr[start-1][start] = 1
    arr[start][start-1] = 1

    # 1이 흑 2가 백
    for _ in range(M):
        x, y, bw = map(int, input().split())
        # x-1, y-1한 이유는
        othelo(x-1, y-1)

    # 끝난 후 각각 갯수 찾기
    black, white = 0, 0
    # for i in range(N):
    #     for j in range(N):
    #         if arr[i][j] == 1:
    #             black += 1
    #         elif arr[i][j] == 2:
    #             white += 1
    for a in arr:
        black += a.count(1)
        white += a.count(2)
    print('#{} {} {}'.format(tc, black, white))



