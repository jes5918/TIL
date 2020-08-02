import sys
T = int(sys.stdin.readline())
for tc in range(1, T+1):
    print(f'#{tc}: {sum(map(int, sys.stdin.readline().split()))}')