import sys
sys.stdin = open("input5.txt", "r")

def find_ladder(x, y, cnt, arr):
    # 시작지점 만나면 탈출
    while x > 0:
        # 좌우 확인하고 둘다 0이면 위로 올라간다
        if arr[x][y+1] == 0 and arr[x][y-1] == 0:
            x -= 1
            cnt += 1

        # 오른쪽에 사다리가 있으면
        elif arr[x][y+1] == 1:
            # 벽에 부딫힐 때까지 계속 오른쪽으로 돌진
            while arr[x][y+1]:
                y += 1
                cnt += 1
            # 벽에 부닥치면 위로 한칸 올라가자
            x -= 1
            cnt += 1

        # 왼쪽에 사다리가 있는 경우
        elif arr[x][y-1] == 1:
            # 벽에 부딫힐 떄까지 계속 왼쪽으로 돌진
            while arr[x][y-1]:
                y -= 1
                cnt += 1
            # 벽에 부닥치면 위로 한칸 올라가자
            x -= 1
            cnt += 1
    # 다끝나면 시작점과 cnt를 튜플형태로 반환
    return y-1, cnt

for tc in range(1, 11):
    test_case = int(input())

    # 띄를 둘러보자
    ladder = [0] * 101 # 아래쪽은 띄를 안 두를거라 101개 만든다
    ladder[0] = [0] * 102
    for i in range(1, 101):
        ladder[i] = [0] + list(map(int, input().split())) + [0]

    # 끝나는 지점 탐색
    end = []
    for i in range(1, 101):
        if ladder[100][i]:
            end.append(i)

    # 모든 경우의 수를 result에 튜플 형태로 저장
    result = []
    for e in end:
        count = 0
        # return 값을 2개주면 튜플형태로 자동으로 반환됨
        temp = find_ladder(100, e, count, ladder)
        result.append(temp)

    # 우선 cnt로 정렬하고, 동일한 것이 있을 때는 시작번호가 큰것 순서로 저장
    result.sort(key=lambda x: (x[1], -x[0]))
    print('#{} {}'.format(tc, result[0][0]))


# def dfs(x, y): # 첫번째 방법 - dfs
#     global cnt, visited
#     visited.append((x, y))
#     if x == 1:
#         return y-1
#     for a, b in delta:
#         new_x = x + a
#         new_y = y + b
#         if 0 < new_x <= 100 and 0 < new_y <= 100 and ladder[new_x][new_y] == 1 and ((new_x, new_y) not in visited):
#             cnt += 1
#             return dfs(new_x, new_y)
#
# for tc in range(1, 11):
#     test_case = int(input())
#     ladder = [0] * 101
#     ladder[0] = [0] * 102
#     delta = [(0, -1), (0, 1), (-1, 0)]
#     for i in range(1, 101):
#         ladder[i] = [0] + list(map(int, input().split())) + [0]
#
#     end = []
#     for i in range(1, 101):
#         if ladder[100][i]:
#             end.append(i)
#
#     result = []
#     for e in end:
#         cnt = 0
#         visited = []
#         result.append((dfs(100, e), cnt))
#     print(result)
#     result.sort(key=lambda x: (x[1], -x[0]))
#     print('#{} {}'.format(tc, result[0][0]))
