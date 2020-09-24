import sys
num = int(sys.stdin.readline())
melon = []
for _ in range(6):
    a, b = map(int, sys.stdin.readline().split())
    melon.append(b)
MAX = 0
for i in range(6):
    temp = melon[i] * melon[(i+1)%6]
    if MAX < temp:
        idx = i
        MAX = temp
print(num * (MAX - (melon[(idx+3)%6] * melon[(idx+4)%6])))