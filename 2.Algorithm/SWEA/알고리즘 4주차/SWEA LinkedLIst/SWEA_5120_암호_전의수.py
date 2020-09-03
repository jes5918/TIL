import sys
sys.stdin = open('5120.txt', 'r')

for tc in range(1, int(input())+1):
    N, M, K = map(int, input().split())
    numbers = list(map(int, input().split()))
    x = M
    while True:
        while K != 0:
            if N < x:
                temp = x - N
                break
            if N == x:
                numbers.append(numbers[-1] + numbers[0])
                temp = M - 1
                N += 1
                K -= 1
                break
            numbers[x:0] = [numbers[x-1] + numbers[x]]
            N += 1
            x += M
            K -= 1
        if K == 0:
            break
        x = temp
    print('#{} {}'.format(tc, ' '.join(str(x) for x in numbers[-1:-11:-1])))