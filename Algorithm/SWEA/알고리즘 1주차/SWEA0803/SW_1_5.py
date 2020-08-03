T = int(input())
for tc in range(1, T+1):
    li = [[x for x in input().split()] for _ in range(9)]
    index = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
    res = '1'
    for i in range(9):
        row = []
        col = []
        for j in range(9):
            col += li[i][j]
            row += li[j][i]
        if index != set(col) or index != set(row):
            res = '0'
         
    for x in range(0,9,3):
        for y in range(0,9,3):
            cross = []
            for a in range(3):
                for b in range(3):
                    cross += li[x+a][y+b]
            if index != set(cross):
                res = '0'    
    print(f'#{tc} {res}')