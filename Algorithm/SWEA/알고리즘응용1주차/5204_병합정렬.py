import sys
sys.stdin = open('input.txt', 'r')

# bad gateway 뜬다
def merge_sort(a):
    if len(a) == 1:
        return a
    mid = len(a)//2
    left = []
    right = []
    for x in a[:mid]:
        left.append(x)
    for x in a[mid:]:
        right.append(x)
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


def merge(left, right):
    global cnt
    res = []
    if left[-1] > right[-1]:
        cnt += 1
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                res.append(left.pop(0))
            else:
                res.append(right.pop(0))
        elif len(left) > 0:
            res.append(left.pop(0))
        elif len(right) > 0:
            res.append(right.pop(0))
    return res

for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    arr = merge_sort(arr)
    print('#{} {} {}'.format(tc, arr[N//2], cnt))

# 다른사람코드
# def merge(lst):
#     cnt = 0
#     len_lst = len(lst)
#     if len_lst <= 1:
#         return lst, cnt
#     else:
#         # 분리
#         left, left_cnt = merge(lst[: len_lst // 2])
#         right, right_cnt = merge(lst[len_lst // 2:])
# 
#         # 리스트 병합
#         my_lst = []  # 리턴 할 리스트
#         left_idx = right_idx = 0  # 좌우측 인덱스
#         right_is_small = False
#         for _ in range(len_lst):
#             if left_idx == len(left):  # 좌측 리스트가 먼저 동났을 때
#                 my_lst.append(right[right_idx])  # 우측 리스트에서 가져옴
#                 right_idx += 1
# 
#             elif right_idx == len(right):  # 우측 리스트가 먼저 동났을 때
#                 my_lst.append(left[left_idx])  # 좌측 리스트에서 가져옴
#                 left_idx += 1
#                 right_is_small = True  # 오른쪽 마지막 원소가 작은 경우
# 
#             elif left[left_idx] <= right[right_idx]:  # 좌측 리스트의 값이 작을 때
#                 my_lst.append(left[left_idx])  # 좌측 리스트에서 가져옴
#                 left_idx += 1
# 
#             else:  # 우측 리스트의 값이 작을 때
#                 my_lst.append(right[right_idx])  # 우측 리스트에서 가져옴
#                 right_idx += 1
# 
#         # cnt 계산
#         cnt = left_cnt + right_cnt
#         if right_is_small:  # 오른쪽 마지막 원소가 작은 경우
#             cnt += 1
# 
#         return my_lst, cnt
# 
# 
# def sorted_merge(lst):
#     sorted_lst, cnt = merge(lst)
#     return sorted_lst[N // 2], cnt
# 
# 
# T = int(input())
# for test_case in range(1, T + 1):
#     N = int(input())
#     lst = list(map(int, input().split()))
#     print('#{}'.format(test_case), *sorted_merge(lst))