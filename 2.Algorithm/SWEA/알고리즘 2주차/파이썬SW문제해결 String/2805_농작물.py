import sys
sys.stdin=open('no.txt','r')

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [[int(x) for x in input()] for _ in range(N)]
    st = ed = N // 2
    sum_cost = 0
    while st >= 0:
        sum_cost += arr[st][ed]
        for i in range(1, st+1):
            sum_cost += arr[st][ed-i]
            sum_cost += arr[st][ed+i]
        st -= 1

    st = N // 2 + 1
    ed = N // 2
    n = st
    while st < N:
        sum_cost += arr[st][ed]
        for i in range(1, n-1):
            sum_cost += arr[st][ed-i]
            sum_cost += arr[st][ed+i]
        st += 1
        n -= 1

    print('#{} {}'.format(tc, sum_cost))