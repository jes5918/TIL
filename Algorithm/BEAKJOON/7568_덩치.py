import sys
T = int(sys.stdin.readline())
person = []
for _ in range(T):
    person.append(list(map(int, sys.stdin.readline().split())))
    res = ''
    for i in person:
        rank = 1
        for j in person:
            if i[0] < j[0] and i[1] < j[1]:
                rank += 1
        res += str(rank)
        res += ' '
print(res)