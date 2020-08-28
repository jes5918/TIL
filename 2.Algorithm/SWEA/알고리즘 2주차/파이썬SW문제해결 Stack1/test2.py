
N, M = map(int, input().split())
crosswords = [0] * (N + 2)
for i in range(1, N + 1):
    crosswords[i] = [0] + list(map(int, input().split())) + [0]
crosswords[0] = [0] * (N + 2)
crosswords[-1] = [0] * (N + 2)

print(crosswords)

crosswords += (list(map(list, zip(*crosswords))))
print(crosswords)


# 10
# 5 3
# 0 0 1 1 1
# 1 1 1 1 0
# 0 0 1 0 0
# 0 1 1 1 1
# 1 1 1 0 1
# 5 3
# 1 0 0 1 0
# 1 1 0 1 1
# 1 0 1 1 1
# 0 1 1 0 1
# 0 1 1 1 0
# 8 3
# 1 1 0 1 0 1 1 1
# 0 1 0 1 0 0 0 1
# 1 1 1 0 0 1 0 1
# 0 1 0 1 0 1 1 1
# 0 0 0 1 0 1 0 1
# 1 1 1 1 1 1 0 0
# 0 1 0 0 0 1 0 1
# 1 1 1 0 1 1 1 1
# 8 4
# 0 1 1 1 0 1 1 1
# 1 0 0 1 0 1 0 0
# 1 0 0 1 1 1 0 1
# 1 1 1 0 0 1 1 1
# 0 0 1 0 0 1 0 1
# 1 1 1 1 1 0 0 0
# 0 1 0 0 1 0 0 0
# 1 1 1 0 1 1 1 0
# 10 3
# 0 1 0 0 0 1 0 0 0 1
# 0 1 0 1 0 1 0 1 1 1
# 1 1 1 1 1 1 1 1 0 1
# 0 1 0 0 1 0 0 1 0 0
# 0 1 1 1 1 0 1 1 1 0
# 0 0 0 1 0 1 0 0 1 0
# 0 1 1 1 0 1 1 1 1 1
# 0 1 0 0 0 1 0 0 0 1
# 1 1 1 0 0 0 0 1 1 1
# 0 0 1 1 1 0 0 1 0 0
# 10 4
# 0 0 1 0 0 0 1 0 0 1
# 0 0 1 1 0 0 1 1 1 1
# 1 1 1 1 1 1 1 1 0 1
# 0 0 1 0 1 0 0 1 0 0
# 0 1 1 1 1 1 0 1 1 1
# 0 0 0 1 0 0 1 0 1 0
# 0 1 1 1 0 1 1 1 0 1
# 0 0 1 0 0 0 1 0 0 1
# 1 1 1 0 0 0 0 1 1 1
# 0 1 0 1 1 0 1 1 1 0
# 12 3
# 0 1 0 1 0 1 0 1 0 1 0 1
# 1 1 0 1 1 1 0 1 1 1 0 1
# 0 1 1 1 0 1 1 1 0 1 1 1
# 0 0 1 0 0 0 1 0 0 0 1 0
# 0 1 1 1 0 1 1 1 0 1 1 1
# 1 1 0 1 1 1 0 1 1 1 0 1
# 0 1 1 1 0 1 1 1 0 1 1 1
# 0 0 1 0 0 0 1 0 0 0 1 0
# 0 1 1 1 0 1 1 1 0 1 1 1
# 1 1 0 1 1 1 0 1 1 1 0 1
# 0 1 1 1 0 1 1 1 0 1 1 1
# 0 0 1 0 0 0 1 0 0 0 1 0
# 12 4
# 0 1 1 1 0 1 1 1 0 1 1 1
# 1 1 0 1 1 1 0 1 1 1 0 1
# 1 1 1 1 1 1 1 1 1 1 1 1
# 1 0 1 0 1 0 1 0 1 0 1 0
# 0 1 1 1 0 1 1 1 0 1 1 1
# 1 1 0 1 1 1 0 1 1 1 0 1
# 1 1 1 1 1 1 1 1 1 1 1 1
# 1 0 1 0 1 0 1 0 1 0 1 0
# 0 1 1 1 0 1 1 1 0 1 1 1
# 1 1 0 1 1 1 0 1 1 1 0 1
# 1 1 1 1 1 1 1 1 1 1 1 1
# 1 0 1 0 1 0 1 0 1 0 1 0
# 15 3
# 1 1 1 0 1 1 1 0 1 1 1 0 1 1 1
# 0 1 1 1 0 1 1 1 0 1 1 1 0 1 1
# 1 0 1 1 1 0 1 1 1 0 1 1 1 0 1
# 1 1 0 1 1 1 0 1 1 1 0 1 1 1 0
# 1 1 1 0 1 1 1 0 1 1 1 0 1 1 1
# 0 1 1 1 0 1 1 1 0 1 1 1 0 1 1
# 1 0 1 1 1 0 1 1 1 0 1 1 1 0 1
# 1 1 0 1 1 1 0 1 1 1 0 1 1 1 0
# 1 1 1 0 1 1 1 0 1 1 1 0 1 1 1
# 0 1 1 1 0 1 1 1 0 1 1 1 0 1 1
# 1 0 1 1 1 0 1 1 1 0 1 1 1 0 1
# 1 1 0 1 1 1 0 1 1 1 0 1 1 1 0
# 1 1 1 0 1 1 1 0 1 1 1 0 1 1 1
# 0 1 1 1 0 1 1 1 0 1 1 1 0 1 1
# 1 0 1 1 1 0 1 1 1 0 1 1 1 0 1
# 15 2
# 1 1 1 0 1 1 1 0 1 1 1 0 1 1 1
# 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0
# 1 0 1 1 1 0 1 1 1 0 1 1 1 0 1
# 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0
# 1 1 1 0 1 1 1 0 1 1 1 0 1 1 1
# 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0
# 1 0 1 1 1 0 1 1 1 0 1 1 1 0 1
# 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0
# 1 1 1 0 1 1 1 0 1 1 1 0 1 1 1
# 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0
# 1 0 1 1 1 0 1 1 1 0 1 1 1 0 1
# 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0
# 1 1 1 0 1 1 1 0 1 1 1 0 1 1 1
# 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0
# 1 0 1 1 1 0 1 1 1 0 1 1 1 0 1
