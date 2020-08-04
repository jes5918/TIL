T = int(input())
for t in range(1, T+1):
    cards = int(input())
    card_num = list(map(int, input()))
    card_dict = dict()
    max_n = 0
    max_num = 0
    for i in card_num:
        if i not in card_dict.keys():
            card_dict[i] = 1
        else:
            card_dict[i] += 1
    cnt_values = list(card_dict.values())
    cnt_keys = list(card_dict.keys())
    for j in range(len(cnt_values)-1):
        if cnt_values[j] == cnt_values[j+1]:
            max_n = max(cnt_values)
            max_num = max(cnt_keys)
            continue
        else:
            max_n = max(cnt_values)
            max_num = cnt_keys[cnt_values.index(max(cnt_values))]
            break
    print(f'#{t} {max_num} {max_n}')