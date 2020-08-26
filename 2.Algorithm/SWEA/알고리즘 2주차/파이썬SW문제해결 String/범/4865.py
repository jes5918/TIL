for t in range(1, 1+int(input())):
    a = input()
    b = input()
    new_a = list(set(a))
    m = 0
    for i in new_a:
        cnt = 0
        for j in b:
            if i == j:
                cnt += 1
        if cnt > m:
            m = cnt
    print(f'#{t} {m}')
