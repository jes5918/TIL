import sys
num = int(sys.stdin.readline())
melon = []
for _ in range(6):
    a, b = map(int, sys.stdin.readline().split())
    melon.append(b)
MAX = 0
for i in range(6):
    temp = melon[i] * melon[(i+1) % 6]
    if temp > MAX:
        idx = i
        MAX = temp
# num 1m^2당 참외 갯수
# MAX 가장 큰 사각형의 크기
print(num * (MAX - (melon[(idx + 3) % 6] * melon[(idx + 4) % 6])))