import sys, time
# sys.stdin = open('input.txt', 'r')
start = time.time()
for tc in range(1, int(input())+1):
    N, arr = input().split()
    idx = ['A', 'B', 'C', 'D', 'E', 'F']
    board = []
    for x in arr:
        if x in idx:
            i = idx.index(x)
            board.append(i+10)
        else:
            board.append(int(x))

    result = ''
    for b in board:
        temp = bin(b)[2:]
        while True:
            if len(temp) == 4:
                break
            temp = '0' + temp
        result += temp

    print('#{} {}'.format(tc, result))
print(time.time()-start)