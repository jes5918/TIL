import sys

#sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = input()
    M = input()
    result = 0
    if N in M:
        result = 1
    else:
        result = 0
    print(f'#{test_case} {result}')


# T = int(input())

# for test_case in range(1, T + 1):
#     N = input()
#     M = input()
#     n = len(N)
#     m = len(M)
#     i = 0
#     result = 0
#     while i <= m-n:
#         j = n-1
#         while j >=0:
#             if N[j] != M[i+j]:
#                 if M[i+j] in N:
#                     move = n -(N.index(M[i+j])) - 1
#                 else:
#                     move = n
#                     break
#             j -= 1
#         if j == -1:
#             result = 1
#             break
#         else:
#             i += move

#     print(f'#{test_case} {result}')

    