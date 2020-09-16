import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    board = [input() for _ in range(5)]
    print('#{} '.format(tc), end='')
    MAX = 0
    for i in range(len(board)):
        if MAX < len(board[i]):
            MAX = len(board[i])

    for j in range(MAX):
        for i in range(5):
            try:
                print(board[i][j], end='')
            except:
                pass
    print()
