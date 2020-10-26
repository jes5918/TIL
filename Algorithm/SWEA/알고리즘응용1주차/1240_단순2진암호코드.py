import sys
sys.stdin = open('input2.txt', 'r')

code_index = ['0001101', '0011001', '0010011', '0111101', '0100011',
              '0110001', '0101111', '0111011', '0110111', '0001011']

def findstartpoint():
    for i in range(N):
        for j in range(M - 1, -1, -1):
            if board[i][j] == '1':
                return i, j - 55

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    board = [input() for _ in range(N)]
    start_row, start_col = findstartpoint()
    num_list = board[start_row][start_col:start_col+56]

    code = []
    for i in range(0, 56, 7):
        temp = num_list[i:i+7]
        t = code_index.index(temp)
        code.append(t)

    res = 0
    for i in range(7):
        if i % 2 == 0:
            res += code[i] * 3
        else:
            res += code[i]
    res += code[7]

    if (res % 10) != 0:
        res = 0
    else:
        res = sum(code)
    print('#{} {}'.format(tc, res))

