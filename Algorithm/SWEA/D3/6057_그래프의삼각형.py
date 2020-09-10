# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     lists = []
#     for _ in range(M):
#         line = list(map(int, input().split()))
#         lists.append(line)
    
#     cnt = 0  
#     for x in range(M-1):
#         for y in range(x+1, M):
#             if (lists[x][1] == lists[y][0]) and (sorted([lists[x][0], lists[y][1]]) in lists) and (x != y):
#                 cnt += 1
    
#     print(f'#{tc} {cnt}')
    
# 먼가 오류가 나네....오바메모리
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lists = []
    for _ in range(M):
        line = list(map(int, input().split()))
        lists.append(line)
    cnt = 0  
    for x in range(M):
        for y in range(x+1, M):
            for z in range(y+1, M):
                temp = []
                temp.extend(lists[x])
                temp.extend(lists[y])
                temp.extend(lists[z])
                if len(set(temp)) == 3:
                    cnt += 1
    print(f'#{tc} {cnt}')

# T = int(input())
# for tc in range(1,T+1):
#     N,M = list(map(int,input().split()))
#     lists = [[0 for j in range(N+1)] for i in range(N+1)]
#     for i in range(M):
#         x,y = list(map(int,input().split()))
#         lists[x][y] = 1
#         lists[y][x] = 1
#     res = 0
#     for i in range(1,N+1):
#         for j in range(i+1,N+1):
#             for k in range(j+1,N+1):
#                 if lists[i][j] and lists[j][k] and lists[k][i]:
#                     res += 1
#     print(f'#{tc} {res}')