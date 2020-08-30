import sys

N = int(sys.stdin.readline().rstrip())
numbers = []
for i in range(N):
    numbers.append(int(sys.stdin.readline().rstrip()))
numbers = sorted(numbers)
for i in range(N):
    print(numbers[i])