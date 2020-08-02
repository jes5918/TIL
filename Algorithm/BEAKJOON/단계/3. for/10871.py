import sys
T = list(map(int, sys.stdin.readline().split()))
numbers = list(map(int, sys.stdin.readline().split()))  
for i in numbers:
    if T[1] > i:
        print(i, end=' ')