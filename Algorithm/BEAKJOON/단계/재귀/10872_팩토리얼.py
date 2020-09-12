import sys
sys.getrecursionlimit(100000)
N = int(input())

def factorial(N):
    if N == 0:
        return 1
    elif N == 1:
        return 1
    return N * factorial(N - 1)
print(factorial(N))