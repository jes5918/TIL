di = [0,0,1,-1]
dj = [1,-1,0,0]

ans = -1

def check():
    global ans
    for i in range(N):
        for j in range(N):
            if board[i][j] > ans:
                ans = board[i][j]
    return

def DFS(cnt,dir):
    global ans
    if cnt > 5:
        check()
        return
    if dir == 0: # 오른 쪽
        for i in range(0,N):
            q = []
            # 그 방향서부터 큐에 넣기.
            for j in range(0,N)[::-1]:
                if board[i][j] != 0:
                    q.append(board[i][j])
            # 큐에서 블럭들 합치기
            zero_cnt = 0
            for j in range(len(q)-1):
                if q[j] == q[j+1]:
                    q[j] *= 2
                    q[j+1] = 0
                    zero_cnt += 1
            for _ in range(zero_cnt):
                q.remove(0)
            # 큐에 잇는 애들 다시 해당 줄에 넣기
            for j in range(0,N)[::-1]:
                if q:
                    board[i][j] = q[0]
                    q.pop(0)
                else:
                    board[i][j] = 0
    if dir == 1: # 왼 쪽
        for i in range(0,N):
            q = []
            # 그 방향서부터 큐에 넣기.
            for j in range(0,N):
                if board[i][j] != 0:
                    q.append(board[i][j])
            # 큐에서 블럭들 합치기
            zero_cnt = 0
            for j in range(len(q)-1):
                if q[j] == q[j+1]:
                    q[j] *= 2
                    q[j+1] = 0
                    zero_cnt += 1
            for _ in range(zero_cnt):
                q.remove(0)
            # 큐에 잇는 애들 다시 해당 줄에 넣기
            for j in range(0,N):
                if q:
                    board[i][j] = q[0]
                    q.pop(0)
                else:
                    board[i][j] = 0
    if dir == 2: # 위 쪽
        for j in range(0,N):
            q = []
            # 그 방향서부터 큐에 넣기.
            for i in range(0,N):
                if board[i][j] != 0:
                    q.append(board[i][j])
            # 큐에서 블럭들 합치기
            zero_cnt = 0
            for i in range(len(q)-1):
                if q[i] == q[i+1]:
                    q[i] *= 2
                    q[i+1] = 0
                    zero_cnt += 1
            for _ in range(zero_cnt):
                q.remove(0)
            # 큐에 잇는 애들 다시 해당 줄에 넣기
            for i in range(0,N):
                if q:
                    board[i][j] = q[0]
                    q.pop(0)
                else:
                    board[i][j] = 0
    if dir == 3: # 아래 쪽
        for j in range(0,N):
            q = []
            # 그 방향서부터 큐에 넣기.
            for i in range(0,N)[::-1]:
                if board[i][j] != 0:
                    q.append(board[i][j])
            # 큐에서 블럭들 합치기
            zero_cnt = 0
            for i in range(len(q)-1):
                if q[i] == q[i+1]:
                    q[i] *= 2
                    q[i+1] = 0
                    zero_cnt += 1
            for _ in range(zero_cnt):
                q.remove(0)
            # 큐에 잇는 애들 다시 해당 줄에 넣기
            for i in range(0,N)[::-1]:
                if q:
                    board[i][j] = q[0]
                    q.pop(0)
                else:
                    board[i][j] = 0
    for ndir in range(4):
        DFS(cnt+1,ndir)



N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]

for dir in range(4):
    DFS(0,dir)

# print(board)
print(ans)





