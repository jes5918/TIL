for tc in range(1, int(input()) + 1):
    string1 = input()
    string2 = input()
    res = 0
    for i in range(len(string2) - len(string1)+1):
        if string1 == string2[i:i+len(string1)]:
            res = 1
    print(f'#{tc} {res}')