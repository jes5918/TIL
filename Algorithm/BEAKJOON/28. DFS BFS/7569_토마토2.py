from collections import deque

# 주의해야할 점 Python에서 list를 queue처럼 사용할 수 있다.
# pop(0)를 하면 index 0 에 있는 숫자가 pop된다,
# 하지만, 이 방법은 O(n)의 시간복잡도로 pop하기 때문에 매우 느리다.
# 그래서 이 문제에서는 시간초과를 막기 위해 collections의 deque를 사용해야 한다.
# 해당 자료구조는 O(1)의 시간복잡도로 pop하도록 구현 되어있다.
# 자료구조의 차이를 잘 생각하자

def bfs():
    global result
    while q:
        zz, xx, yy = q.popleft()
        for c, a, b in delta:
            nz = zz + c
            nx = xx + a
            ny = yy + b
            if nx < 0 or nx >= N or ny < 0 or ny >= M or nz < 0 or nz >= K:
                continue
            if visited[nz][nx][ny] != 0:
                continue
            if board[nz][nx][ny] == -1:
                visited[nz][nx][ny] = -1
                continue
            q.append((nz, nx, ny))
            visited[nz][nx][ny] = visited[zz][xx][yy] + 1


def tomato():
    global MAX
    for k in range(K):
        for i in range(N):
            for j in range(M):
                if visited[k][i][j] == 0 and board[k][i][j] == 0:
                    MAX = 0
                    return
                if MAX < visited[k][i][j]:
                    MAX = visited[k][i][j]


M, N, K = map(int, input().split())
board = [[[int(x) for x in input().split()] for _ in range(N)] for _ in range(K)]
delta = [(0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1), (1, 0, 0), (-1, 0, 0)]
visited = [[[0] * M for _ in range(N)] for _ in range(K)]

q = deque()
for k in range(K):
    for i in range(N):
        for j in range(M):
            if board[k][i][j] == 1:
                q.append((k, i, j))
                visited[k][i][j] = 1

bfs()
result = 0
MAX = 0
tomato()
if not result:
    print(MAX - 1)
else:
    print(result)