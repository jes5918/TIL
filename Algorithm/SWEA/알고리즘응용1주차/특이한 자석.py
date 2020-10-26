import sys
sys.stdin = open('input.txt', 'r')

def sawmachine(n, d):
    # 돌려야할 톱니바퀴가 들어있는 visited 배열
    visited = [False] * 4
    visited[n-1] = True

    # 오른쪽 확인
    for i in range(n-1, 3):
        if saw[i][2] == saw[i+1][6]:
            break
        else:
            visited[i+1] = True

    # 왼쪽 확인
    for i in range(n-1, 0, -1):
        if saw[i][6] == saw[i-1][2]:
            break
        else:
            visited[i-1] = True

    # 방향 확인 n기준으로 방향이 다 바뀌므로...
    temp = [False]*4
    for i in range(4):
        if (i-n-1) % 2 == 0:
            temp[i] = d
        else:
            temp[i] = -d

    # 돌린다
    for i in range(4):
        # 돌릴톱니바퀴
        if visited[i]:
            # 시계방향 회전
            if temp[i] == 1:
                saw[i].insert(0, saw[i].pop())
            # 반시계방향 회전
            else:
                saw[i].append(saw[i].pop(0))


for tc in range(1, int(input())+1):
    K = int(input())
    saw = {}
    for i in range(4):
        saw[i] = list(map(int, input().split()))

    for _ in range(K):
        number, direction = map(int, input().split())
        sawmachine(number, direction)

    result = 0
    for i in range(4):
        if saw[i][0]:
            result += 2**i
    print('#{} {}'.format(tc, result))


# def turn(a):
#     visited = [0]*4
#     global idx
#     # 돌려야하는 자석을 검사.
#     # 0부터 시작하니깐 -1 해줌. x는 톱니바퀴 번호, y는 회전 방향
#     p, y = a[0]-1, a[1]

#     stack = [(p,-y)]
#     plus = [[p,-y]]
#     while stack:
#         (x , f) = stack.pop()
#         y = -f
#         visited[x] = 1
#         if x == 1 or x == 2:
#             if mgnt[x][idx[x][0]] != mgnt[x-1][idx[x-1][-1]] and visited[x-1] == 0:
#                 stack.append((x-1, y))
#                 plus.append([x - 1, y])
#                 visited[x-1] = 1

#             if mgnt[x][idx[x][-1]] != mgnt[x+1][idx[x+1][0]] and visited[x+1] == 0:
#                 stack.append((x + 1, y))
#                 plus.append([x + 1, y])
#                 visited [x+1] = 1

#         elif x == 0:
#             if mgnt[x][idx[x][-1]] != mgnt[x+1][idx[x+1][0]] and visited[x+1] == 0:
#                 stack.append((x + 1,y))
#                 plus.append([x+1, y])
#                 visited[x + 1] = 1

#         else:
#             if mgnt[x][idx[x][0]] != mgnt[x-1][idx[x-1][-1]] and visited[x-1] == 0:
#                 stack.append((x - 1,y))
#                 plus.append([x-1, y])
#                 visited[x - 1] = 1

#     for pl in plus:
#         m_x, m_y = pl[0], pl[1]
#         for d in range(3):
#             idx[m_x][d] = (idx[m_x][d] + m_y) % 8

# for test_case in range(1, int(input()) + 1):
#     k = int(input())
#     # 자석들의 정보를 저장 ( 빨간 화살표부터 시계방향으로 )
#     mgnt = [list(map(int, input().split())) for _ in range(4)]
#     rotate = [list(map(int, input().split())) for _ in range(k)]
#     # 시계방향이면 (-1하고 % 8) 반시계 방향이면 (+1 하고 %8) 최종 idx 가운데 빨간 화살표
#     idx = [[6, 0, 2], [6, 0, 2], [6, 0, 2], [6, 0, 2]]
#     for r in rotate:
#         turn(r)
#     total = 0
#     for j in range(4):
#         total += mgnt[j][idx[j][1]] * (2 ** j)

#     print('#{} {}'.format(test_case, total))