import sys
N, K = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
i = 0
temp = sum(arr[0:K])
MAX = temp
while True:
    temp -= arr[i]
    if i + K >= N:
        break
    temp += arr[i+K]
    if MAX < temp:
        MAX = temp
    i += 1
print(MAX)
