import sys
sys.stdin = open('input.txt', 'r')

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
