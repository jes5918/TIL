import sys
T = int(sys.stdin.readline())
for i in range(1, T+1):
    print(' ' * (T - i), end='')
    print('*' * i)