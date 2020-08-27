import sys
sys.stdin = open("sample_input.txt", "r")
def dfs(start_node):
    global result
    visited[start_node] = 1 # 방문했다는 표시
    for i in range(1, V+1):
        if arr[start_node][i] and not visited[i]: # 간선이 있고 방문하지 안았으면 dfs 반복
            if i == G: # 도착점이 끝점일 경우 result 1을 반환하여 함수 탈출
                result = 1
                return
            dfs(i) # 새로운 지점으로 dfs 파고들자

for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    arr = [[0] * (V+1) for _ in range(V+1)] # 간선을 확인하기 위해 배열 생성
    visited = [0] * (V+1) # 방문했던 것을 알기 위해 배열 생성
    for i in range(E): # 경로 입력받기
        st, ed = map(int, input().split())
        arr[st][ed] = 1 # 간선표시
    S, G = map(int, input().split()) # S는 시작점 G는 도착점
    result = 0 # 결과출력을 위해 초기화
    dfs(S) # dfs함수 불러오기
    print('#{} {}'.format(tc, result))