T = int(input())

for test_case in range(1, T + 1):
    datas = map(int, input().split())
    data_sum= sum(n for n in datas if n % 2 == 1)
    print(f'#{test_case} {data_sum}')