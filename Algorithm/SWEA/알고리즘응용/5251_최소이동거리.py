import sys
sys.stdin = open('input9.txt', 'r')

for tc in range(1, int(input().rstrip())+1):
    N, E = map(int, input().rstrip().split())
    for _ in range(E):
        s, e, w = map(int, input().rstrip().split())
