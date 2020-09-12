
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