def selectionsort(now):
    global len_a
    if len_a <= now:
        return
    min_idx = now
    for i in range(now, len_a):
        if a[i] < a[min_idx]:
            min_idx = i
    a[now], a[min_idx] = a[min_idx], a[now]
    selectionsort(now+1)

a = [23, 4, 6, 1, 44, 23, 22, 7, 1]
len_a = len(a)
selectionsort(0)

# def countingsort(before, After, k):
#     temp = [0] * k
#
#     for i in range(0, len(After)):
#         temp[before[i]] += 1
#
#     for i in range(1, len(C)):
#         temp[i] += temp[i - 1]
#
#     for i in range(len(After)-1, -1, -1):
#         After[temp[before[i]] - 1] = before[i]
#         temp[before[i]] -= 1
#
# a = [23, 4, 6, 1, 44, 23, 22, 7, 1]
# b = [0] * len(a)
# countingsort(a, b, max(a)+1)