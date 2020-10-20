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
