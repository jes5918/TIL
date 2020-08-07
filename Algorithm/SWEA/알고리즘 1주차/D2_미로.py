'''
1,1 의 시작점 넣고
좌우 상하 탐색
delta = [(0,1),(0,-1),(-1,0),(1,0)] 우 좌 상 하
우로이동  delta 0 2 3
좌로이동  delta 1 2 3
위로이동 delta 0 1 3
아래로이동 delta 0 1 2
1개 -> 그쪽으로 이동
2개 -> 지점 저장 -> 탐색 0개가 나온다 -> 저장위치로 다시이동


0이 1개
0이 2개
0이 3개
'''
# for i in range(10):
#     N = int(input())
#     miro = [[int(x) for x in input().split()] for _ in range(16)]
import sys
sys.stdin = open("input4.txt", "r")

def IsSafe(y,x):
    return 0<=y<16 and 0<=x<16 and (Maze[y][x] == 0 or Maze[y][x] == 3)

def DFS(start_y, start_x):
    global result

    if Maze[start_y][start_x] == 3:
        result = 1
        return

    visited.append((start_y, start_x))
    for dir in range(4):
        New_Y = start_y + dy[dir]
        New_X = start_x + dx[dir]
        if IsSafe(New_Y, New_X) and (New_Y, New_X) not in visited:
            DFS(New_Y, New_X)


for i in range(10):
    N = int(input())
    Maze = [list(map(int, input())) for _ in range(16)]

    try:
        for y in range(16):
            for x in range(16):
                if Maze[y][x] == 2:
                    start_y, start_x = y, x
                    raise NotImplementedError
    except:
        dy = [-1, 1, 0, 0]
        dx = [0, 0, -1, 1]

        visited = []
        result = 0
        DFS(start_y, start_x)
        print(f'#{N} {result}')