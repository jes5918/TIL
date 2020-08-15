T = int(input())
for tc in range(1, T+1):
    N = int(input())
    index = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    li = [list(str(N))[0]]
    sp = 0
    while True:
        sp += 1
        num = N * sp
        num_str = list(str(num))
        li.extend(num_str)
        res = set(li)
        if res == index:
            break
    print(f'#{tc} {num}')