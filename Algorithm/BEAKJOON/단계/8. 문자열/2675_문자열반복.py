for tc in range(int(input())):
    N, strings = input().split()
    N = int(N)
    for s in strings:
        print('{}'.format(s) * N, end='')
    print()