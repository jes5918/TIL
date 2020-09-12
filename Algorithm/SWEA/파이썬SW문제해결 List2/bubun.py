# input data : -2 1 1 3 4 -3 5 -3 8 2
N = 10
arr = list(map(int, input().split()))
cnt = 0
for i in range(1<<N):
    SUM = 0
    sub = []
    for j in range(N):
        if i & (1<<j):
            sub.append(arr[j])
            SUM += arr[j]
            if SUM > 0:
                break
    if SUM == 0:
        cnt += 1
        print(sub)
print(f'{cnt}')
