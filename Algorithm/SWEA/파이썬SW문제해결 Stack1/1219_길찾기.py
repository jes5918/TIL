# 다시해야대 ㅠ
#
# import sys
# sys.stdin = open("input4.txt", "r")
#
# def f1(n):
#     global ans
#     if n > 0:
#         if n == 99:
#             ans = 1
#         f1(ch1[n])
#         f1(ch2[n])
# 
# for _ in range(10):
#     tc, E = map(int, input().split())
#     tmp = list(map(int, input().split()))
#     ch1 = [-1] * 100
#     ch2 = [-1] * 100
#     for i in range(E):
#         n1 = tmp[i * 2]
#         n2 = tmp[i * 2 + 1]
#         if ch1[n1] == -1:
#             ch1[n1] = n2
#         else:
#             ch2[n1] = n2
#         ans = 0
#         f1(0)
#         print('#{} {}'.format(tc, ))

