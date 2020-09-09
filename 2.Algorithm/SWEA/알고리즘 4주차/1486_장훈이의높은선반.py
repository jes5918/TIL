import sys
sys.stdin = open('1486.txt', 'r')

def janghun(n, height):
    global minimum
    if height >= minimum:
        return
    elif n >= N:
        if height >= B and height < minimum:
            minimum = height
        return
    else:
        janghun(n+1, height+H[n])
        janghun(n+1, height)

for tc in range(1, int(input())+1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    minimum = 987654321
    janghun(0, 0)
    print('#{} {}'.format(tc, minimum-B))