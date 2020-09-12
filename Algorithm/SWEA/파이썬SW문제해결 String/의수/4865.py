for tc in range(1, int(input())+1):
    str1 = input()
    str2 = input()
    temp = {}
    for x in str1:
        temp[x] = str2.count(x)
    print(f'{tc} {max(temp.value())}')
    