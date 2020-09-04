import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    natural_code = list(map(int, input().split()))
    K = int(input())
    order_code = list(input().split())
    stack = []
    res = []
    for code in order_code:
        if code == 'I':
            res.append(stack)
            stack = []
        else:
            stack.append(int(code))
    res.pop(0)
    res.append(stack)
    for i in range(K):
        natural_code[res[i][0]:0] = res[i][2:]
    print('#{} {}'.format(tc, ' '.join(str(x) for x in natural_code[:10])))