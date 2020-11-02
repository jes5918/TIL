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

# 다른사람 코드인데 이해해보자 꿀팁이 숨어있땅
# T = int(input())
# for test_case in range(1, T + 1):
#     num, data = input().split()
#     result = ''
#     for i in range(int(num)):
#         result += '{:04b}'.format(int(data[i], 16)) # 한글자씩 16진수를 2진수 4자리로
#     print('#{} {}'.format(test_case, result))