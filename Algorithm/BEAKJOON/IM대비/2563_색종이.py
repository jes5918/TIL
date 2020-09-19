paper = [[0] * 101 for _ in range(101)]
N = int (input())
for _ in range(N):
    st_x, st_y = map(int, input().split())
    for i in range(st_x, st_x + 10):
        for j in range(st_y, st_y + 10):
            if not paper[i][j]:
                paper[i][j] = 1
res = 0
for p in paper:
    res += p.count(1)
print(res)