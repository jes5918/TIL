temp = input()
N = 26
res = [-1] * (N)
cnt = 0
for t in temp:
    if res[ord(t)-97] > -1:
        cnt += 1
        continue
    res[ord(t)-97] = cnt
    cnt += 1
print(*res)
