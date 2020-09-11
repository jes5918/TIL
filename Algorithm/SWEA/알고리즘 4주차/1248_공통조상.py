import sys
sys.stdin = open('1248.txt', 'r')

# 조상노드가 처음으로 겹치는 부분 찾는 함수
def find_parent():
    for aa in a:
        for bb in b:
            if aa == bb:
                return aa

# 후위 순회로 자식의 갯수 찾기
def LRP(x):
    global cnt
    if L[x]:
        LRP(L[x])
    if R[x]:
        LRP(R[x])
    P[x] = x
    cnt += 1

for tc in range(1, int(input())+1):
    V, E, node1, node2 = map(int, input().split())
    tree = list(map(int, input().split()))
    L = [False] * (V+1)
    R = [False] * (V+1)
    P = [False] * (V+1)
    cnt = 0
    # 입력받는 부분
    for i in range(0, E*2, 2):
        if not L[tree[i]]:
            L[tree[i]] = tree[i+1]
        else:
            R[tree[i]] = tree[i+1]
        # 조상노드 저장
        P[tree[i+1]] = tree[i]

    # 두 정점의 부모노드 리스트 만들기
    a = []
    b = []
    while node1 != 1:
        a.append(P[node1])
        node1 = P[node1]

    while node2 != 1:
        b.append(P[node2])
        node2 = P[node2]

    # 최초의 같은 부모 노드 찾기
    res = find_parent()
    # 자식노드의 갯수 찾기
    LRP(res)
    print('#{} {} {}'.format(tc, res, cnt))