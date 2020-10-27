import sys
sys.stdin = open('1267.txt', 'r')

for tc in range(1, 11):
    # V 노드갯수, E 간선개수
    V, E = map(int, input().split())
    # 입력받는 부분
    arr = list(map(int, input().split()))
    # 인접행렬 초기화
    work = [[] for _ in range(V+1)]
    # 도착 노드가 저장될 임시 리스트
    temp = []
    # 결과값들이 저장 될 리스트
    res = [False] * (V+1)
    # 2개씩 잘라서 저장
    for i in range(0, len(arr), 2):
        # 인접행렬 저장
        work[arr[i]].append(arr[i+1])
        # 도착노드 저장
        temp.append(arr[i+1])

    for n in range(1, V):
        if n not in temp:
            # 순서를 같이 저장하기 위해서 리스트 형태로 저장
            res[n] = [1, n]
            # BFS활용
            q = []
            q.append(n)
            while q:
                nn = q.pop(0)
                for w in work[nn]:qe
                    # 결과값이 저장되어 있지 않은 부분이라면
                    if not res[w]:
                        # 결과값에 저장 (전 순위보다 1증가시켜서 저장)
                        res[w] = [res[nn][0]+1, w]
                        q.append(w)
                    else:
                        if res[w][0] < res[nn][0] + 1:
                            res[w][0] = res[nn][0] + 1
                            q.append(w)
    # 인덱싱을 편하기 위해서 추가했던것을 제거
    res.pop(0)
    # 들어가는 순서에 따라 정렬한다.
    # 같은 순서일 때는 상관 없으므로 정렬 안함
    res.sort(key=lambda x: x[0])
    print('#{} '.format(tc), end='')
    for r in res:
        print(r[1], end=' ')
    print()
