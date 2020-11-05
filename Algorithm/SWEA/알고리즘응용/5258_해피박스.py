import sys
sys.stdin = open('input3.txt', 'r')

def check(box, price):
    for i in range(M):
        check(box + arr[i][0], price + arr[i][1])

for tc in range(1, int(input().rstrip())+1):
    N, M = map(int, input().rstrip().split())
    arr = []
    for _ in range(M):
        arr += [tuple(map(int, input().rstrip().split()))]
    arr.sort()
    visited = []
    minbox = arr[0][0]
    check(0, 0)
