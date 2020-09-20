N = int(input())
arr = []
for _ in range(N-1):
    a, b = map(int, input().split())
    arr.append((a,b))
print(arr)