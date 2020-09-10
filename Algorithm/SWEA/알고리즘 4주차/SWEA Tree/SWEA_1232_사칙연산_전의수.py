import sys
sys.stdin = open('1232.txt', 'r')

# 후위 순회
def LRP(x):
    # L 왼쪽자식 확인
    if L[x]:
        # 왼쪽 자식으로 다시 파고들자
        LRP(L[x])
    # R 오른쪽 자식 확인
    if R[x]:
        # 오른쪽 자식으로 다시 파고들자
        LRP(R[x])
    # P 후위 계산
    calculate(x)

def calculate(x):
    # P에는 x번호 노드에 담겨진 값이 저장되어 있다.
    # 연산자있는 자리의 왼쪽자식 데이터랑 오른쪽 자식 데이터를 계산
    if P[x] == '+':
        P[x] = P[L[x]] + P[R[x]]
    elif P[x] == '-':
        P[x] = P[L[x]] - P[R[x]]
    elif P[x] == '*':
        P[x] = P[L[x]] * P[R[x]]
    elif P[x] == '/':
        P[x] = P[L[x]] / P[R[x]]

for tc in range(1, 11):
    N = int(input())
    # 왼쪽 자식 초기화
    L = [0] * (N + 1)
    # 오른쪽 자식 초기화
    R = [0] * (N + 1)
    # 노드에 담긴 데이터 저장할 곳
    P = [0] * (N + 1)
    for i in range(N):
        t = list(input().split())
        # 입력이 4개 주어질 떄
        if len(t) == 4:
            P[int(t[0])] = t[1]
            L[int(t[0])] = int(t[2])
            R[int(t[0])] = int(t[3])
        # 입력이 2개 주어질 때(최 하위 노드들)
        else:
            P[int(t[0])] = int(t[1])
    # 후위 순회 계산
    LRP(1)
    # 결과값은 int 형으로 나와야 한다고 했으니 트리의 맨 위쪽(1번노드) 출력
    print('#{} {}'.format(tc, int(P[1])))


# 구조교 코드
# def s(i):
#     if len(n[i])
#         return str(int(eval(s(n[i][0])+o[i]+s(n[i][1]))))
#     else:
#         o[i]
# for t in range(10):
#     o=[0];n=[0]
#     for i in range(int(input())):
#         a,b,*c=input().split()
#         o+=[b]
#         n+=[[*map(int,c)]]
#     print(f'#{t+1}',s(1))



