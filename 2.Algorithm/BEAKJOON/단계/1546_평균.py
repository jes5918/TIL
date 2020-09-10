N = int(input())
arr = list(map(int, input().split()))
MAX = max(arr)
for i in range(N):
    arr[i] = arr[i] / MAX * 100
print(sum(arr)/N)