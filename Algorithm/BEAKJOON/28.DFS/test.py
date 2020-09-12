import sys
sys.stdin = open('input.txt', 'r')

# dfs 함수 정의
def dfs(x, y):
    # 방문했다는 표시
    visited[x][y] = True
    # 좌우상하 탐색하기
    for a, b in delta:
        # 새로운 좌표 생성
        nx = x + a
        ny = y + b
        # 새로운 좌표가 행렬의 범위 넘어가면 다음 반복문으로 continue
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue
        # 방문했다면 continue
        if visited[nx][ny]:
            continue
        # 연못이 1이 아니면 continue
        if not arr[nx][ny]:
            continue
        # 위의 모든 조건이 충족되지 않는다(잘 가고있다)면 dfs를 새로운 좌표로 실행
        dfs(nx, ny)
    # 함수의 종료
    return

T = int(input())
# 테스트 케이스 반복 부분
for tc in range(1, T+1):
    # 뒷마당의 열, 행, 연못좌표의수 입력받기
    M, N, K = map(int, input().split())
    # 뒷마당 크기 초기화
    arr = [[False] * M for _ in range(N)]
    # dfs를 위해 방문배열 만들어버린다
    visited = [[False] * M for _ in range(N)]
    # 좌우상하 델타변수 초기화
    delta = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    # 연못의 배열을 만드는 부분
    for i in range(K):
        yy, xx = map(int, input().split())
        arr[xx][yy] = True

    # 결과값 저장하는 변수 설정
    res = 0

    # 이제 본격적으로 dfs로 탐색하는 부분
    for i in range(N):
        for j in range(M):
            # 배열에 1이 있고, 방문하지 않았다면 dfs 실행
            if arr[i][j] and not visited[i][j]:
                dfs(i, j)
                res += 1

    # 결과값 출력
    print('#{} {}'.format(tc, res))