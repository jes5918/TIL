T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lists = [[str(x) for x in input().split()] for _ in range(N)] # N개의 알파뱃을 2차원 배열 스트링형태로 저장 ex) [['A', '3'], ['B', '2']]
    tmp = []
    for i in range(N):
        tmp.extend(lists[i][0] * int(lists[i][1])) # tmp = ['A', 'A', 'A', 'B', 'B']

    print(f'#{tc}')
    for x in range(len(tmp)//10+1): #tmp만들어진 것의 길이를 10로 나눈 몫의 수만큼 for문 반복
        res = tmp[10*x:10*(x+1)] # tmp를 10개씩 슬리이싱한다.
        res = ''.join(res) # 리스트 10개를 join함수로 합친다
        print(res) # 한줄 출력