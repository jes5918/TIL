def puzzle(arr): # 퍼즐탐색
    count = 0
    for x in range(N):
        cnt = 0
        for y in range(N):
            if arr[x][y]:
                cnt += 1
                if y == N - 1 and cnt == K: # 마지막 끝에 도착했을 때 길이가 K이면
                    count += 1
            else:
                if cnt == K:
                    count += 1
                cnt = 0
    return count

def rotate90(arr, N): # 배열 90도 돌리는 함수
    temp = [[0]*N for _ in range(N)] # array와 동일한 크기의 배열 초기화
    for i in range(N):
        for j in range(N):
            temp[j][N-i-1] = arr[i][j] # 90도 회전하자
    return temp

for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    array = [[int(x) for x in input().split()] for _ in range(N)]
    a = puzzle(array)
    b = puzzle(rotate90(array, N))
    print('#{} {}'.format(tc, a+b))