def discrim(arr):
    for i in range(N):
        for j in range(N-M+1):
            cnt = 0
            for x in range(M//2):
                if arr[i][j+x] == arr[i][j+M-x-1]:
                    cnt += 1
            if cnt == M//2: 
                return arr[i][j:j+M]
    return 0    

def rotate90(arr):
    temp = [[0]*N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            temp[y][N-x-1] = arr[x][y]
    return temp

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [[x for x in input()] for _ in range(N)]
    result = discrim(arr)  # 회문이 없으면 0 내놓고 아니면 결과출력
    if result == 0:
        ro90 = rotate90(arr)
        result = discrim(ro90)
    result = ''.join(result) 
    print(f'#{tc} {result}')
    
# T = int(input())

# for TC in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [list(input()) for _ in range(N)]
#     switch = 0

#     for i in range(N):
#         if switch:
#             break
#         for j in range(N-M+1):
#             temp = ''
#             for k in range(M):
#                 temp += arr[i][j+k]
#             if temp == temp[::-1]:
#                 result = temp
#                 switch = 1
#                 break

#     for j in range(N):
#         if switch:
#             break
#         for i in range(N-M+1):
#             temp = ''
#             for k in range(M):
#                 temp += arr[i+k][j]
#             if temp == temp[::-1]:
#                 result = temp
#                 break

#     print('#{} '.format(TC), end='')
#     print(result)
