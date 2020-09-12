N = int(input())
x = 0
for i in range(2 * N - 1, -1, -2):
    print(' ' * x, end='')
    print('*' * i)
    x += 1
x -= 1
for j in range(3, 2 * N + 1, 2):
    x -= 1
    print(' ' * x, end='')
    print('*' * j)

# n = int(input())
# for i in range(n):
#     print(" " * i + "*" * ((n - i) * 2 - 1))
# for i in range(n - 2, -1, -1):
#     print(" " * i + "*" * ((n - i) * 2 - 1))