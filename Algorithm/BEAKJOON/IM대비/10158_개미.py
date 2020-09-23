import sys
W, H = map(int, sys.stdin.readline().split())
x, y = map(int, sys.stdin.readline().split())
T = int(sys.stdin.readline())
x += T
y += T
x = x % (2 * W)
y = y % (2 * H)
if x > W:
    x = 2 * W - x
if y > H:
    y = 2 * H - y
print(x, y)

# cnt = 0
# flag_x = False
# flag_y = False
# while cnt < T:
#     if flag_x:
#         x -= 1
#         if x == 0:
#             flag_x = False
#     else:
#         x += 1
#         if x == W:
#             flag_x = True
#
#     if flag_y:
#         y -= 1
#         if y == 0:
#             flag_y = False
#     else:
#         y += 1
#         if y == H:
#             flag_y = True
#     cnt += 1
# print(x, y)