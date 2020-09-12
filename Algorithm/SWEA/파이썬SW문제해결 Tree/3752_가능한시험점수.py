import sys
sys.stdin = open('3752.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    point = list(map(int, input().split()))
    # 최대 포인트 선언
    max_point = sum(point)
    # 방문배열활용 최대 포인트의 인덱스 편하게 하기위해 +1 했음
    visited = [0] * (max_point + 1)
    # 포인트의 경우의 수가 저장될 리스트
    res = [0]
    # 포인트를 하나씩 돌아보자
    for p in point:
        # 모든 조합을 생각해보자
        for x in range(len(res)):
            # 이 점수에 방문하지 않았다면
            if not visited[p + res[x]]:
                # 결과 리스트에 점수 저장
                res.append(p + res[x])
                # 이 점수는 방문했다 표시
                visited[p + res[x]] = 1
    # 경우의 수를 출력하라고 했으니 결과값의 길이 출력
    print('#{} {}'.format(tc, len(res)))

# 교수님 풀이
# for tc in range(1, int(input())+1):
#     N = int(input())
#     score = list(map(int, input().split()))
#     visit = [[0] * (sum(score)+1) for _ in range(N+1)]
#
#     def dfs(k, s):
#         if visit[k][s]:
#             return
#         visit[k][s] = 1
#         if k == N:
#             return
#         dfs(k+1, s)
#         dfs(k+1, s+score[k])
#
#     dfs(0, 0)
#     print('#{} {}'.format(tc, sum(visit[N])))


# 백트레킹은 시간초과
# def powerset(idx):
#     if idx == N:
#         total = 0
#         for i in range(N):
#             if sel[i]:
#                 total += score[i]
#         result.add(total)
#         return
#     sel[idx] = 1
#     powerset(idx + 1)
#     sel[idx] = 0
#     powerset(idx + 1)
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     score = list(map(int, input().split()))
#     sel = [0] * N
#     result = set()
#     powerset(0)
#     print('#{} {}'.format(tc, len(result)))



# # 구조교 코드
# for t in range(int(input())):
#     input();a=1
#     for i in map(int,input().split()):a|=a<<i
#     print(f'#{t+1}',bin(a).count('1'))