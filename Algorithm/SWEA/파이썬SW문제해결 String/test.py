# a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# b = list(zip(*a))
# for i in range(4):
#     print(b[i])

# def horizontal(x):
#     for j in range(N):
#         for i in range(N-M+1):
#             if x[j][i:i+M+1] == x[j][i:i+M+1][::-1]:
#                 return x[j][i:i+M+1]
#     return 0
#
# def rotate90(arr):
#     temp = [[0]*N for _ in range(N)]
#     for x in range(N):
#         for y in range(N):
#             temp[y][N-x-1] = arr[x][y]
#     return temp
#
#
# for tc in range(1, int(input())+1):
#     N, M = map(int, input().split())
#     arr = [[x for x in input()] for _ in range(N)]
#     result = horizontal(arr)  # 회문이 없으면 0 내놓고 아니면 결과출력
#     if result == 0:
#         ro90 = rotate90(arr)
#         result = horizontal(ro90)
#     result = ''.join(result)
#     print('#{} {}'.format(tc, result))

#회문
#N을 2차원배열로 NXN을 만듦
#길이가 M인 회문이 가로, 세로 중 1개가 존재함
#가로, 세로를 돌면서 같은 것이 있는지 찾기
#행이든 열이든 M//2만큼 돌건데(회문이기때문에 반만돈다)
#idx값이 i와 M-i-1가 같으면 temp에 idx를 저장하고, temp 개수가 M//2와 같아지면
#가장 작은 idx에서 부터 M-1까지 slicing으로 잘라 출력
import sys
sys.stdin=open('input.txt','r')

def row(arr):
    temp = []
    STR = ''
    for i in range(N):
        for j in range(M//2):
            if arr[i][j] == arr[i][M-j-1]:
                temp.append(j)
            else:
                temp = []
            if len(temp) == M//2:
                # STR = arr[i][temp[0]:M-temp[0]-1]
                for idx in range(temp[0], M):
                    STR += arr[i][idx]
                return STR

def col(arr):
    temp = []
    STR = ''
    for i in range(N):
        for j in range(M//2):
            if arr[j][i] == arr[M-j-1][i]:
                temp.append(j)
            else:
                temp = []
            if len(temp) == M//2:
                for idx in range(temp[0],M):
                    STR += arr[idx][i]
                return STR

for tc in range(1,int(input())+1):
    N, M = map(int,input().split())
    arr = [list(input()) for _ in range(N)]
    ROW = row(arr)
    COL = col(arr)
    if ROW:
        print('#{} {}'.format(tc,ROW))
    else:
        print('#{} {}'.format(tc,COL))