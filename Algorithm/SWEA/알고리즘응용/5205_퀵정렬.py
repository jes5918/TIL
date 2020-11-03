import sys

sys.stdin = open('input9.txt', 'r')


def partitionlomuto(board, l, r):
    pivot = board[r]
    i = l - 1
    for j in range(l, r):
        if board[j] < pivot:
            i += 1
            board[i], board[j] = board[j], board[i]
    board[i + 1], board[r] = board[r], board[i + 1]
    return i + 1


def partitionhoare(board, l, r):
    pivot = (l + r) // 2
    while l < r:
        while (board[l] < board[pivot] and l < r):
            l += 1
        while (board[r] >= board[pivot] and l < r):
            r -= 1
        if l < r:
            if l == pivot:
                pivot = r
            board[l], board[r] = board[r], board[l]
    board[pivot], board[r] = board[r], board[pivot]
    return r


def quick_sort(board, l, r):
    if l < r:
        # p = partitionhoare(board, l, r)
        p = partitionlomuto(board, l, r)
        if p == N // 2:
            return
        elif p > N // 2:
            quick_sort(board, l, p - 1)
        else:
            quick_sort(board, p + 1, r)


for tc in range(1, int(input()) + 1):
    N = int(input())
    board = list(map(int, input().split()))
    quick_sort(board, 0, N - 1)
    print('#{} {}'.format(tc, board[N // 2]))
