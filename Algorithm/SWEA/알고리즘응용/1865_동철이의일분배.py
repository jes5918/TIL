import sys

sys.stdin = open('input2.txt', 'r')

# print(1 << 2)
def DFS(flag, idx, value):
    global ans
    if flag == N:
        if ans < value * 100:
            ans = value * 100
        return
        # 진행할 수록 값이 작아지니 이미 구한 값보다 작다면 필요없다.
    if value * 100 <= ans:
        return
    for i in range(N):
        # 해당 일은 이미 배정되어서 처리함.
        # print(bin(flag)[2:].zfill(3), end=' ')
        # print(bin(flag | 1 << i)[2:].zfill(3),end=' ')
        # print(flag & (1 << i))
        if flag & (1 << i): continue
        DFS(flag | 1 << i, idx + 1, value * (work[idx][i] / 100))


for tc in range(1, int(input()) + 1):
    N = int(input())
    work = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    # flag, idx, value
    DFS(0, 0, 1)
    print("#{} {:.6f}".format(tc, ans))


# def dongchul(person, percentage):
#     global res
#     if res >= percentage:
#         return
#     if person == N:
#         if res < percentage:
#             res = percentage
#         return
#     for j in range(N):
#         if not visited[j]:
#             visited[j] = True
#             dongchul(person + 1, percentage * board[person][j])
#             visited[j] = False
#
#
# for tc in range(1, int(input()) + 1):
#     N = int(input())
#     board = [[int(x) / 100 for x in input().split()] for _ in range(N)]
#     res = 0
#     visited = [False] * N
#     dongchul(0, 1)
#     print('#{} {:6f}'.format(tc, res * 100))
