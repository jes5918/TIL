import sys
sys.stdin = open('5110.txt', 'r')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    for i in range(1, M):
        new_list = list(map(int, input().split()))
        for j in range(M*i):
            if num_list[j] > new_list[0]:
                num_list[j:0] = new_list
                break
        if len(num_list) == M*i:
            num_list.extend(new_list)
    print('#{}'.format(tc), end=' ')
    for i in range(10):
        print('{}'.format(num_list[-1-i]), end=' ')
    print()


# 답은 맞는데 제한시간초과,,,
# def addnum(idx, num, arr):
#     s1 = arr[:idx]
#     s2 = arr[idx:]
#     s1.extend(num)
#     return s1+s2
#
# for tc in range(1, int(input())+1):
#     N, M = map(int, input().split())
#     num_list = list(map(int, input().split()))
#     for i in range(M-1):
#         flag = False
#         new_list = list(map(int, input().split()))
#         temp = new_list[0]
#         for idx, num in enumerate(num_list):
#             if num > temp:
#                 num_list = addnum(idx, new_list, num_list)
#                 break
#             if idx == M-1:
#                 flag = True
#         if flag:
#             num_list.extend(new_list)
#     print('#{}'.format(tc), end=' ')
#     for i in range(10):
#         print('{}'.format(num_list[-1-i]), end=' ')
#     print()