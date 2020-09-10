import sys
sys.stdin = open('5099.txt', 'r')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
    # 인덱스값 표현하기 위해 x 설정
    x = N
    q = []
    # 첫 판을 짜는 부분 q에는 [idx, 치즈의 수] 형태로 저장
    for i in range(N):
        q.append([i+1, pizza[i]])

    # 피자 화덕에 1만 남으면 종료
    while len(q) != 1:
        # 일단 첫번째꺼 반갈라
        q[0][1] //= 2
        # 0인게 나오면
        if q[0][1] == 0:
            # 남은 피자가 있으면 빼고 추가
            if x < M:
                q.pop(0)
                q.append([x+1, pizza[x]])
                x += 1
            # 남은 피자가 없다,, 그냥 빼자
            elif x >= M:
                q.pop(0)
        # 0인게 없으면 q를 통해 뒤를빼고 앞에 추가한다.
        else:
            q.append((q.pop(0)))
    print('#{} {}'.format(tc, q[0][0]))