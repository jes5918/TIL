import sys

sys.stdin = open('input8.txt', 'r')


# def perm(num, k):
#     res = []
#     for i in range(1 << num):
#         temp = []
#         for j in range(k, num):
#             if i & (1 << j):
#                 temp.append(j)
#                 if len(temp) == 2:
#                     if temp not in res:
#                         res.append(temp)
#                     break
#     return res
#
#
# def goldenbell(arr, cnt, perm_li, num):
#     global res
#     if cnt == 0:
#         temp = int(''.join(arr))
#         if temp > res:
#             res = temp
#         return
#     for idx, (i, k) in enumerate(perm_li):
#         arr[i], arr[k] = arr[k], arr[i]
#         goldenbell(arr, cnt-1, perm_li, num+1)

def solve(arr, n, now):
    temp = arr[now:]
    t = arr.count(max(temp))
    if t > 2:
        n += t
    while n and len(temp) > 1:
        temp = arr[now:]
        max_board = max(temp)
        for i in range(len(temp) - 1, -1, -1):
            if temp[i] == max_board:
                max_idx = i
                break
        if max_idx + now != now:
            n -= 1
            arr[max_idx + now], arr[now] = arr[now], arr[max_idx + now]
        # print(temp, max_idx, now, '여기', *arr, '@@@@@ n =', n)
        now += 1
    if n > 0:
        if n % 2 and len(set(board)) == len(board):
            arr[len(arr) - 1], arr[len(arr) - 2] = arr[len(arr) - 2], arr[len(arr) - 1]
    return arr


for tc in range(1, int(input()) + 1):
    num, N = map(int, input().rstrip().split())
    board = list(str(num))
    print('#{} {}'.format(tc, int(''.join(solve(board, N, 0)))))

    # perm_list = perm(len(board), 0)
    # res = 0
    # goldenbell(board, N, perm_list, 0)
    # print('#{} {}'.format(tc, res))
