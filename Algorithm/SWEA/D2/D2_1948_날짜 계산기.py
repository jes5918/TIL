T = int(input())
for tc in range(1, T+1):
    month_st, day_st, month_end, day_end = map(int, input().split())  # 차례로 입력받자
    lastday = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # 1~12월까지 순서대로 마지막날이 언젠지 인덱싱하자
    res = 0  # 결과 값 초기화
    if month_st == month_end: # 만약 3월 과 3월을 비교하게 된다면 day만 계산하면 되기 때문에 따로 조건문을 사용한다.
        res = day_end - day_st + 1  # 마지막날에서 처음날 빼고 +1 하면 기간
    else:   # 다른월 끼리 비교하자
        res = (lastday[month_st-1] - day_st + 1) + day_end  # 예를 들어 3월에서 6월의 기간을 계산할 때 3월과 6월의 짤짤이 계산, 4,5월은 아래 포문으로 계산
        for i in range(month_st+1, month_end):  # 예를들어 3월부터 6월 계산할 때 4월과 5월의 총 일수 합치자~
            res += lastday[i-1] # 결과값에 4월과 5월 일수 더해더해~
    print(f'#{tc} {res}')   # 출력출력