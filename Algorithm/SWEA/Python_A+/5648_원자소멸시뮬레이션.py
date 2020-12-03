import sys
sys.stdin = open('input3.txt', 'r')

delta = [(0, 0.5), (0, -0.5), (-0.5, 0), (0.5, 0)]
for tc in range(1, int(input()) + 1):
    N = int(input())
    point = {}
    result = 0
    for _ in range(N):
        x, y, d, energy = map(int, input().split())
        point[(x, y)] = [[d, energy]]

    for _ in range(4000):
        if len(point) <= 1:
            break
        temp = {}
        for key, value in point.items():
            nx = key[0] + delta[value[0][0]][0]
            ny = key[1] + delta[value[0][0]][1]
            if nx > 1000 or nx < -1000 or ny > 1000 or ny < -1000:
                continue
            try:
                temp[(nx, ny)].append(value[0])
            except:
                temp[(nx, ny)] = value

        # 원자소멸 에너지 저장
        poplist = []
        for key, value in temp.items():
            if len(temp[key]) > 1:
                for v in value:
                    result += v[1]
                poplist.append(key)

        # 제거
        for p in poplist:
            del(temp[p])

        point = temp
    print('#{} {}'.format(tc, result))
