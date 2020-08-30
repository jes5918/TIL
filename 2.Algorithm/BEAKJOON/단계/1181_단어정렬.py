num = int(input())
a = []
for i in range(num):
    a.append(input())
a = set(a)
d = dict()
for i in a:
    d[i] = len(i)
d = sorted(d, key = lambda x : [len(x), x.lower()])
for i in d:
    print(i)

# import sys
#
# N = int(input())
# aa = []
# for i in range(N):
#     aa.append(sys.stdin.readline().rstrip())
#
# d = {}
# for a in aa:
#     l = len(a) * 1000
#     k = ord(a[0])-ord('a')
#     d[a] = d.get(a, k) + l
# d = sorted(d.items(), key=lambda x: x[1])
# print(d)
