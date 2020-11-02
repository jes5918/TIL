import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    board = list(map(int, input().split()))
    board_set = set(board)
    result = ''
    if len(board) != len(board_set):
        result = 'No'
    else:
        if max(board) == N:
            result = 'Yes'
        else:
            result = 'No'
    print('#{} {}'.format(tc, result))