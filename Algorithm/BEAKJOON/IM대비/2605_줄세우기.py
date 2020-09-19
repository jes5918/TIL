N = int(input())
numbers = list(map(int, input().split()))
res = []
for i in range(N):
    res.insert(i-numbers[i], i+1)
print(*res)