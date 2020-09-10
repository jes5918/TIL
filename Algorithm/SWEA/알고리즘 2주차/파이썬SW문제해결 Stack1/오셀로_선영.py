import sys
sys.stdin = open("ot.txt", "r")
def IsEnemy(hr, hc, color):  # 탐색
    global d_lst, board # 탐색 가능한 방향
    d_lst = []
    for i in range(8):  # 8방향(0-7)
        tr = hr + dr[i]
        tc = hc + dc[i]
        if 0<=tr<N and 0<=tc<N and board[tr][tc] >= 1 and board[tr][tc]!= color:  # 1또는2
            check = (lambda x: 2 if color==1 else 1)(color)
            if board[tr][tc] == check:  # 상대방 돌
                d_lst.append(i)
    print(d_lst)
    return d_lst

def DFS(hr, hc, color):
    global tr, tc
    visited.append((hr, hc))
    if len(d_lst) == 0: # 갈 곳 없음
        return False
    else:
        d = 0
        for d in d_lst:  # 예시-[0, 2, 3 ... ] i값
            tr = hr + dr[d]
            tc = hc + dc[d]
            if (tr, tc) not in visited:
                tmp = change(tr, tc)
                board[tr][tc] = tmp
def change(r, c):
    if board[r][c] == 1:
        return 2
    else:  # color == 2
        return 1
T=int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    board = [[0]*N for _ in range(N)]
    # 초기 가운데 돌 4개 배치
    n = N//2
    board[n-1][n-1] = board[n][n] = 2  # 백
    board[n][n-1] = board[n-1][n] = 1  # 흑
    # 이동 범위
    dr = [+1, 0, -1, -1, -1, 0, 1, 1]
    dc = [-1, -1, -1, 0, 1, 1, 1, 0]
    # 초기 설정
    visited = []
    for _ in range(M):  # 돌 놓기
        r, c, color = map(int, input().split())
        r, c = r-1, c-1  # index 조정
        board[r][c] = color
        IsEnemy(r, c, color)
        DFS(r, c, color)
        board[r][c] = color
    # 인쇄 기초작업
    black_cnt, white_cnt = 0, 0
    for b in board:
        black_cnt += b.count(1)
        white_cnt += b.count(2)
    print('#{} {} {}'.format(test_case, black_cnt, white_cnt))
