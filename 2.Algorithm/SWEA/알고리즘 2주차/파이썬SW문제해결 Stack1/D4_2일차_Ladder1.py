import sys
sys.stdin = open("input2.txt", "r")
# 리턴값은 2를 만나면 2를 리턴
def find_ladder(x, y):
    res = 0
    while True:
        if arr[x][y] == 2:
            res = 2
            break
        if y == 101:
            break

        if arr[x][y-1] == 0 and arr[x][y+1] == 0:
            y += 1
        elif arr[x][y-1] == 1:
            x -= 1
        elif arr[x][y+1] == 1:
            x += 1
    return res

T = 10
for tc in range(1, T+1):
    test_case = input()
    delta_LR = [(-1, 0), (1, 0)]
    # 띄 0 두르고 안에 입력받기
    N = 100
    arr = [0] * (N + 2)
    arr[0] = arr[N + 1] = [0] * (N + 2)
    for i in range(N):
        arr[i + 1] = [0] + list(map(int, input().split())) + [0]

    # 시작지점 index 저장
    start_index = []
    for i in range(1, 101):
        if arr[1][i]:
            start_index.append(i)

    # 시작지점 차례로 함수 돌리고 2(도착점) 찾으면 브레이키
    result = 0
    for idx in start_index:
        if find_ladder(1, idx) == 2:
            result = idx
            break
    print('#{} {}'.format(test_case, result))



#     for a, b in delta_LR:
#     pointX = x + a
#     pointY = y + b
#     if arr[pointX][pointY] == 1:
#         find_ladder(pointX, pointY)

