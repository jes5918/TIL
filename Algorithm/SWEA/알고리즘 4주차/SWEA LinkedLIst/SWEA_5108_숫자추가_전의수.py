import sys
sys.stdin = open('5108.txt', 'r')

def addnum(idx, num, arr):
    s1 = arr[:idx]
    s2 = arr[idx:]
    s1.append(num)
    return s1+s2

for tc in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    arr = [int(x) for x in input().split()]
    for i in range(M):
        idx, num = map(int, input().split())
        arr = addnum(idx, num, arr)
    print('#{} {}'.format(tc, arr[L]))