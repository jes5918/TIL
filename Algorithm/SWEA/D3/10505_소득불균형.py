for tc in range(1, int(input())+1):
    N = int(input())
    incomes = list(map(int, input().split()))
    average_income = sum(incomes)/len(incomes)
    cnt = 0
    for income in incomes:
        if average_income >= income:
            cnt += 1
    print(f'#{tc} {cnt}')