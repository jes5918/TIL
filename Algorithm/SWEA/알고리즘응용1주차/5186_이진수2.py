import sys
sys.stdin = open('input2.txt', 'r')

for tc in range(1, int(input())+1):
    N = float(input())
    res = ''
    while N != 0:
        N