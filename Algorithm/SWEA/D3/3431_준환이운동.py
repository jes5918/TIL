T = int(input())
for tc in range(1, T+1):
    minutes = list(map(int, input().split()))
    if max(minutes) == minutes[2]:
        res = -1
    elif (min(minutes) != minutes[2]) and (max(minutes) != minutes[2]):
        res = 0
    else:
        res = minutes[0] - minutes[2]
    print(f'#{tc} {res}')