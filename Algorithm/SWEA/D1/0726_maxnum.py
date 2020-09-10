T = int(input())
for test_case in range(1, T + 1):
    max_number = 0
    lists = list(map(int, input().split()))
    for i in lists:
        if max_number < i:
            max_number = i
    print(f'#{test_case} {max_number}')