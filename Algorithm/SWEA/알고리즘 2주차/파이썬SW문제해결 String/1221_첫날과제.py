# 딕셔너리로 풀어보자
# input에 #1도 입력받는거 주의하고
# 입력테이터를 리스트로 저장받고
# 딕셔너리의 dict_num[key] = get(key, default) + 1를 이용해서 {'ZRO': 213, 'ONE': 123...}이런식으로 저장되게 한다.
# 출력이 조금 생각할 시간이 필요했다
# #을 포함한 test_case는 일단 받았고
# 다음줄부터 for 문을 이용해 출력을 한다.
# 순서가 없는 dict를 순서대로 출력하기 위해 index_num 이라는 비교데이터를 만들어준다
# 그 후 차례대로 불러오면 끝이겠지


for tc in range(1, int(input())+1):
    test_case, N = input().split()
    number_list = list(input().split()) # 입력받자 입력을 받아
    index_num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"] # 비교를 위해 인덱스를 준다.
    dict_num = {} # dict로 풀자

    # 딕셔너리의 dict_num[key] = get(key, default) + 1를 이용한 결과 -> {'ZRO': 213, 'ONE': 123...}
    for number in number_list: # 데이터가 들어있는 number_list에서 하나하나꺼내서 확인
        dict_num[number] = dict_num.get(number, 0) + 1 # dict에 값을 저장하자

    print(test_case)  # #1을 출력한다
    for i in range(10):
        a = dict_num[index_num[i]] # dict_num의 key 값인 index_num[i] => 순서대로 위의 인덱스를 불러오자,,,
        print(f'{index_num[i]} '*a, end='')
    print() # 테스트 케이스 마다 띄워줘야 하니 추가