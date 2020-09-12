N = int(input())
a = N // 2
b = N - N // 2

for i in range(N):
    print('* ' * b)
    print(' *' * a)