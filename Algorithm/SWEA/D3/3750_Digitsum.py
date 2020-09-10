import sys
sys.stdin = open('input.txt', 'r')
# runtime 문제 발생 TC를 append 하는게 더빠른가
TC = []
for tc in range(1, int(input())+1):
    N = int(input())
    while True:
        N = str(N)
        if len(N) == 1:
            TC.append(N)
            break
        else:
            b = []
            for i in N:
                b.append(int(i))
            N = str(sum(b))
j = 1
for i in TC:
    print('#{} {}'.format(j, i))
    j += 1
