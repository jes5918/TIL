import sys
sys.stdin = open('5099.txt', 'r')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
