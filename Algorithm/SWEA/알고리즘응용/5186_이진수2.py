import sys
sys.stdin = open('input2.txt', 'r')

for tc in range(1, int(input())+1):
    num = float(input())
    result = ''
    for _ in range(12):
        num *= 2
        result += str(int(num) % 2)
        if num % 1 == 0:
            break
    else:
        result = 'overflow'
    print('#{} {}'.format(tc, result))