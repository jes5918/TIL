import sys
sys.stdin = open('5178.txt', 'r')

for tc in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    tree = [-1] * (N+1)
    for i in range(M):
        node, num = map(int, input().split())
        tree[node] = num

    for idx in range(N, -1, -1):
        if tree[idx] == -1:
            if idx * 2 < N:
                tree[idx] = tree[idx * 2] + tree[idx * 2 + 1]
            else:
                tree[idx] = tree[idx * 2]

    print('#{} {}'.format(tc, tree[L]))