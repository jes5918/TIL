from pprint import pprint

def solution(n, s, a, b, fares):
    answer = 0
    board = [[100001] * (n+1) for _ in range(n+1)]
    for i in range(n+1):
        for j in range(n+1):
            if i == j:
                board[i][j] = 0

    for fare in fares:
        board[fare[0]][fare[1]] =  board[fare[1]][fare[0]] = fare[2]

    pprint(board)

    def convert_board(board, N):
        for i in range(len(board)):
            board[i].insert(0, board[i].pop(N[0]))
            board[i].insert(len(board)-1, board[i].pop(N[1]))
        board.insert(0, board.pop(N[0]))
        board.insert(len(board)-1, board[i].pop(N[1]))
        return board

    def cal(board):
        for n in range(2, len(board)):
            for i in range(len(board)-n):
                temp = []
                for j in range(n):
                    if j == (n-1):
                        temp.append(board[i+j+1][i])
                    else:
                        temp.append(board[i+j+1][i]+board[i+n][i+j+1])
                board[i+n][i] = min(temp)
                del temp
        return board


    board = convert_board(board, [s, a])
    print()
    pprint(board)
    board = cal(board)
    print(board)
    return







print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
# print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))