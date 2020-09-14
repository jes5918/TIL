import sys
sys.stdin = open('input.txt', 'r')

def check(x):
    for i in range(1, len(x)):
        if ord(x[i]) < 97 or ord(x[i]) > 122:
            return 0
    return 1

for tc in range(1, int(input())+1):
    N = int(input())
    string_list = list(map(str, input().split()))
    res = []
    cnt = 0
    for word in string_list:
        if word[-1] == '?' or word[-1] == '!' or word[-1] == '.':
            if 65 <= ord(word[0]) <= 90:
                cnt += check(word[:len(word) - 1:])
            res.append(cnt)
            cnt = 0
        else:
            if 65 <= ord(word[0]) <= 90:
                cnt += check(word)

    print('#{} '.format(tc), end='')
    print(*res)