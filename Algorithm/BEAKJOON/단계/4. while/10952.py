import sys
while True:
    numbers = list(map(int, sys.stdin.readline().split()))
    if numbers[0] == 0 and numbers[1] == 0:
        break 
    print(sum(numbers))
    