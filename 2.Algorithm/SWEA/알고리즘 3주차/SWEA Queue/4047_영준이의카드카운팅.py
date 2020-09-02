import sys
sys.stdin = open('4047.txt', 'r')

for tc in range(1, int(input())+1):
    cards = input()
    # dict에 저장해보자 value는 리스트
    card_dict = {'S':[], 'D':[], 'H':[], 'C':[]}
    # cards 입력받은 것을 3개 단위로 잘라서 첫번째는 deck에 2,3번째는 deck_num에 저장
    for i in range(0, len(cards), 3):
        # card_dict에 값 저장하자(list니 append 사용)
        card_dict[cards[i]].append(cards[i+1:i+3])

    # ERROR를 위한 flag 신호 초기화
    flag = True
    # 결과값 저장 하기 위한 res
    res = [13, 13, 13, 13]
    # res의 index를 표시하기 위해 변수 하나 설정
    i = 0
    # card_dict의 items을 돌리자돌려
    for dec, num in card_dict.items():
        # 중복되는 것이 있으면 flag로 error 발생
        if len(set(num)) != len(num):
            flag = False
            break
        # 중복되는 것이 없을때
        else:
            res[i] -= len(card_dict[dec])
            i += 1

    # flag = False면 실행
    if not flag:
        print('#{} ERROR'.format(tc))
    # 중복되는 것이 없을 때 그냥 정상적인 실행
    else:
        print('#{} {} {} {} {}'.format(tc, res[0], res[1], res[2], res[3]))