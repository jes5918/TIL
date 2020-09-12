temp = input().upper()
list_temp = []
for i in set(temp):
    list_temp.append(temp.count(i))
idx = [i for i, x in enumerate(list_temp) if x == max(list_temp)]
if len(idx) > 1:
    print('?')
else:
    print(list(set(temp))[list_temp.index(max(list_temp))])


# 런타임 에러
# temp = input()
# temp = temp.upper()
# dict_temp = {}
# for t in temp:
#     dict_temp[t] = dict_temp.get(t, 0) + 1
# print(dict_temp)
# res = sorted(dict_temp.items(), key=lambda x: -x[1])
# if res[0][1] == res[1][1]:
#     print('?')
# else:
#     print(res[0][0])