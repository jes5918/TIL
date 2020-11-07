import sys

sys.stdin = open('input.txt', 'r')
# 0.14정도
for tc in range(1, int(input().rstrip()) + 1):
    N, M = map(int, input().rstrip().split())
    dict = {
        'A': [],
        'B': [],
    }
    for _ in range(N):
        dict['A'] += [input().rstrip()]
    for _ in range(M):
        dict['B'] += [input().rstrip()]
    len_A = len(dict['A'])
    len_B = len(dict['B'])
    dict['A'] += dict['B']
    len_set = len(set(dict['A']))
    print('#{} {}'.format(tc, len_A + len_B - len_set))

# for tc in range(1, int(input().rstrip()) + 1):
#     N, M = map(int, input().rstrip().split())
#     A = []
#     B = []
#     for _ in range(N):
#         A += [input().rstrip()]
#     for _ in range(M):
#         B += [input().rstrip()]
#     len_A = len(A)
#     len_B = len(B)
#     A += B
#     len_set = len(set(A))
#     print('#{} {}'.format(tc, len_A + len_B - len_set))