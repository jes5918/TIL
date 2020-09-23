import sys

K = int(sys.stdin.readline())
board = [[False] * (101) for _ in range(101)]
cnt = [0] * (K+1)
for x in range(1, K+1):
    stx, sty, M, N = map(int, sys.stdin.readline().split())
    for i in range(stx, stx + M):
        for j in range(sty, sty + N):
            board[i][j] = x

for b in board:
    for a in b:
        if a:
            cnt[a] += 1
for b in cnt[1:]:
    print(b)
# res_dict = {}
# for k in range(1, K+1):
#     for i in range(101):
#         for j in range(101):
#             res_dict[board[i][j]] = res_dict.get(board[i][j], 0) + 1
#
# res = sorted(res_dict.items(), key=lambda x: x[0])
# for i in range(1, K+1):
#     print(res[i][1]//2)