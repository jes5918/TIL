import sys

sys.stdin = open('input3.txt', 'r')


def swimming(mon, total):
    global result
    if total > result:
        return
    if mon > 12:
        result = min(result, total)
        return
    if play[mon]:
        swimming(mon + 1, total + min(day * play[mon], month))
        swimming(mon + 3, total + triple)
    else:
        swimming(mon + 1, total)


for tc in range(1, int(input()) + 1):
    day, month, triple, year = map(int, input().split())
    play = [0] + list(map(int, input().split()))
    result = year
    swimming(1, 0)
    print('#{} {}'.format(tc, result))
