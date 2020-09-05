import sys
sys.stdin = open('5174.txt', 'r')

for tc in range(1, int(input())+1):
    E, N = map(int, input().split())
    lines = list(map(int, input().split()))
    visited = []
    for i in range(E):
        lines[i*2]
        lines[i*2+1]