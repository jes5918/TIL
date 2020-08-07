T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[int(x) for x in input().split()] for _ in range(N)]
    dic_res = {}
    for x in range(N):
        cnt = 0
        for y in range(N):
            if arr[x][y]:
                cnt += 1
            elif arr[x][y] == 0 and cnt != 0:
                dic_res[cnt] = dic_res.get(cnt, 0) + 1
                cnt = 0
        if cnt:
            dic_res[cnt] = dic_res.get(cnt, 0) + 1

    res_arr = []
    for x, y in dic_res.items():
        res_arr.append((x * y, y, x))
    res_arr.sort()
    print(f'#{tc} {len(res_arr)}', end=' ')
    for i in range(len(res_arr)):
        print(f'{res_arr[i][1]} {res_arr[i][2]}', end=' ')
    print()