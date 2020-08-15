T = int(input())
for tc in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    fee_a = P * W
    if W >= R:
        fee_b = Q + ((W - R) * S)
    else:
        fee_b = Q 
    print(f'#{tc} {fee_b}') if fee_a >= fee_b else print(f'#{tc} {fee_a}')