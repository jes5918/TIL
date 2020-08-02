import sys
T = int(sys.stdin.readline())
for tc in range(1, T+1):
    a = map(int, sys.stdin.readline().split())
    b = list(a)
    print(f'Case #{tc}: {b[0]} + {b[1]} = {b[0] + b[1]}')