import sys
sys.stdin = open('input.txt', 'r')

def pal(x):
    x = str(x)
    len_x = len(x)
    if x[0:(len_x//2)] == x[-1:len_x-(len_x//2)-1:-1]:
        return True
    else:
        return False
for tc in range(1, int(input())+1):
    A, B = map(int, input().split())
    cnt = 0
    for i in range(1, B+1):
        if A <= i*i <= B:
            if pal(i) and pal(i*i):
                cnt += 1
        if i*i > B:
            break
    print('#{} {}'.format(tc, cnt))