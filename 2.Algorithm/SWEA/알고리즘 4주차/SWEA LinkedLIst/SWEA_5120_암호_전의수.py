import sys
sys.stdin = open('5120.txt', 'r')

for tc in range(1, int(input())+1):
    N, M, K = map(int, input().split())
    numbers = list(map(int, input().split()))
    for i in range(1, K+1):
        i = (i*M) % N
        numbers[i:0] = [numbers[i-1] + numbers[i]]
        N += 1
    print(numbers)
    # print('#{} {}'.format(tc, ' '.join(str(x) for x in numbers[-1::-1])))