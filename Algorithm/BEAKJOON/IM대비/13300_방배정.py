N, K = map(int, input().split())
arr = [[] for _ in range(2)]
for _ in range(N):
    S, Y = map(int, input().split())
    if S == 0: arr[0].append(Y)
    else: arr[1].append(Y)

result = 0
for a in arr:
    for i in range(1, 7):
        temp = a.count(i)
        if temp % K == 0:
            result += temp // K
        else:
            result += temp // K + 1
print(result)