#회문
#N을 2차원배열로 NXN을 만듦
#길이가 M인 회문이 가로, 세로 중 1개가 존재함
#가로, 세로를 돌면서 같은 것이 있는지 찾기
#N개 안에 M이 N-M+1개가 나오기 때문에 그만큼 돌려서 볼거야
#행이든 열이든 M//2만큼 돌건데(회문이기때문에 반만돈다)
#arr[i][j]==arr[i][k+M-j-1]이면 cnt를 해줌
#cnt가 M//2와 같아지면 그 단어를 k부터 K+M까지 slicing함

##다른방법(의수), 역슬라이싱으로도 풀 수 있음
# for x in range(n):  # 2차원 배열로 받아서 각 행을 하나씩 불러온다
#     for y in range(n - m + 1):  # 각 행에서 n=열의개수, m=회문의길이 즉 n-m+1번 하면 모든 경우의수 돌린다
#         if arr[x][y:y + m] == arr[x][y:y + m][::-1]:  # [::-1] 스터디때 배운 역슬라이싱 활용, 원본과 역슬라이싱한거 비교
#             return m  # 만약 회문이면 회문의길이인 m을 리턴
# return 0

import sys
sys.stdin=open('input.txt','r')


# 100X100에 회문이 있는지 확인하고, 회문이 있다면 가징 긴 길이를 출력
# 회문인지 판별하는 함수를 만든다
# 세로일 때 90도로 돌리는 함수를 만든다
# 회문의 길이를 지정하는 함수를 만든다(100에서 작아짐, 진범님 idea)

def palindrome(arr):
    for i in range(100):
        for k in range(100 - M + 1):
            if arr[i][k:k + M] == arr[i][k:k + M][::-1]:  # 회문 길이 M만큼 slicing하고 역순이랑 같은지 확인
                return M  # 같다면 회문의 길이 반환
    return 0  # 회문이 아니면 0


def rota90(arr):
    temp = [[0] * 100 for _ in range(100)]
    for i in range(100):
        for j in range(100):
            temp[j][100 - i - 1] = arr[i][j]
    return temp


MAX_len = 1  # 초기값, 1단어도 회문1
M = 100  # 초기 LEN값, 줄어들예정
for tc in range(1, 10):
    T = int(input())
    arr = [list(input()) for _ in range(100)]
    while M > 0:  # M값은 1~100사이
        if palindrome(arr) or palindrome(rota90(arr)):  # 가로, 세로 중 값이 true이면 그 값이 최고 회문값
            MAX_len = M
            print('#{} {}'.format(tc, MAX_len))
            break  # 최고를 찾았으니 멈춤
        else:
            M -= 1  # 초기LEN값을 줄여준다