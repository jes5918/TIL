import sys

def perm(n, sum_card):
    global maxx
    if sum_card >= M:
        return
    if n  3:
        total = 0
        for i in range(N):
            if visited:
                total += numbers[n]
        if total > maxx:
            print(total, maxx)
            maxx = total
        return

    visited[n] = 1
    sum_card += numbers[n]
    perm(n+1, sum_card)

    sum_card -= numbers[n]
    visited[n] = 0
    perm(n+1, sum_card)


N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
maxx = 0
visited = [0] * N
perm(0, 0)
print(maxx)