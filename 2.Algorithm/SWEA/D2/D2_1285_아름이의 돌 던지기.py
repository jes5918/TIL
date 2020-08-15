안댄당...
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     stone_throw = list(map(int, input().split()))
#     min_stone = abs(stone_throw[0])
#     cnt = 0
#     for stone in stone_throw:
#         if min_stone > abs(stone):
#             cnt = 1
#             min_stone = abs(stone)
#         elif min_stone == abs(stone):
#             cnt +=1
#     print(f'#{tc} {min_stone} {cnt}')