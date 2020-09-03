import sys
sys.stdin = open('5122.txt', 'r')

for tc in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    numbers = list(map(int, input().split()))
    for _ in range(M):
        edit = list(input().split())
        if edit[0] == 'I':
            numbers[int(edit[1]):0] = [int(edit[2])]
            continue
        elif edit[0] == 'D':
            numbers.pop(int(edit[1]))
            continue
        elif edit[0] == 'C':
            numbers[int(edit[1])] = int(edit[2])
    try:
        print('#{} {}'.format(tc, numbers[L]))
    except:
        print('#{} -1'.format(tc))