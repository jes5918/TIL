import sys
sys.stdin = open('input.txt', 'r')

def check(temp_deck):
    global flag
    sorted_deck = sorted(temp_deck)
    setted_deck = sorted(list(set(temp_deck)))

    # run 확인하는 과정
    cnt = 1
    temp = setted_deck[0]
    for i in range(1, len(setted_deck)):
        if temp + 1 == setted_deck[i]:
            cnt += 1
        else:
            cnt = 1
        temp = setted_deck[i]
        if cnt == 3:
            flag = True
            return

    # triplet 확인하는 과정
    cnt = 1
    temp = sorted_deck[0]
    for i in range(1, len(sorted_deck)):
        if temp == sorted_deck[i]:
            cnt += 1
        else:
            cnt = 1
        temp = sorted_deck[i]
        if cnt == 3:
            flag = True
            return


for tc in range(1, int(input())+1):
    deck = list(map(int, input().strip().split()))
    player1 = []
    player2 = []
    res = 0
    flag = False
    for i in range(len(deck)):
        if i % 2 == 0:
            player1.append(deck[i])
            if len(player1) >= 3:
                check(player1)
                if flag:
                    res = 1
                    break
        else:
            player2.append(deck[i])
            if len(player2) >= 3:
                check(player2)
                if flag:
                    res = 2
                    break
    print('#{} {}'.format(tc, res))