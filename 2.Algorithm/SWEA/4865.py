for tc in range(1, int(input())+1):
    str1 = input()
    str2 = input()
    temp = {}
    for x in str1:
        temp[x] = 0
    for y in str2:
        if y in temp:
            temp[y] += 1

    print(f'#{tc} {max(temp.values())}')