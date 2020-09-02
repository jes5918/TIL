import sys
sys.stdin = open('5097.txt', 'r')

# for tc in range(1, int(input())+1):
#     N, M = map(int, input().split())
#     numbers = list(map(int, input().split()))
#     M = M % N
#     print('#{} {}'.format(tc, numbers[M]))

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    for i in range(M):
        temp = numbers.pop(0)
        numbers.append(temp)
    print('#{} {}'.format(tc, numbers[0]))