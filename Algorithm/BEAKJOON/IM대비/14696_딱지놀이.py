N = int(input())
for _ in range(N):
    aa = list(map(int, input().split()))
    bb = list(map(int, input().split()))
    a = sorted(aa[1:], reverse=True)
    b = sorted(bb[1:], reverse=True)
    K = min(aa[0], bb[0])
    res = ''
    cnt = 0
    for i in range(K):
        if a[i] == b[i]:
            cnt += 1
            continue
        elif a[i] > b[i]:
            res = 'A'
            break
        else:
            res = 'B'
            break
    if cnt == K:
        if aa[0] == bb[0]:
            res = 'D'
        elif aa[0] > bb[0]:
            res = 'A'
        else:
            res = 'B'
    print(res)