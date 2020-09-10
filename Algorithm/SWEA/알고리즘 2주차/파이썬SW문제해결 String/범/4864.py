for t in range(1,int(input())+1):
    a = input()
    b = input()
    res = 0
    if a in b:
        res += 1
    elif b in a:
        res += 1
    print(f'#{t} {res}')