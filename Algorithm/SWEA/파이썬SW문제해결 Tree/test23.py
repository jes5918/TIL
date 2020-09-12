import sys
sys.stdin = open('1248.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    # V 트리의 정점 총 수, E간선 총수, 공통 조상 찾는 두 정점 번호 a,b
    V, E, a, b = map(int, input().split())
    arr = list(map(int, input().split()))
    # 인접리스트에 담기
    G = [[] for _ in range(V + 1)]
    for i in range(0, len(arr), 2):
        st, ed = arr[i], arr[i + 1]
        G[st].append(ed)
    # print(G)
    A = []
    B = []
    parent = 0
    while True:
        # 공통조상을 찾음!
        if a == b:
            break
        for i in range(1, V + 1):
            # a정점의 조상을 찾으면 a를 그 조상으로 바꿔줌
            if a in G[i]:
                A.append(i)
                a = i
                # print(i,'a')
            if b in G[i]:
                B.append(i)
                b = i
                # print(b,'b')

    for k in A:
        for l in B:
            if k == l:
                parent = k
                break
        if parent == k:
            break
    # print(G)
    # print(parent)
    # print(A,B)
    # print(parent,'공통조상')
    # 공통조상을 찾았으니 해당 정점의 서브트리 개수 구하기
    # 정점이 parent가 아닐때까지의 G[idx]의 개수를 더하고 해당 parent 개수까지 1 더해줌
    num = 1  # parent의 개수 이미 더해놨다

    def sooa(x):
        global num
        for i in range(len(G[x])):
            num += 1
            sooa(G[x][i])

    sooa(parent)
    print('#{} {} {}'.format(tc, parent, num))