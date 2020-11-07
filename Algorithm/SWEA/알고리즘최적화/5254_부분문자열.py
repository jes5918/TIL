import sys

sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input().rstrip())+1):
    N, string = input().rstrip().split()
    