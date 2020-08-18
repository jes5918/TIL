for tc in range(1, int(input())+1):
    numbers = list(map(int, input().split()))
    sum3 = []
    for x in range(5):
        for y in range(x, 6):
            for z in range(y, 7):
                temp = [numbers[x], numbers[y], numbers[z]]
                sum3.append(sum(temp))
    sum3 = list(set(sum3))
    sum3 = sorted(sum3, reverse=True)
    print(sum3)
    print(f'#{tc} {sum3[4]}')