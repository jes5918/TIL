arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]

for i in range(1 << len(arr)):
    temp = []
    for j in range(len(arr)):
        if i & (1 << j):
            temp.append(arr[j])
    if sum(temp) == 0 and temp:
        print(temp)

# def check(temp_deck):
#     sorted_deck = sorted(temp_deck)
#     setted_deck = sorted(list(set(temp_deck)))
#
#     # run 확인하는 과정
#     cnt = 1
#     temp = setted_deck[0]
#     for i in range(1, len(setted_deck)):
#         if temp + 1 == setted_deck[i]:
#             cnt += 1
#         else:
#             cnt = 1
#         temp = setted_deck[i]
#         if cnt == 3:
#             print('run')
#             return
#
#     # triplet 확인하는 과정
#     cnt = 1
#     temp = sorted_deck[0]
#     for i in range(1, len(sorted_deck)):
#         if temp == sorted_deck[i]:
#             cnt += 1
#         else:
#             cnt = 1
#         temp = sorted_deck[i]
#         if cnt == 3:
#             print('triplet')
#             return
#
#
# a = [[1, 2, 4, 7, 8, 3],
#      [6, 6, 7, 7, 6, 7],
#      [0, 5, 4, 0, 6, 0],
#      [1, 0, 1, 1, 2, 3]]
#
# for deck in a:
#     check(deck)
