# def is_palindrome1(a, n, m):
#     for i in range(n):
#         for j in range(n - m + 1):
#             for k in range(m // 2):
#                 if a[i][j + k] != a[i][j + m - 1 - k]:
#                     break
#             else:
#                 return m
#     return 0
#
#
# def is_palindrome2(a, n, m):
#     for i in range(n):
#         for j in range(n - m + 1):
#             # if list(a[i])[j:j+m] == list(reversed(list(a[i])[j:j+m])):
#             if a[i][j:j + m] == (a[i][j:j + m])[::-1]:
#                 return m
#     return 0


def discrim(arr, n, m): # 회문인지 판별하는 함수
    for x in range(n): # 2차원 배열로 받아서 각 행을 하나씩 불러온다
        for y in range(n - m + 1): # 각 행에서 n=열의개수, m=회문의길이 즉 n-m+1번 하면 모든 경우의수 돌린다
            if arr[x][y:y + m] == arr[x][y:y + m][::-1]: # [::-1] 스터디때 배운 역슬라이싱 활용, 원본과 역슬라이싱한거 비교
                return m # 만약 회문이면 회문의길이인 m을 리턴
    return 0

for tc in range(10):
    n = 100
    test_case = int(input())
    arr = [[x for x in input()] for _ in range(n)] # 2차원 배열로 다받자

    result = 1 # 결과값은 1로 세팅(문제조건)
    len_pal = 2  # 첫 회문의 길이 세팅

    while len_pal <= 100 and len_pal <= result + 2:
        # while문의 조건 설명
        # len_pal <= 100 회문의길이가 최대 100까지 일 수 있으므로 조건지정
        # len_pal <= result + 2 이 조건을 통해서 실행시간 단축이 가능함 (회문의 속성 이용)
        if discrim(arr, n, len_pal) > result: # 회문의 최대길이를 판별하기 위해 조건문사용
            result = len_pal # 결과값에 최대길이의 회문 저장
        len_pal += 1 # 회문의 길이 +1 하고 while문 돌린다.

    # 가로회문을 확인하기 위한 과정 위와 동일하지만 단지 배열만 zip(*arr)로 회전(?)시켰다
    len_pal = 2
    while len_pal <= 100 and len_pal <= result + 2: # 가로를 찾기위해 한번더한다
        if discrim(list(zip(*arr)), n, len_pal) > result:
            result = len_pal
        len_pal += 1

    print("#{} {}".format(tc+1, result))

# def discrim(arr100):
#     result = 1
#     for x in range(N):
#         for y in range(N, result, -1):
#             if result > y:
#                 break
#             for k in range(N - y + 1):
#                 if arr100[x][k:y + k] == arr100[x][k:y + k][::-1]:
#                     if len(arr100[k:y + k]) > result:
#                         result = len(arr100[k:y + k])
#     return result
#
# def rotate90(arr100):
#     temp = [[0]*N for _ in range(N)]
#     for x in range(N):
#         for y in range(N):
#             temp[y][N-x-1] = arr100[x][y]
#     return temp
#
# for _ in range(10):
#     tc = int(input())
#     N = 100
#     arr = [[x for x in input()] for _ in range(N)]
#     a = discrim(arr)
#     arr90 = rotate90(arr)
#     b = discrim(arr90)
#     print('#{} {}'.format(tc, max(a, b)))