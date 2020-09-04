

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [input() for i in range(N)]
    temp = []

    # 각행의 색깔의 갯수를 카운트 하여 temp에 리스트 형태로 저장된다
    for i in range(N):
        w = arr[i].count('W')
        b = arr[i].count('B')
        r = arr[i].count('R')
        temp.append([w, b, r])

    # 가장 최소이동의 경우의 수를 맞춰야 하기 때문에 누적합을 이용한다
    # 원래의 상태
    # temp = [[3, 0, 2], [2, 2, 1], [3, 0, 2], [2, 1, 2]]
    # 아래 포문 후 상태
    # temp = [[3, 0, 2], [5, 2, 3], [8, 2, 5], [10, 3, 7]]
    # 즉, 맨 아래 행렬의 값인 [10, 3, 7] 이 의미하는 바는 국기에서 각각의 색이 가지고 있는 수의 합이다.
    # white = 10, blue = 3, red = 7 총 N * M = 20
    for i in range(1, N):
        temp[i][0] += temp[i-1][0]
        temp[i][1] += temp[i-1][1]
        temp[i][2] += temp[i-1][2]

    # 첫번째 i, range 범위는 맨 윗쪽의 white의 색이기 때문에 아래 최소 2가지 색이 남을 수 있으니 N-2한다
    # 두번째 j, range 범위는 가운데 파랑색을 돌리는 것이라 최소 i(white)의 갯수+1 부터 최대 마지막 red 한줄을 남겨야 해서 N-1
    # 반복문을 돌리며 최소로 소모되는 이동을 구해야 하니 모든 경우의 수 탐색
    # res에 값에는 움직이지 안아도 될 ww, bb, rr의 갯수의 합의 최댓값이 저장된다
    # 출력할때 N * M - res 하면 이동해야 할 최솟값이 나온다!
    res = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            # 0 은 white, 1은 blue, 2는 red
            # temp엔 누적합이 저장되어 있다
            # 첫번째 ww는 그냥 그대로의 값을 받는다
            ww = temp[i][0]
            # bb는 j까지 누적된 합에서 i까지 누적된 합을 빼면 안움직여도 되는 갯수가 나온다
            bb = temp[j][1] - temp[i][1]
            # rr는 맨 마지막줄에 적혀있는 누적합에서 red의 j 값까지의 누적합을 배면 red에서 움직이지 않아야 하는 갯수가 나온다.
            rr = temp[N-1][2] - temp[j][2]
            # 최댓값 res 저장 (전체에서 빼면 움직여야할 최솟값이 나오므로!)
            if res < ww + bb + rr:
                res = ww + bb + rr
    print('#{} {}'.format(tc, M*N-res))

