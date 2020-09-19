import sys
sys.setrecursionlimit(50000)

def perm(n, summ):
    global result
    if n >= 9:
        if summ == 100 and sum(visited) == 7:
            result = visited[:]
        return
    else:
        visited[n] = 1
        perm(n+1, summ + arr[n])
        visited[n] = 0
        perm(n+1, summ)

arr = []
for i in range(9):
    arr.append(int(input()))
visited = [0] * 9
result = []
perm(0, 0)
res = []
for i in range(9):
    if result[i]:
        res.append(arr[i])
res.sort()
for i in range(7):
    print(res[i])