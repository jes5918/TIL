import sys
while True:
    line = sys.stdin.readline().split()
    if not line:
        break
    numbers = list(map(int, line))
    print(sum(numbers))