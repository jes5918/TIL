# def pascal(sp):
#     a = 1
#     if sp == 1:
#         return 1
#     elif sp


# T = int(input())
# for tc in range(1, T+1):
#     print(f'#{tc}')
#     for x in range(1, tc+1):
#         print(pascal(x))

T = int(input())
for tc in range(1, T+1):
    sp = int(input())
    psc = list([1 for b in range(a+1)] for a in range(sp))
    for i in range(2, sp):
        for j in range(1, i):
            psc[i][j] = psc[i-1][j-1] + psc[i-1][j]
    
    print(f'#{tc}')
    for x in range(sp):
        for y in range(x+1):
            print(psc[x][y], end=' ')
        print()