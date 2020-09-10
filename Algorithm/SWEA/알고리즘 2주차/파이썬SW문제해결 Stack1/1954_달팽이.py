for tc in range(1, int(input())+1):
    N = int(input()) # 행렬의 크기
    delta = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 우 하 좌 상
    dalpang = [[0] * N for _ in range(N)] # 0으로 채워진 빈 행렬 초기화
    direction, row, col = 0, 0, 0 # 방향, 좌표 초기화
    num = 1 # 배열에 차례로 넣을 숫자

    while num <= N * N:
        dalpang[row][col] = num
        num += 1
        new_row = row + delta[direction][0]
        new_col = col + delta[direction][1]
        if 0 <= new_row < N and 0 <= new_col <N and dalpang[new_row][new_col] == 0:
            row, col = new_row, new_col
        else:
            direction = (direction+1) % 4
            row += delta[direction][0]
            col += delta[direction][1]

    print("#{}".format(tc))
    for i in range(N):
        print(*dalpang[i])