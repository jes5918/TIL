import sys
sys.stdin = open("input2.txt", "r")

def find_ladder(x, y):
    while x != 0: # 맨 윗줄의 띄 까지 오면 와일문 탈출
        # 좌우가 0이면 위쪽 행으로올라가자
        if arr[x][y-1] == 0 and arr[x][y+1] == 0:
            x -= 1

        # 오른쪽에 사다리 등장
        elif arr[x][y+1] == 1:
            while arr[x][y+1]: # 오른쪽 벽에 막힐떄까지 오른쪽으로 가자
                arr[x][y] = 0 # 현위치를 0으로 만들고 이동하자
                y += 1 # 한칸 옆으로 고고

        # 왼쪽에 사다리 등장
        elif arr[x][y-1] == 1:
            while arr[x][y-1]: # 왼쪽 벽에 막힐떄까지 왼쪽으로 가자
                arr[x][y] = 0 # 현위치를 0으로 만들고 이동하자
                y -= 1 # 한칸 옆으로 고고
    return y

T = 10
for tc in range(1, T+1):
    test_case = input()
    # 띄 0 두르고 안에 입력받기
    N = 100
    arr = [0] * (N + 1) # 배열의 행 101개 만들기 (0으로 배열의 띄 만들기, 맨 마지막줄은 안해서 101개)
    arr[0] = [0] * (N + 2) # 배열의 1번째 행 102개 만들기(맨 윗줄 띄)
    for i in range(N):
        arr[i + 1] = [0] + list(map(int, input().split())) + [0] # 입력받으며 양 옆의 띄 생성

    # 도착지점부터 찾으면 개꿀인걸? 꺼꾸로 가자
    for i in range(1, 101):
        if arr[-1][i] == 2: # 도착점을 찾으면
            end = i # 인덱스값 저장
            break # 시간단축을 하자

    # 도착지점의 바로 한칸 위 지점부터 시작, 띄로 인한 인덱스 밀림 방지를 위해 -1 한다
    res = find_ladder(99, end) - 1
    print('#{} {}'.format(test_case, res))

# 멍도군코드
# def dfs(a, b):
#     global result
#     visited.append((a, b))
#     # 맨위에 가면 멈추기
#     if a == 0:
#         result = b
#         return
#     # 델타 탐색으로 위 양옆 탐색 후 이동
#     for d in range(3):
#         new_x = a + d_x[d]
#         new_y = b + d_y[d]
#         if (0 <= new_x < 100) and (0 <= new_y < 100) and (arr[new_x][new_y] == 1) and ((new_x, new_y) not in visited):
#             return dfs(new_x, new_y)
#
#
# for _ in range(10):
#     tc = int(input())
#     arr = [list(map(int, input().split())) for _ in range(100)]
#     visited = []
#     d_x = [0, 0, -1]
#     d_y = [-1, 1, 0]
#     result = 0
#     dfs(99, arr[99].index(2))
#
#     print('#{} {}'.format(tc, result))

