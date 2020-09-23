import sys
SPLITS = 20
def find_symmetric(arr, idx):
    r, l = idx - 1, idx + 1
    min_r, max_l = idx, idx
    while r > 0 and l < len(arr):
        if arr[r] == arr[l]:
            min_r, max_l = r, l
            r -= 1
            l += 1
        else:
            break
    return max(idx - min_r, max_l - idx)

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.insert(0, -1)
n = int(sys.stdin.readline())
for _ in range(n):
    sex, idx = map(int, sys.stdin.readline().split())
    if sex == 1:
        for idx in range(idx, len(arr), idx):
            arr[idx] = (arr[idx] + 1) % 2
    elif sex == 2:
        width = find_symmetric(arr, idx)
        temp = arr[idx-width : idx+width + 1]
        for i in range(len(temp)):
            temp[i] = (temp[i] + 1) % 2
        arr[idx-width:idx+width+1] = temp
for idx in range(1, len(arr), SPLITS):
    print(*arr[idx:idx+SPLITS])

# import sys
# N = int(sys.stdin.readline())
# switch = list(map(int, sys.stdin.readline().split()))
# K = int(sys.stdin.readline())
# for _ in range(K):
#     mw, num = map(int, sys.stdin.readline().split())
#     temp = num
#     if mw == 1:
#         cnt1 = 2
#         while temp <= N:
#             if switch[temp-1]:
#                 switch[temp-1] = 0
#             else:
#                 switch[temp-1] = 1
#             temp = num * cnt1
#             cnt1 += 1
#     elif mw == 2:
#         cnt = 0
#         while num-cnt-1 > 0 and num+cnt <= N:
#             if switch[num-cnt-1:num+cnt] == switch[num-cnt-1:num+cnt][::-1]:
#                 cnt += 1
#             else:
#                 break
#         for i in range(num - cnt - 1, num + cnt):
#             if switch[i]:
#                 switch[i] = 0
#             else:
#                 switch[i] = 1
# print(*switch)
