import sys
sys.stdin = open('input6.txt', 'r')


def find_ans():
    for i in range(len(t)):
        for j in range(3):
            if int(t[i]) != j:
                temp = int(t[:i] + str(j) + t[i+1:], 3)
                if temp in candidate:
                    return temp


for tc in range(1, int(input()) + 1):
    b = input()
    t = input()
    candidate = []
    ans = 0
    for i in range(len(b)):
        for j in range(2):
            if int(b[i]) != j:
                candidate.append(int(b[:i] + str(j) + b[i+1:], 2))
    print('#{} {}'.format(tc, find_ans()))
