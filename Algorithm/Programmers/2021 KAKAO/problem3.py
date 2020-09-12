def solution(info, query):
    board = []
    print(info)
    for i in info:
        board.append(i.split())

    board_query = []
    for q in query:
        board_query.append(q.split(' and '))
    for i in range(len(board_query)):
        temp = board_query[i][-1].split(' ')
        board_query[i].pop()
        board_query[i].extend(temp)

    def kakao3(querys):
        res = 0
        for x in range(len(board)):
            cnt = 0
            for y in range(4):
                if querys[y] == board[x][y]:
                    cnt += 1
                elif querys[y] == '-':
                    cnt += 1
            if cnt == 4 and int(querys[4]) <= int(board[x][4]):
                res += 1
        return res

    answer = []
    for i in range(len(board_query)):
        count = kakao3(board_query[i])
        answer.append(count)
    return answer




print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))