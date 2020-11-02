import sys

sys.stdin = open('input2.txt', 'r')


def dongchul(person, percentage):
    global res
    if res >= percentage:
        return
    if person == N:
        if res < percentage:
            res = percentage
        return
    for j in range(N):
        if not visited[j]:
            visited[j] = True
            dongchul(person + 1, percentage * board[person][j])
            visited[j] = False


for tc in range(1, int(input()) + 1):
    N = int(input())
    board = [[int(x) / 100 for x in input().split()] for _ in range(N)]
    res = 0
    visited = [False] * N
    dongchul(0, 1)
    print('#{} {:6f}'.format(tc, res * 100))
