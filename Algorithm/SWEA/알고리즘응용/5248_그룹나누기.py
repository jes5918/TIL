import sys

sys.stdin = open('input6.txt', 'r')


def check(idx):
    global cnt
    for b in board[idx]:
        if not visited[b]:
            visited[b] = True
            check(b)

for tc in range(1, int(input().rstrip()) + 1):
    N, M = map(int, input().rstrip().split())
    input_li = list(map(int, input().rstrip().split()))
    board = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)
    for x in range(0, len(input_li), 2):
        board[input_li[x]] += [input_li[x + 1]]
        board[input_li[x + 1]] += [input_li[x]]
    cnt = 0
    for i in range(1, N+1):
        if not visited[i]:
            cnt += 1
            check(i)
    print('#{} {}'.format(tc, cnt))

# for tc in range(1, int(input()) + 1):
#     N, M = map(int, input().split())
#     nums = list(map(int, input().split()))
#
#     dic = {k: [] for k in range(N + 1) if k != 0}
#     for i in range(0, len(nums), 2):
#         s, e = nums[i], nums[i + 1]
#         if s not in dic[e]:
#             if s == e:
#                 continue
#             dic[s].append(e)
#
#     ans = N
#     print(dic)
#     for k in dic.keys():
#         ans -= len(set(dic[k]))
#
#     print('#{} {}'.format(tc, ans))

# 예외
# 1
# 4 3
# 1 2 3 4 4 3