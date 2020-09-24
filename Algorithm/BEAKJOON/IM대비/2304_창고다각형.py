import sys

N = int(sys.stdin.readline())
arr = [0] * 1001
mx, mh = 0, 0
for _ in range(N):
    x, h = map(int, sys.stdin.readline().split())
    arr[x] = h
    if mh < h:
        mx = x
        mh = h
res = 0
now = 0
for i in range(mx + 1):
    if arr[i] > now:
        now = arr[i]
    res += now

now = 0
for i in range(1000, mx, -1):
    if arr[i] > now:
        now = arr[i]
    res += now

print(res)