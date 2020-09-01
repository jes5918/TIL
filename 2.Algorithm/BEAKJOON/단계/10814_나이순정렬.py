N = int(input())
l = []
for i in range(N):
    a, b = input().split()
    a = int(a)
    l.append([a, b, i])
l.sort(key=lambda x: (x[0], x[2]))
for i in range(N):
    print(l[i][0], l[i][1])