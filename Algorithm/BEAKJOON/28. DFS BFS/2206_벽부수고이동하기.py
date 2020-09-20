from collections import deque

def bfs():
    q = deque()
    q.append((0, 0, 0))
    while q:
        xx, yy, zz = q.popleft()
        if (xx, yy) == (N-1, M-1):
            return visited[zz][xx][yy]
        for a, b in delta:
            nx = a + xx
            ny = b + yy
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if visited[zz][nx][ny]:
                continue
            if board[nx][ny] and not zz:
                q.append((nx, ny, 1))
                visited[1][nx][ny] = visited[zz][xx][yy] + 1
            elif not board[nx][ny]:
                q.append((nx, ny, zz))
                visited[zz][nx][ny] = visited[zz][xx][yy] + 1
    return -1


N, M = map(int, input().split())
board = [[int(x) for x in input()] for _ in range(N)]
visited = [[[0] * M for _ in range(N)] for _ in range(2)]
visited[0][0][0] = 1
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
print(bfs())