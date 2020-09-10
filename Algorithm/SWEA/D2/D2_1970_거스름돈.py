for t in range(1, int(input())+1):
    N = int(input())
    index = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    print(f'#{t}')
    for i in range(8):
        res = N // index[i]
        N = N % index[i]
        print(f'{res}', end=' ')
    print()