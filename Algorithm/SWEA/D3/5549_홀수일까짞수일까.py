for tc in range(1, int(input())+1):
    N = int(input())
    if N % 2 == 1:
        print('#{} Odd'.format(tc))
    elif N % 2 == 0:
        print('#{} Even'.format(tc))