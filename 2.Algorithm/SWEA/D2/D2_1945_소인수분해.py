# T = int(input())
# for tc in range(1, T + 1):
#     a, b, c, d, e = 0, 0, 0, 0, 0
#     num = int(input())
    
#     while num % 2 == 0:
#         a += 1
#         num = num // 2
#     while num % 3 == 0:
#         b += 1
#         num = num // 3
#     while num % 5 == 0:
#         c += 1
#         num = num // 5
#     while num % 7 == 0:
#         d += 1
#         num = num // 7
#     while num % 11 == 0:
#         e += 1
#         num = num // 11
#     print(f'#{tc} {a} {b} {c} {d} {e}')T = int(input())
T = int(input())
for tc in range(1, T+1):
    number = int(input())
    print(f'#{tc}', end=' ')
    cnt = [0]*5
    while number != 1:
        if number % 2 == 0:
            number //= 2
            cnt[0] += 1
        elif number % 3 == 0:
            number //= 3
            cnt[1] += 1
        elif number % 5 == 0:
            number //= 5
            cnt[2] += 1
        elif number % 7 == 0:
            number //=7
            cnt[3] += 1
        elif number % 11 == 0:
            number //= 11
            cnt[4] += 1
    print(f'{cnt[0]} {cnt[1]} {cnt[2]} {cnt[3]} {cnt[4]}')