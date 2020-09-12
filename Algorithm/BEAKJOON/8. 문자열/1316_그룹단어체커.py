T = int(input())
count = T
for tc in range(1, T+1):
    group = input()
    res = set()
    for g in group:
        if g not in res:
            temp = g
            res.add(g)
            continue
        elif g in res and g != temp:
            count -= 1
            break
print(count)