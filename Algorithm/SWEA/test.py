'''
V개의  작업
해야할 V개의 작업
어떤 작업은 특정 작업이 끝나야 시작할 수 있음(선행관계)
선행관계를 나타낸 그래프
각 작업은 하나씩 정점으로 표시됨
선행 관계는 방향성을 가진 간선으로 표현
사이클은 존재하지 않음(한 정점에서 시작해서 같은 정점으로 돌아오는 경로)
한번에 하나의 작업씩 처리
가능한 작업순서 중 하나만 제시하면 됨!
선행관계만 잘 지켜서 출력하면 됨!

선행관계를 잘 지켜야되니..bfs아닐까...?ㅎ

+지형오빠 도움
정점을 1부터 도는데 1로 향하는 다른 인접 정점을 찾고 만약에 그 정점에 방문하지 않았다면 q에 담아주고 while문을 돌게함
while문을 나왔을 땐 1의 모든 부모 정점들이 거꾸로 담겨있음, 그것을 ans라는 임시로 정점을 담을 list에 담아준 뒤 거꾸로 뒤집어줌

+채린's
while문을 돌면서 해당 정점을 향한 간선이 있는지 확인하고 만약 방문하지 않았다면 continue를 해줌,
그렇게 방문하지 않은 부모 정점이 있으면 전부 뛰어넘고 방문한 정점들만 출력해주고 전부 True가 될때까지 계속 반복함
'''
import sys
sys.stdin = open('test.txt', 'r')

def BFS(v):
    q = [v]
    ans = [v]
    visited[v] = True
    while q:
        if visited[1:V + 1] == [True for _ in range(V)]:
            break
        pv = q.pop(0)
        for w in range(1, V + 1):
            if G[w][pv] == 1:
                if visited[w] == False:
                    visited[w] = True
                    q.append(w)
        ans += q
    ans = ans[::-1]
    return ans


for tc in range(1, 11):
    V, E = map(int, input().split())
    G = [[0] * (V + 1) for _ in range(V + 1)]
    temp = list(map(int, input().split()))
    visited = [False for _ in range(V + 1)]

    for i in range(0, len(temp), 2):
        st, ed = temp[i], temp[i + 1]
        G[st][ed] = 1

    result = []
    for i in range(1, V + 1):
        if visited[i] == False:
            result.extend(BFS(i))

    print('#{}'.format(tc), end=' ')
    for r in result:
        print(r, end=' ')
    print()