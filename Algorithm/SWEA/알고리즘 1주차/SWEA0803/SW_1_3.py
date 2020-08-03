for t in range(1, 2):
    N = int(input())
    li = [[int(x) for x in input().split()] for _ in range(100)]
    sum_row = [0] * 100
    sum_col = [0] * 100
    sum_cross = [0] * 2
    for i in range(100):
        for j in range(100):
            sum_row[i] += li[i][j]
            sum_col[i] += li[j][i]
            if i == j:
                sum_cross[0] += li[i][j]
                sum_cross[1] += li[99-i][j]
    a = max(sum_row)
    b = max(sum_col)
    c = max(sum_cross)
    print(f'#{t} {max(a, b, c)}')