T = int(input())
for tc in range(1, T + 1):
    list_1 = list(map(int, input().split()))
    avr = round(sum(list_1) / len(list_1))
    print(f'#{tc} {avr}')