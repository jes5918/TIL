T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input()))
    cnt = [0] * 10
    max_card = -1
    
    for i in range(N):
        cnt[cards[i]] += 1
    
    for i in range(9, -1, -1):
        if cnt[i] > max_card:
            res = i
            max_card = cnt[i]
    print(f'#{tc} {res} {cnt[res]}')