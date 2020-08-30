# import sys
#
# N = int(input())
# d = {}
# for i in range(N):
#     a = int(sys.stdin.readline())
#     d[a] = d.get(a, 0) + 1
#
# for sorted in sorted(d.items()):
#         for i in range(sorted[1]):
#             print(sorted[0])
#
# # a = sorted(d.items(), key=lambda x: x[0])
# # for i in range(len(a)):
# #     for j in range(a[i][1]):
# #         print(a[i][0])
#
# import sys
# N = int(input())
# dic = {}
# for i in range(N):
#     a = int(sys.stdin.readline())
#     if a in dic:
#         dic[a] =  dic[a] +1
#     else:
#         dic[a] = 1
# for sorted in sorted(dic.items()):
#     for i in range(sorted[1]):
#         print(sorted[0])