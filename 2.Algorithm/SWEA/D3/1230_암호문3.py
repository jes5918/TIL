import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    natural = list(map(int , input().split()))
    K = int(input())
    code = list(input().split())
    i = 0
    while i < len(code):
        if code[i] == 'I':
            natural[int(code[i+1]):0] = code[i+3:i+3+int(code[i+2])]
            i += int(code[i+2]) + 3
        elif code[i] == 'D':
            natural[int(code[i+1]):int(code[i+2])] = []
            i += 3
        elif code[i] == 'A':
            natural.append(code[int(code[i+2]):int(code[i+1])])
            i += int(code[i+1]) + 2
    print('#{} {}'.format(tc, ' '.join(str(x) for x in natural[:10])))