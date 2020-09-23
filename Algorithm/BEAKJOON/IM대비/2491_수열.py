# 처음에 풀었던 코드,,, 시간초과 난다
# N = int(input())
# numbers = list(map(int, input().split()))
# MAX = 0
# for i in range(len(numbers)):
#     for j in range(i+1, len(numbers)+1):
#         temp = numbers[i:j]
#         sorted_up_temp = sorted(temp)
#         sorted_down_temp = sorted(temp, reverse=True)
#         if temp == sorted_up_temp or temp == sorted_down_temp:
#             l = len(temp)
#             if l > MAX:
#                 MAX = l
# print(MAX)