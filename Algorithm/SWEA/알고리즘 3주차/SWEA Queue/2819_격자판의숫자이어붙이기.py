import sys
sys.stdin = open('2819.txt', 'r')

# def dfs(x, y, s, dp):
#     # 출력하기 위한 res 설정
#     global res
#     # 7번 파고들게 되면 결과값을 res에 추가추가하고 return
#     if dp == 7:
#         res.add(s)
#         return
#     # 4방향 탐색
#     for a, b in delta:
#         # 새로운 좌표 만들기
#         nx = a + x
#         ny = b + y
#         # 밖으로 나가지마
#         if nx < 0 or ny < 0 or nx >= 4 or ny >= 4:
#             continue
#         # 원래 s = 1, 새로운 좌표의 값 1 이면 ns = 11을 만들기 위해 생성
#         ns = s * 10 + board[nx][ny]
#         # 새로운 좌표, 새로운 값, dp+1해서 파고들자
#         dfs(nx, ny, ns, dp+1)
#
# tc = int(input())
# for tc in range(1, tc + 1):
#     board = [[int(x) for x in input().split()] for _ in range(4)]
#     delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#     # 결과값은 중복이 없어야 하므로 set으로 설정
#     res = set()
#     # 모든 곳을 다 탐색해야해,,,
#     for i in range(4):
#         for j in range(4):
#             # dfs 파고드는데 시작좌표, 시작값, 몇번파고드나 설정
#             dfs(i, j, board[i][j], 1)
#
#     # 중복없는 set의 갯수세면 정답
#     print('#{} {}'.format(tc, len(res)))

def bfs(x, y, s, dp):
    global res
    q = []
    q.append((x, y, s, dp))
    while q:
        xx, yy, ss, depth = q.pop(0)
        if depth == 7:
            res.add(ss)
            return
        else:
            for a, b in delta:
                nx = a + xx
                ny = b + yy
                if nx < 0 or ny < 0 or nx >= 4 or ny >= 4:
                    continue
                ns = ss * 10 + borad[nx][ny]
                q.append((nx, ny, ns, depth+1))

for tc in range(1, int(input())+1):
    borad = [[int(x) for x in input().split()] for _ in range(4)]
    delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    res = set()
    for i in range(4):
        for j in range(4):
            bfs(i, j, borad[i][j], 1)
    print(res)
    print('#{} {}'.format(tc, len(res)))






# 수아쓰코드
# '''
# 4X4 크기 격자판
# 각 격 자판 0부처 9까지
# 동서남북 4방향으로 인접한 격자로 총 6번 이동
# 각 칸 숫자 차례로 이어붙이면 7자리
# 한번 거쳤던 격자칸 다시 거쳐도 됨
# 0으로 시작 가능
# 격자판 벗어나면 안됨
# 서로 다른 일곱자리 수 개수 구하기
#
# 음...DFS? -> RecursionError남
# 현우's hint
# 수를 입력받을떄 str로 받아라
# DFS인자로 num을 주고 다음 num 은 num = num + arr[i][j]
# if len(num)이 7이면 return
# '''
# import sys
# sys.stdin = open('2819.txt','r')
#
# di = [0,0,1,-1] #우좌하상
# dj = [1,-1,0,0]
# def DFS(i,j,num):
#     global num_set
#     #d 밑에다가 넣는다면 num이 계속 붙어버려서 밖에다 처음 등장햇을 떄! 처리해야됨
#     # print('i',i,'j',j,'num',num)
#     if len(num) == 7:
#         num_set.add(num)
#         return
#     for d in range(4):
#         ni = i + di[d]
#         nj = j + dj[d]
#         if ni < 0 or ni >= 4 or nj < 0 or nj >= 4:
#             continue
#         DFS(ni,nj,num+arr[ni][nj])
#
# T = int(input())
# for tc in range(1,T+1):
#     arr = [list(input().split()) for _ in range(4)]
#     # print(arr)
#     cnt = 0
#     num = ''
#     num_set = set()
#     for i in range(4):
#         for j in range(4):
#             DFS(i,j,arr[i][j])
#     # DFS(0,0,arr[0][0])
#     print('#{} {}'.format(tc,len(num_set)))