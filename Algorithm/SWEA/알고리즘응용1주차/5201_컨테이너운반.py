import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    container.sort()
    truck.sort()
    result = 0
    while container or truck:
        try:
            if container[-1] > truck[-1]:
                container.pop()
            else:
                truck.pop()
                result += container.pop()
        except:
            break
    print("#{} {}".format(tc, result))
