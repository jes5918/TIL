# 이건 딕셔너리 키 밸류 값으로 풀어볼까?
# get 함수도 써봐야겠넹

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split())) # 우선 숫자들 입력받자 1000개...
    grades = {} # 빈 딕셔너리 초기화
    
    for num in numbers: # 숫자 받은거 하나씩 돌려보자
        # .get(x, default)를 이용해 key 값이 없다면 그 value 값을 0으로 한다.
        grades[num] = grades.get(num, 0) + 1 # 그후 + 1을 해주어 새롭게 딕셔너리에 key = num 과 value = 1 로 저장한다.
    
    # lambda에 대해서는 인터넷 검색을 통해서 꼭 공부하자
    # sorted lambda 를 이용해 value를 내림차순으로 먼저 정렬하고 동일한 값이 있다면 key 값을 이용해 내림차순으로 하자.
    # 딕셔너리를 정렬하여 튜플형태로 새로운 grade_list에 넣자
    grades_list = sorted(grades.items(), key = lambda x : (-x[1], -x[0]))
    
    # 모두 내림차순으로 정렬 했으니 가장 첫번째 튜플의 첫번째 값이 최빈수가 된다.
    print(f'#{tc} {grades_list[0][0]}')