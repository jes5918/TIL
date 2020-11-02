import sys

sys.stdin = open('input8.txt', 'r')


def merge_sort(a):
    if len(a) == 1:
        return a
    mid = len(a) // 2
    left = a[:mid]
    right = a[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


def merge(left, right):
    global cnt
    res = []
    if left[-1] > right[-1]:
        cnt += 1
    l_idx = 0
    r_idx = 0
    while len(left) > l_idx or len(right) > r_idx:
        if len(left) > l_idx and len(right) > r_idx:
            if left[l_idx] <= right[r_idx]:
                res += [left[l_idx]]
                l_idx += 1
            else:
                res += [right[r_idx]]
                r_idx += 1
        elif len(left) > l_idx:
            res += [left[l_idx]]
            l_idx += 1
        elif len(right) > r_idx:
            res += [right[r_idx]]
            r_idx += 1
    return res


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    arr = merge_sort(arr)
    print('#{} {} {}'.format(tc, arr[N // 2], cnt))
