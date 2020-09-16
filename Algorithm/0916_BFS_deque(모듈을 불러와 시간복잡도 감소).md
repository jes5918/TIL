## 백준 7576 토마토문제(BFS)

> 처음 문제를 풀 때 `from collections import deque` 모듈을 사용하지 않고
>
> q.pop(0) 과 같이 일반적인 pop을 사용하였다. 하지만 계속 시간초과로 문제가 풀리지 않자
>
> 검색을 통해  이유를 찾았다.

주의해야할 점 Python에서 list를 queue처럼 사용할 수 있다. pop(0)를 하면 index 0 에 있는 숫자가 pop된다,

 하지만, 이 방법은 `O(n)`의 시간복잡도로 pop하기 때문에 매우 느리다. 

그래서 이 문제에서는 시간초과를 막기 위해 collections의 deque를 사용해야 한다. 

해당 자료구조는 `O(1)`의 시간복잡도로 pop하도록 구현 되어있다.

```python
from collections import deque

def bfs():
    global result
    while q:
        xx, yy = q.popleft()
        for a, b in delta:
            nx = xx + a
            ny = yy + b
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if visited[nx][ny] != 0:
                continue
            if board[nx][ny] == -1:
                visited[nx][ny] = -1
                continue
            q.append((nx, ny))
            visited[nx][ny] = visited[xx][yy] + 1


def tomato():
    global MAX
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and board[i][j] == 0:
                MAX = 0
                return
            if MAX < visited[i][j]:
                MAX = visited[i][j]


M, N = map(int, input().split())
board = [[int(x) for x in input().split()] for _ in range(N)]
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[0] * M for _ in range(N)]

q = deque()
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            q.append((i, j))
            visited[i][j] = 1

bfs()
result = 0
MAX = 0
tomato()

if not result:
    print(MAX - 1)
else:
    print(result)
```

