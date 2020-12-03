import sys

sys.stdin = open('input.txt', 'r')

from copy import deepcopy
from collections import deque

delta = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def DFS(n, arr):
    global min_value
    # 벽돌이 하나도 없을경우 리턴
    if min_value == 0:
        return
    # 기회랑 실행횟수랑 같을 때 결과값 계산하는 부분
    if n == N:
        temp = 0
        for i in range(H):
            for j in range(W):
                if arr[i][j]:
                    temp += 1
        if temp < min_value:
            min_value = temp
        return
    # 각 열 단위로 배열 복사하고, 벽돌뿌시고(BFS), 부신상태의 배열을 가지고 다음 구슬치기 기회로 넘어감
    for i in range(W):
        copied_arr = deepcopy(arr)
        BFS(i, copied_arr)
        DFS(n + 1, copied_arr)


def BFS(y, arr):
    # BFS는 각 열 단위로 진행한다(구슬치기니깐)
    # 맨 위쪽 벽돌 찾는 과정
    x = 0
    for k in range(H):
        # 가장 위쪽 벽돌 찾는다
        if arr[k][y]:
            x = k
            break
        # 해당 열에 벽이 하나도 없을 때는 함수 리턴
        if k == (H - 1):
            return

    # 벽돌 연쇄폭발 시키는 과정
    q = deque()
    q.append((x, y))
    while q:
        xx, yy = q.popleft()
        # bomb 는 폭발의 크기
        bomb = arr[xx][yy]
        # 해당위치 터졌다는 표시
        arr[xx][yy] = 0
        for bomb_range in range(1, bomb):
            for a, b in delta:
                nx = xx + a * bomb_range
                ny = yy + b * bomb_range
                if 0 <= nx < H and 0 <= ny < W:
                    q.append((nx, ny))

    # 벽돌을 터트리고 난 후 아래로 모으는 과정
    for b in range(W):
        temp = []
        for a in range(H - 1, -1, -1):
            if arr[a][b]:
                temp.append(arr[a][b])
                arr[a][b] = 0
        for a in range(len(temp)):
            arr[H - a - 1][b] = temp[a]


for tc in range(1, int(input()) + 1):
    N, W, H = map(int, input().split())
    board = [[int(x) for x in input().split()] for _ in range(H)]
    min_value = 0xfffffff
    DFS(0, board)
    print('#{} {}'.format(tc, min_value))
