T = int(input())
for tc in range(1, T+1):
    patern_str = input()
    for n in range(1, 15):
        if patern_str[:n] == patern_str[n:2*n]:
            break
    print(f'#{tc} {n}')