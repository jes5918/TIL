temp = input()
temp = temp.upper()
dict_temp = {}
for t in temp:
    dict_temp[t] = dict_temp.get(t, 0) + 1
res = sorted(dict_temp.items(), key=lambda x: -x[1])
if res[0][1] == res[1][1]:
    print('?')
else:
    print(res[0][0])