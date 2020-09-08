last_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
T = int(input())
for test_case in range(1, T + 1):
    date = input()
    year = int(date[0:4])
    month = int(date[4:6])
    day = int(date[6:8])
    res = '-1'
    if 0 < month < 13 and 0 < day < last_day[month - 1] + 1:
        res = date[0:4] + '/' + date[4:6] + '/' + date[6:8]
    print(f'#{test_case} {res}')